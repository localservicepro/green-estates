/* Green Estates Gardening — site behaviour */
(function () {
  'use strict';
  var d = document, w = window;
  d.documentElement.classList.add('js');
  var reduce = w.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- Header ---------- */
  var header = d.querySelector('.site-header');
  function onScroll() { if (header) header.classList.toggle('scrolled', w.scrollY > 40); }
  w.addEventListener('scroll', onScroll, { passive: true }); onScroll();

  /* Services mega-dropdown: hover on pointer devices, click everywhere */
  var dd = d.querySelector('.nav-dropdown');
  if (dd) {
    var trigger = dd.querySelector('.nav-trigger');
    var hoverCapable = w.matchMedia('(hover: hover)').matches;
    var openDd = function () { dd.classList.add('open'); trigger.setAttribute('aria-expanded', 'true'); };
    var closeDd = function () { dd.classList.remove('open'); trigger.setAttribute('aria-expanded', 'false'); };
    if (hoverCapable) { dd.addEventListener('mouseenter', openDd); dd.addEventListener('mouseleave', closeDd); }
    trigger.addEventListener('click', function (e) { e.preventDefault(); dd.classList.contains('open') ? closeDd() : openDd(); });
    d.addEventListener('click', function (e) { if (!dd.contains(e.target)) closeDd(); });
    d.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeDd(); });
    dd.addEventListener('focusout', function (e) { if (!dd.contains(e.relatedTarget)) closeDd(); });
  }

  /* Mobile nav */
  var burger = d.querySelector('.nav-burger');
  var mnav = d.querySelector('.mobile-nav');
  if (burger && mnav) {
    var setOpen = function (open) {
      header.classList.toggle('is-open', open);
      mnav.classList.toggle('open', open);
      d.body.classList.toggle('nav-open', open);
      burger.setAttribute('aria-expanded', String(open));
      burger.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
      if (open) { var f = mnav.querySelector('a,button'); if (f) f.focus(); } else { burger.focus(); }
    };
    burger.addEventListener('click', function () { setOpen(!mnav.classList.contains('open')); });
    d.addEventListener('keydown', function (e) { if (e.key === 'Escape' && mnav.classList.contains('open')) setOpen(false); });
    mnav.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', function () { setOpen(false); }); });
    var acc = mnav.querySelector('.m-acc');
    if (acc) {
      var sub = mnav.querySelector('.m-sub');
      acc.addEventListener('click', function () {
        var open = acc.getAttribute('aria-expanded') === 'true';
        acc.setAttribute('aria-expanded', String(!open));
        sub.classList.toggle('open', !open);
      });
    }
    w.matchMedia('(min-width: 1024px)').addEventListener('change', function (e) { if (e.matches) setOpen(false); });
  }

  /* Active nav link */
  var path = location.pathname.replace(/index\.html$/, '');
  d.querySelectorAll('.nav-main a, .mobile-nav a').forEach(function (a) {
    var href = a.getAttribute('href');
    if (href && href.indexOf('#') === -1 && href === path) a.classList.add('is-active');
  });

  /* ---------- Before / after sliders ---------- */
  d.querySelectorAll('.ba').forEach(function (ba) {
    var range = ba.querySelector('input[type=range]');
    if (!range) return;
    var set = function () { ba.style.setProperty('--pos', range.value + '%'); };
    range.addEventListener('input', set); set();
  });

  /* ---------- Quote forms ---------- */
  d.querySelectorAll('form[data-quote-form]').forEach(function (form) {
    var summary = form.querySelector('.form-summary');
    var btn = form.querySelector('button[type=submit]');
    var msgs = {
      full_name: 'Please tell us your name.',
      email: 'Please enter a valid email address.',
      phone: 'Please enter a phone number we can call you on.',
      property_address: 'Please enter the property address or suburb.',
      service_needed: 'Please choose the service you need.'
    };
    function fieldWrap(el) { return el.closest('.field'); }
    function showError(el) {
      var fw = fieldWrap(el); if (!fw) return;
      fw.classList.add('has-error');
      var err = fw.querySelector('.error'); if (err) err.textContent = msgs[el.name] || 'Please complete this field.';
      el.setAttribute('aria-invalid', 'true');
    }
    function clearError(el) {
      var fw = fieldWrap(el); if (!fw) return;
      fw.classList.remove('has-error'); el.removeAttribute('aria-invalid');
    }
    form.setAttribute('novalidate', '');
    form.querySelectorAll('input,select,textarea').forEach(function (el) {
      el.addEventListener('input', function () { if (el.checkValidity()) clearError(el); });
      el.addEventListener('change', function () { if (el.checkValidity()) clearError(el); });
    });
    form.addEventListener('submit', function (e) {
      var invalid = [];
      form.querySelectorAll('input,select,textarea').forEach(function (el) {
        if (el.closest('.hp')) return;
        if (!el.checkValidity()) { invalid.push(el); showError(el); } else { clearError(el); }
      });
      var hp = form.querySelector('.hp input');
      if (hp && hp.value) { e.preventDefault(); return; }
      if (invalid.length) {
        e.preventDefault();
        if (summary) {
          summary.innerHTML = '<strong>Please check the highlighted fields.</strong> ' + invalid.map(function (el) {
            var lab = form.querySelector('label[for="' + el.id + '"]');
            return '<a href="#' + el.id + '">' + (lab ? lab.textContent.replace('(optional)', '').trim() : el.name) + '</a>';
          }).join(' · ');
          summary.classList.add('show');
          summary.setAttribute('tabindex', '-1'); summary.focus();
        }
        invalid[0].focus();
        return;
      }
      /* Valid: the GHL tracking script listens to this submit event and records the fields.
         We stop the browser navigation, give the beacon a moment, then go to the thank-you page. */
      e.preventDefault();
      if (summary) summary.classList.remove('show');
      if (btn) { btn.classList.add('is-loading'); btn.setAttribute('disabled', ''); btn.innerHTML = 'Sending…'; }
      try { w.dataLayer = w.dataLayer || []; w.dataLayer.push({ event: 'quote_form_submit', form_name: form.getAttribute('data-quote-form') }); } catch (err) {}
      var next = form.getAttribute('data-redirect') || '/thank-you/';
      setTimeout(function () { w.location.assign(next); }, 900);
    });
  });

  /* ---------- Year ---------- */
  d.querySelectorAll('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* ---------- Motion (GSAP) ---------- */
  if (reduce || typeof gsap === 'undefined') return;
  if (typeof ScrollTrigger !== 'undefined') gsap.registerPlugin(ScrollTrigger);

  /* Hero entrance: eyebrow, headline lines, lead, CTAs, then the form card */
  var hero = d.querySelector('.hero');
  if (hero) {
    var tl = gsap.timeline({ defaults: { ease: 'expo.out' } });
    var h1 = hero.querySelector('h1');
    if (h1 && !h1.dataset.split) {
      var words = h1.innerHTML.split(/(\s+)/);
      h1.innerHTML = words.map(function (t) { return /^\s+$/.test(t) || !t ? t : '<span class="w" style="display:inline-block">' + t + '</span>'; }).join('');
      h1.dataset.split = '1';
    }
    var bg = hero.querySelector('.hero__bg img');
    if (bg) tl.fromTo(bg, { scale: 1.12 }, { scale: 1.04, duration: 2.2, ease: 'power2.out' }, 0);
    tl.from(hero.querySelectorAll('.breadcrumbs, .eyebrow'), { y: 16, opacity: 0, duration: .5 }, .1)
      .from(hero.querySelectorAll('h1 .w'), { y: 40, opacity: 0, duration: .7, stagger: .05 }, .2)
      .from(hero.querySelectorAll('.gold-rule'), { scaleX: 0, transformOrigin: 'left center', duration: .6 }, '-=.4')
      .from(hero.querySelectorAll('.lead, .hero__cta, .trust-strip li'), { y: 24, opacity: 0, duration: .55, stagger: .07 }, '-=.5')
      .from(hero.querySelectorAll('.quote-card, .hero__aside'), { y: 30, opacity: 0, duration: .7 }, '-=.6');
  }

  /* Scroll reveals */
  gsap.utils.toArray('[data-reveal]').forEach(function (el) {
    gsap.from(el, { opacity: 0, y: 24, duration: .55, ease: 'power2.out', scrollTrigger: { trigger: el, start: 'top 88%', once: true } });
  });
  gsap.utils.toArray('[data-reveal-stagger]').forEach(function (el) {
    var kids = Array.prototype.slice.call(el.children, 0, 12);
    gsap.from(kids, { opacity: 0, y: 20, scale: .96, duration: .45, ease: 'back.out(1.4)', stagger: { each: .07, grid: 'auto', from: 'start' }, scrollTrigger: { trigger: el, start: 'top 85%', once: true } });
  });

  /* Count-up stats */
  gsap.utils.toArray('[data-count]').forEach(function (el) {
    var target = parseFloat(el.getAttribute('data-count'));
    var dec = (el.getAttribute('data-decimals') | 0);
    var suffix = el.getAttribute('data-suffix') || '';
    var obj = { v: 0 };
    gsap.to(obj, { v: target, duration: 1.4, ease: 'power1.out', scrollTrigger: { trigger: el, start: 'top 90%', once: true },
      onUpdate: function () { el.textContent = obj.v.toFixed(dec) + suffix; } });
  });

  /* Gentle parallax on framed images */
  gsap.utils.toArray('.img-frame img, .ba').forEach(function (img) {
    gsap.fromTo(img, { y: -12 }, { y: 12, ease: 'none', scrollTrigger: { trigger: img, start: 'top bottom', end: 'bottom top', scrub: 1 } });
  });
})();
