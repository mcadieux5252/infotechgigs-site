import html, os
BRANDS = {
 'infotechgigs': dict(
  name='InfoTechGigs', domain='infotechgigs.ai', accent='#1f8a3e', hover='#1a7a36', tint='#eef8f1', deep='#0f3d1d', bright='#6fe39a',
  field='IT and technology', people='IT professionals',
  headline='The right tech role, texted to you.',
  sub='A private text alert service for IT professionals. Tell us your stack, certifications and what you want next. We text you only the roles that fit.',
  match_title='Matched to how you actually work',
  match=[('Your stack','Languages, cloud platforms, tools and frameworks you use every day.'),
         ('Your credentials','AWS, Azure, CISSP, PMP, CCNA and the certifications employers ask for.'),
         ('Your next move','Remote or on site, contract or full time, IC or leadership, and the pay you want.')],
  sample=('Senior Cloud Engineer (AWS)','Remote, US','$165k to $190k'),
  sample_co='A healthcare SaaS company',
  chips=['Cloud & DevOps','Cybersecurity','Data & Analytics','Software Engineering','IT Infrastructure','Product & Project'],
 ),
 'financegigs': dict(
  name='FinanceGigs', domain='financegigs.ai', accent='#c8102e', hover='#b00e28', tint='#fdf0f2', deep='#4a0712', bright='#ff8a9b',
  field='finance and accounting', people='finance and accounting professionals',
  headline='The right finance role, texted to you.',
  sub='A private text alert service for finance and accounting professionals. Tell us your specialty, credentials and what you want next. We text you only the roles that fit.',
  match_title='Matched to your expertise',
  match=[('Your specialty','FP&A, controllership, audit, tax, treasury and corporate finance.'),
         ('Your credentials','CPA, CFA, CMA and the systems you know, like NetSuite, SAP and Workday.'),
         ('Your next move','Remote or on site, interim or permanent, manager or CFO track, and the pay you want.')],
  sample=('FP&A Manager','Chicago, IL (hybrid)','$135k to $155k'),
  sample_co='A private equity backed manufacturer',
  chips=['FP&A','Accounting & Controllership','Audit','Tax','Treasury','CFO & Leadership'],
 ),
}
CHECK='<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 13l4 4L19 7"/></svg>'

def page(b):
    e=html.escape
    match=''.join(f'<div class="card"><div class="num">0{i+1}</div><h3>{e(t)}</h3><p>{e(d)}</p></div>' for i,(t,d) in enumerate(b['match']))
    chips=''.join(f'<span class="chip">{e(c)}</span>' for c in b['chips'])
    t,loc,pay=b['sample']
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{b["name"]} · Private job alerts for {e(b["people"])}</title>
<meta name="description" content="{e(b["sub"])}">
<style>
  :root {{ --accent:{b["accent"]}; --accent-hover:{b["hover"]}; --tint:{b["tint"]}; --deep:{b["deep"]}; --bright:{b["bright"]}; --ink:#1d1d1f; --muted:#6e6e73; --soft:#f5f5f7; --line:rgba(0,0,0,0.08); }}
  *,*::before,*::after {{ box-sizing:border-box; }}
  body {{ margin:0; font-family:-apple-system,BlinkMacSystemFont,'SF Pro Text','Inter','Helvetica Neue',Arial,sans-serif; color:var(--ink); background:#fff; -webkit-font-smoothing:antialiased; }}
  a {{ color:inherit; text-decoration:none; }}
  h1,h2,h3,p {{ margin:0; }}
  .wrap {{ max-width:1120px; margin:0 auto; }}
  .btn {{ display:inline-block; border:none; cursor:pointer; font-family:inherit; border-radius:980px; font-weight:600; font-size:17px; padding:14px 28px; background:var(--accent); color:#fff; transition:background .2s; }}
  .btn:hover {{ background:var(--accent-hover); }}
  .nav {{ position:sticky; top:0; z-index:20; height:56px; display:flex; align-items:center; justify-content:space-between; padding:0 32px; background:rgba(255,255,255,.88); backdrop-filter:saturate(180%) blur(20px); -webkit-backdrop-filter:saturate(180%) blur(20px); border-bottom:1px solid var(--line); }}
  .logo {{ display:flex; align-items:center; gap:10px; font-size:17px; font-weight:700; letter-spacing:-.01em; }}
  .mark {{ width:28px; height:28px; border-radius:8px; background:var(--accent); color:#fff; display:flex; align-items:center; justify-content:center; font-size:13px; font-weight:800; }}
  .logo .ai {{ color:var(--accent); }}
  .nav-right {{ display:flex; gap:24px; align-items:center; font-size:14px; }}
  .nav-cta {{ background:var(--accent); color:#fff; padding:8px 18px; border-radius:980px; font-weight:600; }}

  .hero {{ background:linear-gradient(180deg,var(--tint) 0%,#fff 100%); padding:88px 32px 96px; }}
  .hero-grid {{ display:grid; grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr); gap:64px; align-items:center; }}
  .pill {{ display:inline-flex; gap:8px; align-items:center; font-size:13px; font-weight:600; color:var(--accent); background:#fff; border:1px solid var(--line); padding:6px 14px; border-radius:980px; margin-bottom:24px; }}
  .dot {{ width:8px; height:8px; border-radius:50%; background:var(--accent); }}
  .hero h1 {{ font-size:64px; line-height:1.04; font-weight:700; letter-spacing:-.035em; margin-bottom:22px; }}
  .hero h1 em {{ font-style:normal; color:var(--accent); }}
  .hero-sub {{ font-size:21px; line-height:1.5; color:var(--muted); margin-bottom:32px; max-width:560px; }}
  .hero-note {{ font-size:14px; color:var(--muted); margin-top:14px; }}
  .chips {{ display:flex; flex-wrap:wrap; gap:8px; margin-top:36px; }}
  .chip {{ font-size:13px; font-weight:500; padding:7px 14px; border-radius:980px; background:#fff; border:1px solid var(--line); }}

  .phone {{ width:320px; margin:0 auto; background:#1d1d1f; border-radius:48px; padding:12px; box-shadow:0 40px 80px rgba(0,0,0,.18); }}
  .screen {{ background:#fff; border-radius:38px; padding:22px 16px 26px; display:flex; flex-direction:column; gap:10px; }}
  .screen-head {{ text-align:center; font-size:12px; color:var(--muted); margin-bottom:6px; }}
  .screen-head strong {{ display:block; font-size:14px; color:var(--ink); }}
  .bubble {{ max-width:85%; font-size:14px; line-height:1.4; padding:11px 14px; }}
  .in {{ align-self:flex-start; background:#e9e9eb; border-radius:18px 18px 18px 4px; }}
  .out {{ align-self:flex-end; background:var(--accent); color:#fff; border-radius:18px 18px 4px 18px; }}

  .section {{ padding:112px 32px; }}
  .title {{ font-size:44px; font-weight:700; letter-spacing:-.025em; text-align:center; margin-bottom:14px; }}
  .lead {{ font-size:20px; line-height:1.5; color:var(--muted); text-align:center; max-width:640px; margin:0 auto 56px; }}
  .cards {{ display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:20px; }}
  .card {{ background:var(--soft); border-radius:22px; padding:36px 30px; border-top:4px solid var(--accent); }}
  .num {{ font-size:14px; font-weight:700; color:var(--accent); margin-bottom:18px; }}
  .card h3 {{ font-size:22px; font-weight:600; margin-bottom:10px; }}
  .card p {{ font-size:17px; line-height:1.5; color:var(--muted); }}

  .band {{ background:var(--deep); color:#fff; padding:104px 32px; }}
  .band-grid {{ display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:40px; }}
  .band h2 {{ font-size:40px; font-weight:700; letter-spacing:-.02em; margin-bottom:56px; max-width:720px; }}
  .band h3 {{ font-size:19px; font-weight:600; margin-bottom:8px; color:var(--bright); }}
  .band p {{ font-size:16px; line-height:1.55; color:rgba(255,255,255,.72); }}

  .join {{ background:var(--soft); padding:112px 32px; }}
  .join-grid {{ display:grid; grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr); gap:64px; align-items:start; }}
  .join h2 {{ font-size:44px; font-weight:700; letter-spacing:-.025em; margin-bottom:16px; }}
  .join .body {{ font-size:19px; line-height:1.55; color:var(--muted); margin-bottom:28px; }}
  .checks {{ list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:14px; }}
  .checks li {{ display:flex; gap:12px; font-size:17px; line-height:1.4; }}
  .checks svg {{ color:var(--accent); flex-shrink:0; margin-top:1px; }}
  .form {{ background:#fff; border-radius:26px; padding:36px; box-shadow:0 20px 50px rgba(0,0,0,.06); }}
  .form h3 {{ font-size:22px; font-weight:700; margin-bottom:6px; }}
  .form .fine {{ font-size:14px; color:var(--muted); margin-bottom:24px; }}
  .row2 {{ display:grid; grid-template-columns:1fr 1fr; gap:12px; }}
  label.f {{ display:block; font-size:13px; font-weight:600; margin-bottom:6px; }}
  input[type=text],input[type=email],input[type=tel] {{ width:100%; font:inherit; font-size:16px; padding:12px 14px; border:1px solid #d2d2d7; border-radius:12px; margin-bottom:14px; }}
  input:focus {{ outline:2px solid var(--accent); outline-offset:1px; border-color:transparent; }}
  .consent {{ display:flex; gap:12px; align-items:flex-start; background:var(--tint); border-radius:14px; padding:16px; margin:4px 0 20px; cursor:pointer; }}
  .consent input {{ width:18px; height:18px; margin-top:2px; flex-shrink:0; accent-color:var(--accent); }}
  .consent strong {{ display:block; font-size:15px; margin-bottom:6px; }}
  .consent span span {{ display:block; font-size:13px; line-height:1.5; color:var(--muted); }}
  .consent a {{ color:var(--accent); font-weight:600; }}
  .form .btn {{ width:100%; }}

  .footer {{ padding:40px 32px 48px; border-top:1px solid var(--line); }}
  .foot {{ display:flex; justify-content:space-between; gap:24px; flex-wrap:wrap; font-size:12px; line-height:1.6; color:var(--muted); }}
  .foot-links {{ display:flex; gap:20px; }}

  @media (max-width:900px) {{
    .nav {{ padding:0 16px; }} .hide {{ display:none; }}
    .hero {{ padding:56px 16px 72px; }} .hero-grid,.join-grid {{ grid-template-columns:minmax(0,1fr); gap:48px; }}
    .hero h1 {{ font-size:44px; }} .hero-sub {{ font-size:19px; }}
    .phone {{ width:280px; }}
    .section,.band,.join {{ padding:80px 16px; }}
    .title,.join h2 {{ font-size:34px; }} .band h2 {{ font-size:32px; }}
    .cards,.band-grid {{ grid-template-columns:minmax(0,1fr); }}
    .form {{ padding:28px 20px; }} .row2 {{ grid-template-columns:minmax(0,1fr); gap:0; }}
    .footer {{ padding:32px 16px 40px; }}
  }}
</style>
</head>
<body>
<nav class="nav" aria-label="Main">
  <a href="/" class="logo" aria-label="{b["name"]}.AI home"><span class="mark">{b["name"][0]}G</span><span>{b["name"]}<span class="ai">.AI</span></span></a>
  <div class="nav-right">
    <a href="#how" class="hide">How it works</a>
    <a href="#join" class="nav-cta">Get early access</a>
  </div>
</nav>

<header class="hero">
  <div class="wrap hero-grid">
    <div>
      <div class="pill"><span class="dot"></span>Now inviting early members</div>
      <h1>{e(b["headline"]).replace("texted to you", "<em>texted to you</em>")}</h1>
      <p class="hero-sub">{e(b["sub"])}</p>
      <a href="#join" class="btn">Get early access</a>
      <p class="hero-note">Free to join the early access list. No spam, ever.</p>
      <div class="chips">{chips}</div>
    </div>
    <div class="phone" role="img" aria-label="Example text conversation: a matched job alert, the member replies INTERESTED, and {b["name"]} confirms.">
      <div class="screen">
        <div class="screen-head"><strong>{b["name"]}</strong>Text message</div>
        <div class="bubble in">{b["name"]}: New match. {e(t)}, {e(loc)}. {e(pay)}. {e(b["sample_co"])}. Reply INTERESTED to share your profile.</div>
        <div class="bubble out">INTERESTED</div>
        <div class="bubble in">Done. Your profile went to the hiring team. We'll text you if they want to talk.</div>
      </div>
    </div>
  </div>
</header>

<section id="how" class="section">
  <div class="wrap">
    <h2 class="title">{e(b["match_title"])}</h2>
    <p class="lead">No job boards to scroll and no recruiters cold calling. Only roles that match your profile, sent while you get on with your day.</p>
    <div class="cards">{match}</div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <h2>Private by design. You decide who sees your profile.</h2>
    <div class="band-grid">
      <div><h3>Invisible until you say so</h3><p>Employers can't search or browse members. Your profile is shared only when you reply INTERESTED to a specific role.</p></div>
      <div><h3>Texts at sensible hours</h3><p>Alerts arrive between 8am and 7pm in your time zone. Pause them or set a weekly limit anytime.</p></div>
      <div><h3>Real roles, vetted employers</h3><p>Every listing is reviewed before it goes out, with the pay range and work arrangement included.</p></div>
    </div>
  </div>
</section>

<section id="join" class="join">
  <div class="wrap join-grid">
    <div>
      <h2>Be first in line.</h2>
      <p class="body">We're opening {b["name"]} to a first group of {e(b["people"])}. Join the list and we'll text you when your membership is ready.</p>
      <ul class="checks">
        <li>{CHECK}Early members get their first month free</li>
        <li>{CHECK}Build your match profile in about five minutes</li>
        <li>{CHECK}Reply STOP anytime to stop texts</li>
      </ul>
    </div>
    <form class="form" name="early-access" method="POST" action="/thanks" data-netlify="true">
      <input type="hidden" name="form-name" value="early-access">
      <h3>Get early access</h3>
      <p class="fine">Takes 30 seconds.</p>
      <div class="row2">
        <div><label class="f" for="first">First name</label><input id="first" name="first_name" type="text" autocomplete="given-name" required></div>
        <div><label class="f" for="last">Last name</label><input id="last" name="last_name" type="text" autocomplete="family-name" required></div>
      </div>
      <label class="f" for="email">Email</label><input id="email" name="email" type="email" autocomplete="email" required>
      <label class="f" for="mobile">Mobile number</label><input id="mobile" name="mobile" type="tel" autocomplete="tel" placeholder="(555) 123-4567">
      <label class="consent" for="sms">
        <input id="sms" name="sms_consent" type="checkbox" value="yes">
        <span><strong>Yes, text me job alerts at this number.</strong>
        <span>I agree to receive recurring automated job alert texts from {b["name"]} at the mobile number provided. Message frequency varies. Msg &amp; data rates may apply. Reply STOP to opt out, HELP for help. Consent is not a condition of purchase. See our <a href="/terms">Terms</a> and <a href="/privacy">Privacy Policy</a>.</span></span>
      </label>
      <button type="submit" class="btn">Join the early access list</button>
    </form>
  </div>
</section>

<footer class="footer">
  <div class="wrap foot">
    <div>SMS job alerts: message frequency varies. Msg &amp; data rates may apply. Reply STOP to opt out, HELP for help. Consent is not a condition of purchase.<br>&copy; 2026 Foundry Holdings Inc. DBA {b["name"]}. All rights reserved.</div>
    <div class="foot-links"><a href="/privacy">Privacy Policy</a><a href="/terms">Terms of Service</a><a href="mailto:support@{b["domain"]}">Contact</a></div>
  </div>
</footer>
</body>
</html>
'''
for slug,b in BRANDS.items():
    os.makedirs(f'out/{slug}',exist_ok=True)
    open(f'out/{slug}/index.html','w').write(page(b))

# ---- Legal and thank-you pages (same look, short layout) ----
def shell(b, title, body):
    e=html.escape
    css = page(b).split('<style>')[1].split('</style>')[0]
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{e(title)} · {b["name"]}</title>
<meta name="robots" content="noindex">
<style>{css}
  .doc {{ max-width:720px; margin:0 auto; padding:72px 24px 96px; }}
  .doc .label {{ font-size:13px; font-weight:700; color:var(--accent); text-transform:uppercase; letter-spacing:.06em; margin-bottom:12px; }}
  .doc h1 {{ font-size:44px; font-weight:700; letter-spacing:-.025em; margin-bottom:8px; }}
  .doc .updated {{ font-size:14px; color:var(--muted); padding-bottom:28px; margin-bottom:12px; border-bottom:1px solid var(--line); }}
  .doc h2 {{ font-size:21px; font-weight:700; margin:36px 0 10px; }}
  .doc p, .doc li {{ font-size:16px; line-height:1.7; color:#424245; }}
  .doc p {{ margin-bottom:14px; }}
  .doc ul {{ padding-left:22px; margin:8px 0 14px; }}
  .doc a {{ color:var(--accent); font-weight:600; }}
  @media (max-width:900px) {{ .doc {{ padding:48px 16px 72px; }} .doc h1 {{ font-size:34px; }} }}
</style>
</head>
<body>
<nav class="nav" aria-label="Main">
  <a href="/" class="logo" aria-label="{b["name"]}.AI home"><span class="mark">{b["name"][0]}G</span><span>{b["name"]}<span class="ai">.AI</span></span></a>
  <div class="nav-right"><a href="/">Home</a></div>
</nav>
<main class="doc">{body}</main>
<footer class="footer">
  <div class="wrap foot">
    <div>SMS job alerts: message frequency varies. Msg &amp; data rates may apply. Reply STOP to opt out, HELP for help. Consent is not a condition of purchase.<br>&copy; 2026 Foundry Holdings Inc. DBA {b["name"]}. All rights reserved.</div>
    <div class="foot-links"><a href="/privacy">Privacy Policy</a><a href="/terms">Terms of Service</a><a href="mailto:support@{b["domain"]}">Contact</a></div>
  </div>
</footer>
</body>
</html>
'''

def privacy(b):
    n, d, s = b['name'], b['domain'], f'support@{b["domain"]}'
    return shell(b, 'Privacy Policy', f'''
<div class="label">Legal</div><h1>Privacy Policy</h1><p class="updated">Last updated: September 2026</p>
<p>{n}, operated by Foundry Holdings Inc. DBA {n} ("we," "us," or "our"), respects your privacy. This policy explains how we collect, use and protect your information when you use our website at {d} and our SMS job alert service.</p>
<h2>Information we collect</h2>
<ul><li>Name, email address and mobile phone number</li><li>Professional details you choose to share, such as your specialty, experience, credentials and career goals</li><li>Resumes and documents you upload</li><li>Payment information, processed securely by Stripe (we never store card numbers)</li></ul>
<h2>How we use your information</h2>
<ul><li>To send SMS job alerts matched to your profile</li><li>To manage your account and membership</li><li>To contact you about your account and our service</li><li>To match your profile to relevant roles from employers</li><li>To improve our service</li></ul>
<h2>SMS communications</h2>
<p>If you opt in, you agree to receive recurring automated SMS job alert messages from {n}, operated by Foundry Holdings Inc. Message frequency varies. Message and data rates may apply. Consent to receive text messages is not a condition of any purchase. You can opt out at any time by replying STOP to any message. Reply HELP for help, or contact <a href="mailto:{s}">{s}</a>.</p>
<p><strong>No mobile information will be shared with third parties or affiliates for marketing or promotional purposes.</strong> Text messaging originator opt-in data and consent will not be shared with any third parties, except with the service providers that deliver our messages (such as Twilio).</p>
<h2>Information sharing</h2>
<p>We do not sell your personal information. We share it only:</p>
<ul><li>With an employer, and only after you reply INTERESTED to that employer's specific role</li><li>With service providers that help us run the service (such as Stripe, Twilio, Supabase and Netlify)</li><li>When required by law or to protect our legal rights</li></ul>
<p>Employers cannot search or browse member profiles.</p>
<h2>Data security</h2>
<p>We use industry-standard safeguards to protect your information. Resumes are stored privately and are never public.</p>
<h2>Your choices</h2>
<p>You can access, update or delete your information at any time. To request deletion, email <a href="mailto:{s}">{s}</a>.</p>
<h2>Contact us</h2>
<p>Questions about this policy? Email <a href="mailto:{s}">{s}</a>.</p>''')

def terms(b):
    n, s = b['name'], f'support@{b["domain"]}'
    return shell(b, 'Terms of Service', f'''
<div class="label">Legal</div><h1>Terms of Service</h1><p class="updated">Last updated: September 2026</p>
<p>These Terms govern your use of {n}, operated by Foundry Holdings Inc. DBA {n} ("we," "us," or "our"). By joining our early access list, creating an account or using our service, you agree to these Terms.</p>
<h2>The service</h2>
<p>{n} is a private SMS job alert service for {html.escape(b["people"])}. We match members with relevant roles from vetted employers and deliver alerts by text message.</p>
<h2>SMS program terms</h2>
<p>{n} Job Alerts, operated by Foundry Holdings Inc. DBA {n}. You opt in by providing your mobile number and checking the SMS consent box on our website or in your account. Message frequency varies. Message and data rates may apply. Reply STOP to opt out at any time. Reply HELP for help, or email <a href="mailto:{s}">{s}</a>. U.S. subscribers only. Consent to receive text messages is not a condition of any purchase. Carriers are not liable for delayed or undelivered messages.</p>
<h2>Accounts</h2>
<p>You agree to provide accurate information and to keep your account secure. Membership is personal and non-transferable. We may approve or decline membership at our discretion.</p>
<h2>Membership fees</h2>
<p>Membership pricing will be shown before you are asked to pay. Paid memberships renew automatically until cancelled, and you can cancel at any time. Fees are non-refundable unless required by law.</p>
<h2>Acceptable use</h2>
<ul><li>Do not provide false or misleading information</li><li>Use the service only for a genuine job search or hiring</li><li>Do not share or sell your account access</li><li>Do not use automated means to access or scrape the service</li></ul>
<h2>Employers</h2>
<p>Employers confirm that every listing is a genuine, current opening, and may use a member's details only to follow up on that member's interest in a specific role.</p>
<h2>Privacy</h2>
<p>Your use of the service is also governed by our <a href="/privacy">Privacy Policy</a>.</p>
<h2>Limitation of liability</h2>
<p>The service is provided "as is." We do not guarantee job placements, employer responses or the accuracy of listings. To the extent permitted by law, our liability is limited to the amount you paid us in the three months before a claim.</p>
<h2>Contact</h2>
<p>Questions about these Terms? Email <a href="mailto:{s}">{s}</a>.</p>''')

def thanks(b):
    return shell(b, "You're on the list", f'''
<div class="label">Early access</div><h1>You're on the list.</h1>
<p class="updated">Thanks for joining {b["name"]}.</p>
<p>We'll email you when your membership is ready. If you opted in to text alerts, we'll also text you then. You can reply STOP at any time to stop texts, or HELP for help.</p>
<p><a href="/">Back to home</a></p>''')

for slug,b in BRANDS.items():
    for name, fn in [('privacy', privacy), ('terms', terms), ('thanks', thanks)]:
        open(f'out/{slug}/{name}.html','w').write(fn(b))
