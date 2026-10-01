#!/usr/bin/env node
/* Redirect check for the 18 old (no trailing slash) URLs from the Wix sitemap.
   Every old URL must answer 301 straight to its slashed equivalent, in one hop, and the
   destination must answer 200. Run against a preview or the live domain:

     node scripts/check-redirects.mjs https://green-estates-xyz.vercel.app
     node scripts/check-redirects.mjs https://greenestatesgardening.com.au

   Exit code 1 if anything is wrong, so it can gate a deploy. */

const base = (process.argv[2] || '').replace(/\/$/, '');
if (!base) { console.error('usage: node scripts/check-redirects.mjs <base-url>'); process.exit(2); }

const OLD = [
  '/', '/lawn-mowing-moreton-bay', '/hedge-trimming-moreton-bay', '/garden-cleanup-moreton-bay',
  '/mulching-services-moreton-bay', '/service-areas', '/about', '/contact', '/blog',
  '/blog/lawn-mowing-north-lakes', '/blog/lawn-mowing-redcliffe', '/blog/lawn-mowing-caboolture',
  '/blog/lawn-mowing-morayfield', '/blog/lawn-mowing-bribie-island', '/blog/garden-maintenance-north-lakes',
  '/blog/lawn-mowing-narangba', '/blog/garden-maintenance-redcliffe', '/blog/lawn-mowing-strathpine',
];
// New pages that have no old URL but must answer 200
const NEW = ['/acreage-mowing-moreton-bay/', '/garden-maintenance-moreton-bay/', '/sitemap.xml', '/robots.txt'];

const rows = []; let bad = 0;
for (const p of OLD) {
  const want = p === '/' ? '/' : p + '/';
  const r = await fetch(base + p, { redirect: 'manual' });
  const loc = r.headers.get('location') || '';
  let status = r.status, hops = 0, finalStatus = status, ok;
  if (p === '/') {
    ok = status === 200;
  } else {
    const locPath = loc.replace(/^https?:\/\/[^/]+/, '');
    hops = 1;
    const dest = loc.startsWith('http') ? loc : base + loc;
    const r2 = loc ? await fetch(dest, { redirect: 'manual' }) : { status: 0 };
    finalStatus = r2.status;
    ok = status === 301 && locPath === want && finalStatus === 200;
  }
  if (!ok) bad++;
  rows.push({ url: p, status, location: loc.replace(base, '') || '', final: finalStatus, ok: ok ? 'OK' : 'FAIL' });
}
for (const p of NEW) {
  const r = await fetch(base + p, { redirect: 'manual' });
  const ok = r.status === 200; if (!ok) bad++;
  rows.push({ url: p, status: r.status, location: '', final: r.status, ok: ok ? 'OK' : 'FAIL' });
}
console.table(rows);
console.log(bad ? `${bad} problem(s)` : 'all redirects correct: 301 in one hop, destinations 200');
process.exit(bad ? 1 : 0);
