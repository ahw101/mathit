/* =====================================================================
   MATH IT!  —  ADVERTISING CONFIGURATION
   =====================================================================

   ▸▸▸ THIS IS THE ONLY FILE YOU NEED TO EDIT TO GO LIVE WITH ADSENSE ◂◂◂

   Until you fill it in, every ad position on the site renders a neutral,
   dashed "Advertisement" placeholder — no network requests are made and
   nothing is tracked.

   ---------------------------------------------------------------------
   HOW TO ACTIVATE
   ---------------------------------------------------------------------
   1. Get approved at https://adsense.google.com and create ad units.
   2. Set  enabled: true
   3. Paste your publisher ID into  publisherId  (looks like
      'ca-pub-1234567890123456' — find it under Account → Settings).
   4. Paste each ad unit's numeric slot ID into the matching entry of
      `slots` below. Leave an entry as '' to keep that position as a
      placeholder.
   5. Edit /ads.txt in the site root with the same publisher ID.

   That's it — the loader script, the <ins> tags and the push() calls are
   all handled for you by the small runtime at the bottom of this file.

   ---------------------------------------------------------------------
   PREFER TO PASTE GOOGLE'S RAW SNIPPET INSTEAD?
   ---------------------------------------------------------------------
   Drop it into `customHtml` for any slot, e.g.

       slots: {
         'practice-sidebar-top': {
           customHtml: '<ins class="adsbygoogle" style="display:block" ' +
                       'data-ad-client="ca-pub-XXXX" data-ad-slot="1234567890" ' +
                       'data-ad-format="auto" data-full-width-responsive="true"></ins>'
         }
       }

   The runtime will inject it verbatim and call adsbygoogle.push({}).
   ===================================================================== */
(function (global) {
  'use strict';

  const AdsConfig = {

    /** Master switch. Keep false while placeholders are fine. */
    enabled: false,

    /** Your AdSense publisher ID, e.g. 'ca-pub-1234567890123456'. */
    publisherId: 'ca-pub-9904590475432919',

    /** Inject the adsbygoogle.js loader automatically. */
    loadScript: false,

    /** Set true if you only use AdSense "Auto ads" (no manual units). */
    autoAdsOnly: false,

    /**
     * Adds <meta name="google-adsense-account" content="ca-pub-…"> to the
     * <head>, which is one of the ways Google verifies site ownership.
     * Harmless to leave on once publisherId is set.
     */
    verificationMeta: true,

    /**
     * Named positions used throughout the site. The key matches the
     * `data-ad-slot-name` attribute in the HTML.
     *
     * Value may be:
     *   ''                       → placeholder only
     *   '1234567890'             → an AdSense ad-unit slot ID
     *   { slot:'123', format:'auto', fullWidth:true }
     *   { customHtml:'<ins …></ins>' }
     */
    slots: {
      'home-leaderboard':         '',   // below the hero, 970×90 / responsive
      'home-infeed':              '',   // between content blocks on the home page
      'practice-sidebar-top':     '',   // 300×250 beside the worksheet
      'practice-sidebar-bottom':  '',   // 300×600 skyscraper beside the worksheet
      'practice-footer':          '',   // responsive unit under the worksheet
      'resources-inarticle':      '',   // in-article unit on the resource hub
      'resources-sidebar':        '',   // 300×250 in the resources sidebar
      'generic':                  '',   // fallback for any unnamed position
    },
  };

  /* ===================================================================
     Runtime — you should not need to change anything below this line.
     =================================================================== */

  let scriptInjected = false;

  function injectLoader() {
    if (scriptInjected || !AdsConfig.loadScript || !AdsConfig.publisherId) return;
    if (document.querySelector('script[data-mathit-ads]')) { scriptInjected = true; return; }
    const s = document.createElement('script');
    s.async = true;
    s.crossOrigin = 'anonymous';
    s.src = 'https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=' +
      encodeURIComponent(AdsConfig.publisherId);
    s.setAttribute('data-mathit-ads', '');
    document.head.appendChild(s);
    scriptInjected = true;
  }

  function injectVerificationMeta() {
    if (!AdsConfig.verificationMeta || !AdsConfig.publisherId) return;
    if (document.querySelector('meta[name="google-adsense-account"]')) return;
    const m = document.createElement('meta');
    m.name = 'google-adsense-account';
    m.content = AdsConfig.publisherId;
    document.head.appendChild(m);
  }

  function placeholder(wrap) {
    const size = wrap.getAttribute('data-ad-size') || '';
    const shape = wrap.getAttribute('data-ad-shape') || '';
    const cls = shape === 'leaderboard' ? 'ad-slot ad-slot--leaderboard'
      : shape === 'tall' ? 'ad-slot ad-slot--tall'
        : 'ad-slot';
    wrap.innerHTML =
      '<div class="' + cls + '" role="complementary" aria-label="Advertisement placeholder">' +
        '<span class="ad-label">Advertisement</span>' +
        (size ? '<span class="mt-1 text-xs text-ink-400">Reserved ' + size + ' unit</span>' : '') +
        '<span class="mt-2 text-[0.65rem] text-ink-300">Ads keep Math It! free for every classroom</span>' +
      '</div>';
  }

  function renderUnit(wrap, def) {
    const shape = wrap.getAttribute('data-ad-shape') || '';
    const minH = shape === 'leaderboard' ? '90px' : shape === 'tall' ? '600px' : '250px';

    if (def && def.customHtml) {
      wrap.innerHTML = def.customHtml;
    } else {
      const slotId = typeof def === 'string' ? def : def.slot;
      const format = (def && def.format) || 'auto';
      const fullWidth = (def && def.fullWidth === false) ? 'false' : 'true';
      wrap.innerHTML =
        '<ins class="adsbygoogle" style="display:block;min-height:' + minH + '"' +
        ' data-ad-client="' + AdsConfig.publisherId + '"' +
        ' data-ad-slot="' + slotId + '"' +
        ' data-ad-format="' + format + '"' +
        ' data-full-width-responsive="' + fullWidth + '"></ins>';
    }
    try {
      (global.adsbygoogle = global.adsbygoogle || []).push({});
    } catch (e) { /* blocked or offline — the reserved space simply stays empty */ }
  }

  function hydrate(root) {
    const wraps = (root || document).querySelectorAll('[data-ad-slot-name]');
    if (!wraps.length) return;

    const live = AdsConfig.enabled && !!AdsConfig.publisherId;
    if (live) { injectVerificationMeta(); injectLoader(); }

    wraps.forEach(function (wrap) {
      const name = wrap.getAttribute('data-ad-slot-name');
      const def = AdsConfig.slots[name] || AdsConfig.slots.generic;
      const hasUnit = def && (typeof def === 'string' ? def.length : (def.slot || def.customHtml));
      if (live && AdsConfig.autoAdsOnly) { wrap.innerHTML = ''; return; }
      if (live && hasUnit) renderUnit(wrap, def);
      else placeholder(wrap);
    });
  }

  global.MathIt = global.MathIt || {};
  global.MathIt.AdsConfig = AdsConfig;
  global.MathIt.Ads = { hydrate: hydrate };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () { hydrate(); });
  } else {
    hydrate();
  }
})(window);
