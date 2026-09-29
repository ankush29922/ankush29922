"""Generate original, self-contained profile artwork (no external services)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
ASSETS.mkdir(exist_ok=True)


def hero(dark):
    bg, panel, line = ("#0b1322", "#111e30", "#25344b") if dark else ("#f0f5f9", "#ffffff", "#d2dee9")
    ink, muted = ("#edf7ff", "#9fb4ca") if dark else ("#142b41", "#506b80")
    mint, blue = ("#87efd2", "#a6c9ff") if dark else ("#08785f", "#2558a0")
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="420" viewBox="0 0 1200 420" role="img" aria-labelledby="title desc">
<title id="title">Ankush Kumar — xen</title><desc id="desc">Software, cloud and connected devices. Original engineering-themed profile banner.</desc>
<defs>
<linearGradient id="back" x2="1" y2="1"><stop stop-color="{bg}"/><stop offset="1" stop-color="{panel}"/></linearGradient>
<linearGradient id="accent"><stop stop-color="{mint}"/><stop offset="1" stop-color="{blue}"/></linearGradient>
<pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="{line}" stroke-width=".6"/></pattern>
</defs>
<rect x="1" y="1" width="1198" height="418" rx="28" fill="url(#back)" stroke="{line}"/>
<path d="M682 1H1172Q1199 1 1199 28V392Q1199 419 1172 419H682Z" fill="url(#grid)" opacity=".7"/>
<path d="M641 48V372" stroke="{line}"/>
<rect x="55" y="48" width="37" height="37" rx="11" fill="{mint}"/>
<path d="m64 57 18 19m0-19L64 76" stroke="{bg}" stroke-width="4.5" stroke-linecap="square"/>
<text x="107" y="73" fill="{muted}" font-family="Consolas,monospace" font-size="16" letter-spacing="2">xen / ENGINEERING</text>
<text x="53" y="189" fill="{ink}" font-family="Segoe UI,Arial,sans-serif" font-size="87" font-weight="700" letter-spacing="-4">Ankush</text>
<text x="53" y="277" fill="{mint}" font-family="Segoe UI,Arial,sans-serif" font-size="87" font-weight="700" letter-spacing="-4">Kumar.</text>
<text x="58" y="329" fill="{ink}" font-family="Segoe UI,Arial,sans-serif" font-size="23">Software. Cloud. Connected devices.</text>
<text x="58" y="372" fill="{muted}" font-family="Consolas,monospace" font-size="14" letter-spacing="1.1">COMPUTER SCIENCE / KIIT</text>
<path d="M726 144V181Q726 193 742 193H790M1031 228V273Q1031 284 1015 284H981" fill="none" stroke="url(#accent)" stroke-width="2"/>
<g font-family="Consolas,monospace" font-size="14" fill="{muted}">
<text x="706" y="54" letter-spacing="2">FROM AN IDEA</text>
<text x="880" y="380" letter-spacing="2">TO SOMETHING USEFUL</text>
</g>
<rect x="687" y="76" width="327" height="82" rx="16" fill="{panel}" stroke="{line}"/>
<rect x="713" y="100" width="32" height="28" rx="6" fill="none" stroke="{mint}" stroke-width="1.5"/>
<path d="m722 109 5 5-5 5m10 0h5" fill="none" stroke="{mint}" stroke-width="1.5"/>
<text x="765" y="124" font-family="Segoe UI,Arial,sans-serif" fill="{ink}" font-size="24" font-weight="600">Write the software</text>
<rect x="787" y="166" width="348" height="82" rx="16" fill="{panel}" stroke="{line}"/>
<path d="M815 215h26a9 9 0 0 0 1-18 12 12 0 0 0-23-2 10 10 0 0 0-4 20Z" fill="none" stroke="{blue}" stroke-width="1.8"/>
<text x="866" y="214" font-family="Segoe UI,Arial,sans-serif" fill="{ink}" font-size="24" font-weight="600">Connect the systems</text>
<rect x="723" y="266" width="299" height="82" rx="16" fill="{panel}" stroke="{line}"/>
<rect x="750" y="288" width="28" height="28" rx="5" fill="none" stroke="{mint}" stroke-width="1.7"/>
<path d="M757 284v4m7-4v4m7-4v4m-14 28v5m7-5v5m7-5v5m-26-25h5m-5 10h5m28-10h5m-5 10h5" stroke="{mint}" stroke-width="1.7"/>
<rect x="758" y="296" width="12" height="12" rx="2" fill="{mint}" opacity=".3"/>
<text x="799" y="314" font-family="Segoe UI,Arial,sans-serif" fill="{ink}" font-size="24" font-weight="600">Make it work</text>
<circle cx="726" cy="177" r="4" fill="{mint}"/><circle cx="1031" cy="259" r="4" fill="{blue}"/>
<path d="M1043 70h68m-34-34v68" stroke="{line}" stroke-width="1.3"/><circle cx="1077" cy="70" r="18" fill="none" stroke="{line}"/>
</svg>'''


def project(kind):
    tv = kind == "lggramtv"
    title, subtitle = ("LGgramTV", "Your Telegram library. Your LG TV.") if tv else ("TYPXEN", "Local automation. Connected hardware.")
    eyebrow = "01 / LIVING-ROOM SOFTWARE" if tv else "02 / DEVICE AUTOMATION"
    color, end = ("#8bf2d8", "#17334e") if tv else ("#ffd092", "#382e37")
    if tv:
        art = '''<g transform="translate(402 70)"><rect x="0" y="0" width="124" height="89" rx="11" fill="#0b1727" stroke="#8bf2d8" stroke-width="2"/><path d="M62 89v14m-26 0h52" stroke="#8bf2d8" stroke-width="2"/><g transform="translate(34 15) scale(.55)"><path d="M50 13 61 35 86 39 68 57 72 82 50 70 28 82 32 57 14 39 39 35Z" fill="#d8fff4"/><rect x="30" y="37" width="40" height="27" rx="9" fill="#123151"/><circle cx="40" cy="48" r="3" fill="#90f8df"/><circle cx="60" cy="48" r="3" fill="#90f8df"/><path d="m47 52 8 5-8 5Z" fill="#90f8df"/></g></g>'''
    else:
        art = '''<g transform="translate(417 61)" fill="none" stroke="#ffd092" stroke-width="2"><rect x="0" y="4" width="70" height="110" rx="14" fill="#172031"/><path d="M25 15h20M30 103h10"/><path d="m29 42 20 20-20 18V42l20 38-20-18 20-20"/><path d="M88 40h18m-18 11h18m-18 11h18m-18 11h18" opacity=".6"/><rect x="100" y="28" width="37" height="58" rx="5" fill="#172031"/><path d="M108 40h21v16h-21zm0 23h8m5 0h8m-21 11h21"/></g>'''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="600" height="260" viewBox="0 0 600 260" role="img" aria-labelledby="title desc">
<title id="title">{title}</title><desc id="desc">{subtitle}</desc>
<defs><linearGradient id="surface" x2="1" y2="1"><stop stop-color="#111c2c"/><stop offset="1" stop-color="{end}"/></linearGradient></defs>
<rect x="1" y="1" width="598" height="258" rx="21" fill="url(#surface)" stroke="#314252"/>
<path d="M361 24v183M376 207h185" stroke="#ffffff" opacity=".07"/>
<text x="29" y="43" fill="{color}" font-family="Consolas,monospace" font-size="13" letter-spacing="1.1">{eyebrow}</text>
<text x="26" y="121" fill="#f0f6ff" font-family="Segoe UI,Arial,sans-serif" font-size="48" font-weight="700" letter-spacing="-1.8">{title}</text>
<text x="29" y="157" fill="#bbccdb" font-family="Segoe UI,Arial,sans-serif" font-size="16">{subtitle}</text>
<path d="M29 188h50" stroke="{color}" stroke-width="3"/>
<text x="29" y="230" fill="{color}" font-family="Consolas,monospace" font-size="13" letter-spacing="1">BUILT BY XEN</text>
<path d="M541 222h18m-6-6 6 6-6 6" fill="none" stroke="{color}" stroke-width="2"/>
{art}
</svg>'''


for name, content in {
    "hero-dark.svg": hero(True),
    "hero-light.svg": hero(False),
    "lggramtv-card.svg": project("lggramtv"),
    "typxen-card.svg": project("typxen"),
}.items():
    (ASSETS / name).write_text(content + "\n", encoding="utf-8")
print("Generated four original SVG assets.")
