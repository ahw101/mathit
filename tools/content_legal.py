# -*- coding: utf-8 -*-
"""Compliance pages: privacy, terms, contact, 404."""
from shell import CONTACT_EMAIL, SITE_NAME, SITE_URL


def _page_header(crumb, eyebrow, title, standfirst):
    return f"""    <section class="border-b border-line bg-surface">
      <div class="mx-auto max-w-4xl px-4 py-14 sm:px-6 lg:px-8">
        <nav class="mb-5 flex items-center gap-1.5 text-sm text-soft" aria-label="Breadcrumb">
          <a href="index.html" class="rounded px-1 py-0.5 hover:text-accent-text hover:underline">Home</a>
          <span aria-hidden="true" class="text-faint">/</span>
          <span class="font-semibold text-strong" aria-current="page">{crumb}</span>
        </nav>
        <span class="kicker">{eyebrow}</span>
        <h1 class="mt-4 font-display text-4xl font-bold leading-tight sm:text-5xl">{title}</h1>
        <p class="mt-5 text-lg leading-relaxed text-body">{standfirst}</p>
        <p class="mt-4 text-sm text-soft">Last updated: <span data-last-updated>1 October 2026</span></p>
      </div>
    </section>"""


PRIVACY = f"""  <main id="main">
{_page_header("Privacy &amp; cookies", "Legal", "Privacy and cookie notice",
              "What {0} does — and deliberately does not do — with information when you use this website.".format(SITE_NAME))}

    <div class="mx-auto max-w-4xl px-4 py-14 sm:px-6 lg:px-8">
      <article class="article">
        <div class="note">
          <p class="!mt-0 font-semibold text-accent-soft-fg">The short version</p>
          <p class="!mt-2 text-accent-soft-fg">
            We do not ask you to register, we do not ask for your name or your child's name, and we
            do not run our own analytics or tracking cookies. Your worksheet preferences are stored
            in your own browser and never leave your device. Adverts are served by Google AdSense,
            which may set cookies — the detail, and how to turn personalised advertising off, is
            explained below.
          </p>
        </div>

        <h2>1. Who we are</h2>
        <p>
          {SITE_NAME} ("we", "us") operates the website at <strong>{SITE_URL}</strong>, a free
          mathematics practice resource for primary-aged children, their families and their
          teachers. For any question about this notice, write to
          <a href="mailto:{CONTACT_EMAIL}" class="link">{CONTACT_EMAIL}</a>.
        </p>
        <p>
          For the purposes of the UK General Data Protection Regulation (UK GDPR) and the Data
          Protection Act 2018, we are the data controller for the limited information described
          below. Where advertising is served, the advertising provider acts as an independent
          controller for the data it collects.
        </p>

        <h2>2. Information we collect</h2>
        <h3>Information you give us</h3>
        <p>
          The only way to send us information is by using the contact form or emailing us
          directly. The contact form does not transmit anything to a server of ours — it opens
          your own email application with the message pre-filled, so you send it exactly as you
          would send any other email. If you do write to us, we will hold your message and email
          address only for as long as it takes to deal with your enquiry, and no longer than
          twelve months.
        </p>

        <h3>Information stored on your device</h3>
        <p>
          The worksheet generator stores your preferences — year group, difficulty tier, selected
          topics, compact mode, contrast mode, text size and timer settings — in your browser's
          <strong>local storage</strong> under the key <code>mathit:settings</code>. This is not a
          cookie, it is never transmitted to us, and it contains nothing that could identify you
          or a child. You can delete it at any time by clearing site data in your browser
          settings.
        </p>

        <h3>Information collected automatically</h3>
        <p>
          Like virtually every website, our hosting provider records standard server logs
          including IP address, browser type, the page requested and the time of the request.
          These logs are used only to keep the site running and secure, and are retained for a
          short period before deletion. We do not use them to build profiles of visitors.
        </p>

        <h2>3. Advertising and cookies</h2>
        <p>
          This site is free to use and is funded by advertising. Advertising space is clearly
          labelled "Advertisement" and is kept visually separate from the worksheet content so
          that nobody — least of all a child — could mistake an advert for part of a maths
          question.
        </p>
        <ul>
          <li>Third-party vendors, including Google, use cookies to serve adverts based on a user's prior visits to this and other websites.</li>
          <li>Google's use of advertising cookies enables it and its partners to serve adverts to users based on their visit to this site and/or other sites on the internet.</li>
          <li>You may opt out of personalised advertising by visiting <a class="link" href="https://www.google.com/settings/ads" rel="nofollow noopener" target="_blank">Google Ads Settings</a>.</li>
          <li>You can opt out of third-party vendor cookies for personalised advertising at <a class="link" href="https://www.aboutads.info/choices/" rel="nofollow noopener" target="_blank">aboutads.info/choices</a> or, in Europe, at <a class="link" href="https://www.youronlinechoices.com/" rel="nofollow noopener" target="_blank">youronlinechoices.com</a>.</li>
          <li>Where required by law, a consent banner will request your permission before any non-essential cookie is set, and personalised advertising will not run unless you agree.</li>
        </ul>
        <p>
          Full details of how Google handles data when you use our partners' sites are published in
          <a class="link" href="https://policies.google.com/technologies/partner-sites" rel="nofollow noopener" target="_blank">Google's privacy and terms</a>.
        </p>

        <table>
          <caption class="sr-only">Categories of cookie used on this site</caption>
          <thead><tr><th>Category</th><th>Purpose</th><th>Set by</th></tr></thead>
          <tbody>
            <tr><td>Strictly necessary</td><td>None required. The site functions without cookies.</td><td>—</td></tr>
            <tr><td>Preferences (local storage)</td><td>Remembers your worksheet settings on your own device.</td><td>{SITE_NAME}</td></tr>
            <tr><td>Advertising</td><td>Ad delivery, frequency capping, measurement and — with consent — personalisation.</td><td>Google AdSense and its certified partners</td></tr>
          </tbody>
        </table>

        <h2>4. Children's privacy</h2>
        <p>
          {SITE_NAME} is written for children's use but is designed to be chosen and supervised by
          an adult. We do not knowingly collect personal data from anyone, and we do not ask for
          any information that would identify a child — no names, no ages, no schools, no scores
          sent anywhere. Worksheet results exist only in the browser tab and disappear when it is
          closed.
        </p>
        <p>
          Where advertising is shown on pages likely to be viewed by children, it is requested as
          non-personalised, child-directed inventory in line with Google's policies for
          child-directed content. If you believe a child has provided us with personal
          information, please contact us and we will delete it immediately.
        </p>

        <h2>5. Lawful basis for processing</h2>
        <p>
          Where we process any personal data it is on the basis of our <strong>legitimate
          interests</strong> in operating and securing a free educational website, or on the basis
          of your <strong>consent</strong> where you have chosen to contact us or to accept
          personalised advertising. You may withdraw consent at any time.
        </p>

        <h2>6. Your rights</h2>
        <p>Under UK GDPR you have the right to:</p>
        <ul>
          <li>ask what personal data we hold about you and request a copy;</li>
          <li>ask us to correct inaccurate data;</li>
          <li>ask us to erase data we no longer need;</li>
          <li>object to or restrict our processing;</li>
          <li>withdraw consent where processing is based on consent; and</li>
          <li>complain to the Information Commissioner's Office at <a class="link" href="https://ico.org.uk/" rel="nofollow noopener" target="_blank">ico.org.uk</a>.</li>
        </ul>
        <p>
          In practice we hold almost nothing, so most requests can be answered within a few days.
          Write to <a href="mailto:{CONTACT_EMAIL}" class="link">{CONTACT_EMAIL}</a>.
        </p>

        <h2>7. Data sharing and international transfers</h2>
        <p>
          We do not sell, rent or trade information to anyone. Our advertising partner may process
          data outside the United Kingdom; where that happens it is covered by the partner's own
          approved transfer mechanisms, such as the UK extension to the EU–US Data Privacy
          Framework or standard contractual clauses.
        </p>

        <h2>8. Security</h2>
        <p>
          The site is served over HTTPS. Because we do not operate user accounts or store personal
          records, the attack surface is deliberately tiny — there is no database of children's
          data to breach.
        </p>

        <h2>9. Changes to this notice</h2>
        <p>
          We will update this page whenever our practices change, and the "last updated" date at
          the top will change with it. Material changes affecting how data is used will be flagged
          prominently on the home page for at least thirty days.
        </p>

        <h2>10. Contact</h2>
        <p>
          Questions, corrections and data requests: <a href="mailto:{CONTACT_EMAIL}" class="link">{CONTACT_EMAIL}</a>,
          or use the <a href="contact.html" class="link">contact form</a>.
        </p>
      </article>
    </div>
  </main>"""


TERMS = f"""  <main id="main">
{_page_header("Terms of use", "Legal", "Terms of use",
              "The ground rules for using {0}. They are short, and deliberately generous about copying worksheets for teaching.".format(SITE_NAME))}

    <div class="mx-auto max-w-4xl px-4 py-14 sm:px-6 lg:px-8">
      <article class="article">
        <h2>1. Agreement</h2>
        <p>
          By using {SITE_URL} you agree to these terms. If you do not agree with them, please stop
          using the site. These terms are governed by the law of England and Wales, and the courts
          of England and Wales have exclusive jurisdiction over any dispute arising from them.
        </p>

        <h2>2. What the service is</h2>
        <p>
          {SITE_NAME} generates mathematics practice worksheets in your web browser and publishes
          free explanatory guides. It is a supplementary practice tool. It is not a tutoring
          service, not an assessment service, not a substitute for teaching, and it does not
          claim to prepare any individual child for any particular examination outcome.
        </p>

        <h2>3. Permitted use — teachers and families</h2>
        <p>We positively encourage educational use. You may, free of charge and without asking:</p>
        <ul>
          <li>generate unlimited worksheets for yourself, your children or your pupils;</li>
          <li>print and photocopy any worksheet or reference sheet for classroom, tutoring or home use;</li>
          <li>display the site on a whiteboard or shared screen;</li>
          <li>link to any page on the site, including deep links to specific worksheets; and</li>
          <li>include printed worksheets in homework packs, intervention folders and revision booklets.</li>
        </ul>

        <h2>4. What you may not do</h2>
        <ul>
          <li>Republish, mirror or redistribute substantial parts of the site's written guides as your own content, in print or online.</li>
          <li>Sell, license or otherwise commercialise the worksheets or guides, whether in their original form or lightly edited.</li>
          <li>Scrape, crawl or systematically extract content, or run automated processes that place unreasonable load on the site.</li>
          <li>Attempt to interfere with the site's operation, security or availability, or with another user's use of it.</li>
          <li>Remove, obscure or alter any attribution, copyright notice or advertising on pages you redistribute.</li>
          <li>Use the site in any way that is unlawful, fraudulent or harmful.</li>
        </ul>

        <h2>5. Intellectual property</h2>
        <p>
          The written guides, the site design, the Math&nbsp;It! name and logo, and the question
          generation software are our intellectual property and are protected by copyright. The
          mathematics itself is, of course, nobody's property — you are free to set 3/4 × 16 in
          your own materials. The licence granted in section 3 above covers everything a teacher
          or parent realistically needs.
        </p>

        <h2>6. Accuracy and no warranty</h2>
        <p>
          We take considerable care over the correctness of generated questions and model answers,
          and the generator is tested automatically against every question type at every year
          group and difficulty tier. Even so, the site is provided <strong>"as is"</strong> and
          <strong>"as available"</strong>, without warranties of any kind, express or implied,
          including fitness for a particular purpose.
        </p>
        <p>
          If you find a question that is wrong, ambiguous or pitched incorrectly for its year
          group, please tell us — <a href="mailto:{CONTACT_EMAIL}" class="link">{CONTACT_EMAIL}</a>
          — and include the sheet number shown beside the worksheet title so we can reproduce the
          exact sheet.
        </p>

        <h2>7. Availability</h2>
        <p>
          We aim to keep the site available at all times but do not guarantee it. We may change,
          suspend or withdraw any part of the service, including individual features, at any time
          and without notice. Worksheet links are intended to remain stable, but we cannot
          guarantee that a link saved today will produce an identical sheet indefinitely if the
          underlying question library changes.
        </p>

        <h2>8. Advertising</h2>
        <p>
          The site carries third-party advertising, which is what keeps it free. Adverts are
          labelled and kept separate from worksheet content. We do not control, endorse or accept
          responsibility for the products, services or claims in third-party adverts, nor for the
          content of any site they link to. Concerns about a specific advert can be raised with us
          and we will pass them on to the advertising provider.
        </p>

        <h2>9. External links</h2>
        <p>
          Where we link to other websites it is because we think they are useful. We have no
          control over their content and accept no responsibility for it.
        </p>

        <h2>10. Limitation of liability</h2>
        <p>
          To the fullest extent permitted by law, we exclude liability for any indirect or
          consequential loss, loss of data, or loss arising from reliance on any content on the
          site. Nothing in these terms limits liability for death or personal injury caused by
          negligence, for fraud, or for anything else that cannot lawfully be excluded. Your
          statutory rights as a consumer are unaffected.
        </p>

        <h2>11. Changes to these terms</h2>
        <p>
          We may revise these terms from time to time. The version published on this page is the
          one that applies to your use of the site, and the "last updated" date shows when it last
          changed.
        </p>

        <h2>12. Contact</h2>
        <p>
          Questions about these terms: <a href="mailto:{CONTACT_EMAIL}" class="link">{CONTACT_EMAIL}</a>.
        </p>
      </article>
    </div>
  </main>"""


CONTACT = f"""  <main id="main">
{_page_header("Contact", "Get in touch", "Contact Math It!",
              "Spotted a wrong answer, want a topic added, or writing from a school? We read everything.")}

    <div class="mx-auto max-w-6xl px-4 py-14 sm:px-6 lg:px-8">
      <div class="grid gap-10 lg:grid-cols-12">

        <div class="lg:col-span-7">
          <div class="card card-pad">
            <h2 class="font-display text-2xl font-bold">Send us a message</h2>
            <p class="mt-2 text-sm leading-relaxed text-soft">
              This form opens your own email application with everything filled in — nothing is
              submitted to a server, and no data is stored on our side. If your email client does
              not open, write to
              <a href="mailto:{CONTACT_EMAIL}" class="link">{CONTACT_EMAIL}</a> instead.
            </p>

            <form data-contact-form data-mailto="{CONTACT_EMAIL}" class="mt-6 grid gap-4" novalidate>
              <div class="grid gap-4 sm:grid-cols-2">
                <div>
                  <label for="cf-name" class="mb-1.5 block text-sm font-medium text-body">Your name <span class="text-bad">*</span></label>
                  <input id="cf-name" name="name" type="text" autocomplete="name" required class="field" placeholder="Alex Morgan">
                </div>
                <div>
                  <label for="cf-email" class="mb-1.5 block text-sm font-medium text-body">Email address <span class="text-bad">*</span></label>
                  <input id="cf-email" name="email" type="email" autocomplete="email" required class="field" placeholder="you@school.sch.uk">
                </div>
              </div>
              <div>
                <label for="cf-subject" class="mb-1.5 block text-sm font-medium text-body">What is it about?</label>
                <select id="cf-subject" name="subject" class="field">
                  <option>A question looks wrong</option>
                  <option>Suggest a new topic or question type</option>
                  <option>Accessibility feedback</option>
                  <option>School or MAT enquiry</option>
                  <option>Advertising enquiry</option>
                  <option>Privacy or data request</option>
                  <option>Something else</option>
                </select>
              </div>
              <div>
                <label for="cf-message" class="mb-1.5 block text-sm font-medium text-body">Message <span class="text-bad">*</span></label>
                <textarea id="cf-message" name="message" rows="7" required class="field" placeholder="If you are reporting a question, please include the sheet number shown beside the worksheet title — it lets us recreate the exact sheet you saw."></textarea>
              </div>
              <div class="flex flex-wrap items-center gap-3">
                <button type="submit" class="btn btn-primary btn-lg">Open email draft</button>
                <a href="mailto:{CONTACT_EMAIL}" class="text-sm font-medium text-soft underline decoration-line-strong underline-offset-2 hover:text-accent-text">or email us directly</a>
              </div>
              <p data-contact-status role="status" aria-live="polite" class="text-sm"></p>
            </form>
          </div>
        </div>

        <div class="lg:col-span-5">
          <div class="card card-pad">
            <h2 class="font-display text-xl font-bold">Straight answers</h2>
            <dl class="mt-5 space-y-5">
              <div>
                <dt class="font-semibold text-strong">Found a wrong answer?</dt>
                <dd class="mt-1 text-sm leading-relaxed text-soft">
                  Please include the sheet number (the <span class="font-mono">#123456</span> beside
                  the worksheet title) and the question number. Every sheet is reproducible from
                  that number, so we can see exactly what you saw.
                </dd>
              </div>
              <div>
                <dt class="font-semibold text-strong">Want a topic added?</dt>
                <dd class="mt-1 text-sm leading-relaxed text-soft">
                  Tell us the year group and the curriculum objective. New question types are the
                  most common change we make, and they are usually live within a fortnight.
                </dd>
              </div>
              <div>
                <dt class="font-semibold text-strong">Schools and trusts</dt>
                <dd class="mt-1 text-sm leading-relaxed text-soft">
                  Everything here is free for whole-school use and may be copied for pupils without
                  asking. If you need something specific — a bespoke topic mix, or an ad-free
                  internal copy — write and ask.
                </dd>
              </div>
              <div>
                <dt class="font-semibold text-strong">Response times</dt>
                <dd class="mt-1 text-sm leading-relaxed text-soft">
                  Math&nbsp;It! is run by a very small team. We aim to reply within three working
                  days; reports of incorrect questions jump the queue.
                </dd>
              </div>
            </dl>
          </div>

          <div class="card card-pad mt-6">
            <h2 class="font-display text-xl font-bold">Before you write</h2>
            <p class="mt-2 text-sm leading-relaxed text-soft">
              The <a href="index.html#faq" class="link">frequently asked questions</a> cover answer
              formats, printing, accessibility settings and how the generator works — they answer
              most messages faster than we can.
            </p>
            <ul class="mt-4 space-y-2 text-sm">
              <li><a href="index.html#faq" class="link">Frequently asked questions</a></li>
              <li><a href="resources.html" class="link">Topic guides and printables</a></li>
              <li><a href="privacy.html" class="link">Privacy and cookie notice</a></li>
              <li><a href="terms.html" class="link">Terms of use</a></li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </main>"""


NOT_FOUND = """  <main id="main" class="mx-auto flex min-h-[60vh] max-w-3xl flex-col items-center justify-center px-4 py-24 text-center sm:px-6">
    <span class="font-display text-7xl font-bold text-accent/25">404</span>
    <h1 class="mt-4 font-display text-4xl font-bold">That page has gone missing</h1>
    <p class="mt-4 max-w-xl text-lg leading-relaxed text-body">
      The link may be out of date, or the address might have a typo in it. Everything on Math It!
      is reachable from the links below.
    </p>
    <div class="mt-8 flex flex-wrap justify-center gap-3">
      <a href="index.html" class="btn btn-primary btn-lg">Back to the home page</a>
      <a href="practice.html" class="btn btn-ghost btn-lg">Open the worksheet generator</a>
    </div>
    <div class="mt-12 grid w-full gap-3 sm:grid-cols-3">
      <a href="practice.html?year=4&amp;level=medium" class="rounded-xl border border-line bg-surface p-4 text-left shadow-sm hover:border-accent-line"><span class="font-display font-bold">Year 4 worksheets</span><span class="mt-1 block text-sm text-soft">Tables, short division, decimals</span></a>
      <a href="practice.html?year=6&amp;level=hard" class="rounded-xl border border-line bg-surface p-4 text-left shadow-sm hover:border-accent-line"><span class="font-display font-bold">Year 6 greater depth</span><span class="mt-1 block text-sm text-soft">BIDMAS, ratio, algebra</span></a>
      <a href="resources.html" class="rounded-xl border border-line bg-surface p-4 text-left shadow-sm hover:border-accent-line"><span class="font-display font-bold">Topic guides</span><span class="mt-1 block text-sm text-soft">Methods explained, printables</span></a>
    </div>
  </main>"""
