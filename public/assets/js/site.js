/* Green Estates Gardening — site behaviour */
(function () {
  'use strict';
  var d = document, w = window;
  d.documentElement.classList.add('js');
  var reduce = w.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- Header ---------- */
  var header = d.querySelector('.site-header');
  function onScroll() { if (header) header.classList.toggle('scrolled', w.scrollY > 40); }
  w.addEventListener('scroll', onScroll, { passive: true }); w.requestAnimationFrame(onScroll);

  /* Mega-dropdowns (Services, Areas): hover on pointer devices, click everywhere */
  var dds = Array.prototype.slice.call(d.querySelectorAll('.nav-dropdown'));
  var hoverCapable = w.matchMedia('(hover: hover)').matches;
  var closeAll = function (except) { dds.forEach(function (x) { if (x !== except) { x.classList.remove('open'); x.querySelector('.nav-trigger').setAttribute('aria-expanded', 'false'); } }); };
  dds.forEach(function (dd) {
    var trigger = dd.querySelector('.nav-trigger');
    var openDd = function () { closeAll(dd); dd.classList.add('open'); trigger.setAttribute('aria-expanded', 'true'); };
    var closeDd = function () { dd.classList.remove('open'); trigger.setAttribute('aria-expanded', 'false'); };
    if (hoverCapable) { dd.addEventListener('mouseenter', openDd); dd.addEventListener('mouseleave', closeDd); }
    trigger.addEventListener('click', function (e) { e.preventDefault(); dd.classList.contains('open') ? closeDd() : openDd(); });
    dd.addEventListener('focusout', function (e) { if (!dd.contains(e.relatedTarget)) closeDd(); });
  });
  if (dds.length) {
    d.addEventListener('click', function (e) { if (!dds.some(function (x) { return x.contains(e.target); })) closeAll(); });
    d.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeAll(); });
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
    mnav.querySelectorAll('.m-acc').forEach(function (acc) {
      var sub = d.getElementById(acc.getAttribute('aria-controls'));
      if (!sub) return;
      acc.addEventListener('click', function () {
        var open = acc.getAttribute('aria-expanded') === 'true';
        acc.setAttribute('aria-expanded', String(!open));
        sub.classList.toggle('open', !open);
      });
    });
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

  /* ---------- Quote pop-up (header + hero CTAs) ---------- */
  var modal = d.getElementById('quote-modal');
  if (modal) {
    var panel = modal.querySelector('.modal__panel');
    var lastFocus = null;
    var focusables = function () {
      return Array.prototype.filter.call(modal.querySelectorAll('a[href],button:not([disabled]),input:not([type=hidden]),select,textarea,[tabindex]:not([tabindex="-1"])'), function (el) { return el.offsetParent !== null; });
    };
    var openModal = function (trigger) {
      lastFocus = trigger || d.activeElement;
      if (burger && d.body.classList.contains('nav-open')) burger.click();
      modal.hidden = false;
      d.body.classList.add('modal-open');
      /* next frame so the transition runs from the hidden state */
      requestAnimationFrame(function () { requestAnimationFrame(function () { modal.classList.add('is-open'); }); });
      var first = modal.querySelector('input:not([type=hidden])');
      setTimeout(function () { (first || panel).focus({ preventScroll: true }); }, reduce ? 0 : 200);
      try { w.dataLayer = w.dataLayer || []; w.dataLayer.push({ event: 'quote_popup_open', source: trigger && trigger.closest('header') ? 'header' : 'hero' }); } catch (err) {}
    };
    var closeModal = function () {
      if (modal.hidden) return;
      modal.classList.remove('is-open');
      d.body.classList.remove('modal-open');
      var done = function () { modal.hidden = true; if (lastFocus && lastFocus.focus) lastFocus.focus({ preventScroll: true }); };
      if (reduce) done(); else setTimeout(done, 260);
    };
    d.addEventListener('click', function (e) {
      var opener = e.target.closest ? e.target.closest('[data-open-quote]') : null;
      if (opener) { e.preventDefault(); openModal(opener); return; }
      if (e.target.closest && e.target.closest('[data-close-quote]')) { e.preventDefault(); closeModal(); }
    });
    d.addEventListener('keydown', function (e) {
      if (modal.hidden) return;
      if (e.key === 'Escape') { e.preventDefault(); closeModal(); return; }
      if (e.key === 'Tab') {
        var f = focusables(); if (!f.length) return;
        var first = f[0], last = f[f.length - 1];
        if (e.shiftKey && (d.activeElement === first || d.activeElement === panel)) { e.preventDefault(); last.focus(); }
        else if (!e.shiftKey && d.activeElement === last) { e.preventDefault(); first.focus(); }
      }
    });
    /* Deep link: /contact/#quote from a page without an inline form still works; ?quote=1 opens the pop-up */
    if (/[?&]quote=1/.test(w.location.search)) openModal(null);
  }

  /* ---------- Quote forms ----------
     There is no form endpoint: the LeadConnector tracking script (loaded in <head>) reads the
     fields when the form is submitted and pushes the lead into the CRM. Our job is to validate,
     let the submit event fire so that script can see it, stop the browser's own navigation, and
     then send the visitor to the thank-you page. Every hook below is registered in the capture
     phase on window so it runs before anything else on the page and cannot be swallowed. */
  var quoteForms = Array.prototype.slice.call(d.querySelectorAll('form[data-quote-form]'));
  if (quoteForms.length) {
    var msgs = {
      full_name: 'Please tell us your name.',
      email: 'Please enter a valid email address.',
      phone: 'Please enter a phone number we can call you on.',
      property_address: 'Please enter the property address or suburb.',
      property_type: 'Please choose the property type.',
      service_needed: 'Please choose the service you need.'
    };
    var fieldWrap = function (el) { return el.closest ? el.closest('.field') : null; };
    var showError = function (el) {
      var fw = fieldWrap(el); if (!fw) return;
      fw.classList.add('has-error');
      var err = fw.querySelector('.error'); if (err) err.textContent = msgs[el.name] || 'Please complete this field.';
      el.setAttribute('aria-invalid', 'true');
    };
    var clearError = function (el) {
      var fw = fieldWrap(el); if (!fw) return;
      fw.classList.remove('has-error'); el.removeAttribute('aria-invalid');
    };
    var validate = function (form) {
      var invalid = [];
      Array.prototype.forEach.call(form.querySelectorAll('input,select,textarea'), function (el) {
        var ok = true;
        try { ok = el.checkValidity(); } catch (err) { ok = true; }
        if (!ok) { invalid.push(el); showError(el); } else { clearError(el); }
      });
      var summary = form.querySelector('.form-summary');
      if (invalid.length) {
        if (summary) {
          summary.innerHTML = '<strong>Please check the highlighted fields.</strong> ' + invalid.map(function (el) {
            var lab = form.querySelector('label[for="' + el.id + '"]');
            return '<a href="#' + el.id + '">' + (lab ? lab.textContent.replace('(optional)', '').trim() : el.name) + '</a>';
          }).join(' · ');
          summary.classList.add('show');
          summary.setAttribute('tabindex', '-1');
        }
      } else if (summary) {
        summary.classList.remove('show');
      }
      return invalid;
    };
    var target = function (form) { return form.getAttribute('data-redirect') || '/thank-you/'; };
    var sendAndRedirect = function (form) {
      if (form.__geSent) return;
      form.__geSent = true;
      var next = target(form);
      var btn = form.querySelector('button[type=submit]');
      try {
        if (btn) { btn.classList.add('is-loading'); btn.setAttribute('aria-busy', 'true'); btn.innerHTML = 'Sending…'; }
        w.dataLayer = w.dataLayer || [];
        w.dataLayer.push({ event: 'quote_form_submit', form_name: form.getAttribute('data-quote-form') });
      } catch (err) { /* cosmetic only */ }
      /* Give the tracking beacon a moment, then leave. Two timers so a blocked assign() still redirects. */
      setTimeout(function () { try { w.location.assign(next); } catch (err) { w.location.href = next; } }, 700);
      setTimeout(function () { w.location.href = next; }, 2500);
    };
    var findForm = function (node) {
      while (node && node !== d) { if (node.matches && node.matches('form[data-quote-form]')) return node; node = node.parentNode; }
      return null;
    };
    quoteForms.forEach(function (form) {
      form.setAttribute('novalidate', '');
      Array.prototype.forEach.call(form.querySelectorAll('input,select,textarea'), function (el) {
        var maybeClear = function () { try { if (el.checkValidity()) clearError(el); } catch (err) {} };
        el.addEventListener('input', maybeClear);
        el.addEventListener('change', maybeClear);
      });
    });
    /* 1. Submit (button click or Enter key). Capture phase on window: first listener to run. */
    w.addEventListener('submit', function (e) {
      var form = findForm(e.target); if (!form) return;
      try {
        var invalid = validate(form);
        if (invalid.length) {
          e.preventDefault(); e.stopImmediatePropagation();
          var summary = form.querySelector('.form-summary'); if (summary) summary.focus();
          invalid[0].focus();
          return;
        }
        e.preventDefault(); /* no native navigation; the event keeps bubbling for the tracking script */
        sendAndRedirect(form);
      } catch (fatal) { e.preventDefault(); w.location.href = target(form); }
    }, true);
    /* 2. Belt and braces: the submit button click itself. If any other script cancels the submit
          event, this still gets a valid form through to the thank-you page. */
    w.addEventListener('click', function (e) {
      var node = e.target;
      while (node && node !== d && !(node.tagName === 'BUTTON' || node.tagName === 'INPUT')) node = node.parentNode;
      if (!node || node === d || (node.getAttribute('type') || 'submit').toLowerCase() !== 'submit') return;
      var form = node.form || findForm(node); if (!form || !findForm(form)) return;
      try {
        if (validate(form).length) return; /* let the submit handler above show the summary and focus */
        /* Valid: let the click go on to fire submit (so the tracking script sees it) and start the redirect now. */
        setTimeout(function () { if (!form.__geSent) sendAndRedirect(form); }, 50);
      } catch (fatal) { w.location.href = target(form); }
    }, true);
  }

  /* Thank-you page: if a no-JS or third-party submit landed here with fields in the query string, tidy the URL. */
  if (/^\/thank-you\/?$/.test(w.location.pathname) && w.location.search && w.history && w.history.replaceState) {
    try { w.history.replaceState(null, '', w.location.pathname); } catch (err) {}
  }

  /* ---------- Year ---------- */
  d.querySelectorAll('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* ---------- Motion ----------
     No animation library. Content that starts below the fold fades up as it scrolls into view;
     anything already on screen at load is never hidden, so first paint and LCP are not delayed.
     Classes are removed once the reveal finishes so hover transitions behave normally. */
  if (reduce || !('IntersectionObserver' in w)) return;
  var settle = function (el, cls, ms) { setTimeout(function () { el.classList.remove(cls, 'is-in'); }, ms); };
  var play = function (el) {
    el.classList.add('is-in');
    if (el.classList.contains('rv')) settle(el, 'rv', 700);
    if (el.classList.contains('rv-s')) settle(el, 'rv-s', 600 + Math.min(el.children.length, 12) * 70);
    if (el.hasAttribute('data-count')) countUp(el);
  };
  var hide = function (el) {
    if (el.hasAttribute('data-reveal')) el.classList.add('rv');
    if (el.hasAttribute('data-reveal-stagger')) {
      Array.prototype.forEach.call(el.children, function (c, i) { if (i < 12) c.style.setProperty('--i', i); });
      el.classList.add('rv-s');
    }
    if (el.hasAttribute('data-count')) el.textContent = (0).toFixed(el.getAttribute('data-decimals') | 0) + (el.getAttribute('data-suffix') || '');
  };
  var seen = new WeakSet();
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      var el = en.target;
      if (!seen.has(el)) {
        /* first report: on screen at load -> leave it alone; below the fold -> hide it and wait */
        seen.add(el);
        var vh = w.innerHeight;
        if (en.isIntersecting || en.boundingClientRect.top < vh || en.boundingClientRect.height === 0) { io.unobserve(el); return; }
        hide(el); return;
      }
      if (en.isIntersecting) { io.unobserve(el); play(el); }
    });
  }, { rootMargin: '0px 0px -8% 0px' });
  d.querySelectorAll('[data-reveal],[data-reveal-stagger],[data-count]').forEach(function (el) { io.observe(el); });

  /* Count-up stats: the final number is in the HTML; only numbers below the fold are animated */
  function countUp(el) {
    var target = parseFloat(el.getAttribute('data-count')), dec = (el.getAttribute('data-decimals') | 0);
    var suffix = el.getAttribute('data-suffix') || '', t0 = null, dur = 1200;
    var step = function (ts) {
      if (t0 === null) t0 = ts;
      var k = Math.min(1, (ts - t0) / dur), e = 1 - Math.pow(1 - k, 3);
      el.textContent = (target * e).toFixed(dec) + suffix;
      if (k < 1) w.requestAnimationFrame(step);
    };
    w.requestAnimationFrame(step);
  }
})();
