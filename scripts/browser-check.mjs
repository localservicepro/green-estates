// Real-browser check: screenshots + interaction tests at mobile and desktop widths.
// Usage: node scripts/browser-check.mjs http://localhost:8080 out-dir
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import fs from 'node:fs';
const base = process.argv[2] || 'http://localhost:8080';
const out = process.argv[3] || 'scratch/shots';
fs.mkdirSync(out, { recursive: true });
const pages = ['/', '/lawn-mowing-moreton-bay/', '/hedge-trimming-moreton-bay/', '/garden-cleanup-moreton-bay/', '/mulching-services-moreton-bay/', '/about/', '/contact/', '/thank-you/'];
const browser = await chromium.launch({ executablePath: process.env.CHROMIUM || undefined });
const results = [];
for (const [label, vp, mobile] of [['desktop', { width: 1440, height: 900 }, false], ['mobile', { width: 375, height: 812 }, true]]) {
  const ctx = await browser.newContext({ viewport: vp, isMobile: mobile, hasTouch: mobile, deviceScaleFactor: mobile ? 2 : 1 });
  for (const p of pages) {
    const page = await ctx.newPage();
    const errors = [];
    page.on('pageerror', e => errors.push('pageerror: ' + e.message));
    page.on('console', m => { if (m.type() === 'error') errors.push('console: ' + m.text()); });
    page.on('requestfailed', r => { const u = r.url(); if (u.startsWith(base)) errors.push('requestfailed: ' + u); });
    await page.goto(base + p, { waitUntil: 'networkidle' });
    await page.waitForTimeout(2400);
    const hscroll = await page.evaluate(() => document.documentElement.scrollWidth > document.documentElement.clientWidth + 1);
    const h1s = await page.locator('h1').count();
    const title = await page.title();
    // top of page
    await page.screenshot({ path: `${out}/${label}${(p === '/' ? '_home' : p.replace(/\//g, '_').replace(/_$/, ''))}-top.png` });
    // full page after scrolling to trigger reveals
    await page.addStyleTag({ content: 'html{scroll-behavior:auto!important}' });
    await page.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 400) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 120)); } window.scrollTo(0, 0); });
    await page.waitForTimeout(600);
    await page.screenshot({ path: `${out}/${label}${(p === '/' ? '_home' : p.replace(/\//g, '_').replace(/_$/, ''))}-full.png`, fullPage: true });
    results.push({ label, p, title, h1s, hscroll, errors });
    await page.close();
  }
  await ctx.close();
}
// Interaction tests on desktop
{
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 } });
  const page = await ctx.newPage();
  await page.goto(base + '/', { waitUntil: 'networkidle' });
  await page.hover('.nav-trigger');
  await page.waitForTimeout(400);
  const ddVisible = await page.locator('#services-menu').isVisible();
  await page.screenshot({ path: `${out}/desktop-dropdown.png` });
  // header frosted after scroll
  await page.evaluate(() => window.scrollTo(0, 600)); await page.waitForTimeout(400);
  const scrolled = await page.locator('.site-header.scrolled').count();
  await page.screenshot({ path: `${out}/desktop-header-scrolled.png` });
  // form validation then submit -> redirect
  await page.evaluate(() => window.scrollTo(0, 0));
  await page.click('#quote button[type=submit]');
  await page.waitForTimeout(300);
  const errCount = await page.locator('#quote .field.has-error').count();
  await page.screenshot({ path: `${out}/desktop-form-errors.png` });
  await page.fill('#quote-name', 'Test Person'); await page.fill('#quote-phone', '0400 000 000'); await page.fill('#quote-email', 'test@example.com');
  await page.fill('#quote-address', '1 Test St, Caboolture'); await page.selectOption('#quote-service', 'Push Mowing');
  await page.click('#quote button[type=submit]');
  await page.waitForURL('**/thank-you/', { timeout: 5000 }).catch(() => {});
  const redirected = page.url().endsWith('/thank-you/');
  // FAQ + before/after
  await page.goto(base + '/garden-cleanup-moreton-bay/', { waitUntil: 'networkidle' });
  await page.locator('.faq details').first().locator('summary').click();
  const faqOpen = await page.locator('.faq details[open]').count();
  await page.locator('.ba input[type=range]').first().fill('20');
  const pos = await page.locator('.ba').first().evaluate(el => getComputedStyle(el).getPropertyValue('--pos').trim());
  results.push({ label: 'interactions', ddVisible, scrolled, errCount, redirected, faqOpen, baPos: pos });
  await ctx.close();
}
// Mobile interactions
{
  const ctx = await browser.newContext({ viewport: { width: 375, height: 812 }, isMobile: true, hasTouch: true, deviceScaleFactor: 2 });
  const page = await ctx.newPage();
  await page.goto(base + '/', { waitUntil: 'networkidle' });
  await page.tap('.nav-burger'); await page.waitForTimeout(500);
  const mnavOpen = await page.locator('.mobile-nav.open').isVisible();
  await page.tap('.m-acc'); await page.waitForTimeout(300);
  await page.screenshot({ path: `${out}/mobile-menu.png` });
  const subOpen = await page.locator('.m-sub.open').isVisible();
  const callbar = await page.locator('.callbar').isVisible();
  results.push({ label: 'mobile-interactions', mnavOpen, subOpen, callbar });
  await ctx.close();
}
await browser.close();
console.log(JSON.stringify(results, null, 1));
