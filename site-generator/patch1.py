import re
s = open('build.js', encoding='utf8').read()
s = re.sub(r"const P = P0\.filter.*?\n", "const P = P0.map(p => ({ ...p, rel: p.rel.filter(r => P0.some(x => x.s === r)) }));\n", s, count=1)
s = s.replace("const JJ = J(J0);", "const JJ = J0;")
a = s.index("const nav = (a) => {"); b = s.index("const social =")
s = s[:a] + """const nav = (a) => {
  const li = (h, t, k) => `<li${a === k ? ' class="active"' : ''}><a href="${h}">${t}</a></li>`;
  return `<ul>${li('index.html', 'Home', 'home')}${li('collections.html', 'Fabrics & Yarns', 'fabric')}${li('about.html', 'About Us', 'about')}${li('journal.html', 'Journal', 'journal')}${li('contact.html', 'Contact', 'contact')}</ul>`;
};
""" + s[b:]
s = s.replace("a: 'faq', title: 'FAQ'", "a: 'about', title: 'FAQ'").replace("a: 'wholesale', title: 'Wholesale", "a: 'about', title: 'Wholesale")
s = s.replace("Four Signature Fabrics. <br> One Standard of Excellence.", "Fabrics & Yarns. <br> One Standard of Excellence.")
s = s.replace("Luxury Fabrics, India", "Luxury Yarns & Fabrics, India")
s = s.replace("title('Fabric Collection',", "title('Fabrics & Yarns',")
s = s.replace("'Fabrics of <br> Rare Craft', 'Handwoven Banarasi silk, mulmul, block print and linen from India’s master weavers, delivered to designers and fashion houses worldwide.'", "'Yarns & Fabrics <br> of Rare Craft', 'Premium cotton, silk, wool and zari yarns, and handwoven Banarasi, mulmul, block-print and linen fabrics from India’s master weavers, delivered worldwide.'")
s = s.replace("crumb('Fabric Collection', 'rolls1')", "crumb('Fabrics & Yarns', 'rolls1')").replace("title: 'Fabric Collection'", "title: 'Fabrics & Yarns'")
s = s.replace("['collections.html', 'Fabric Collection'], ", "['collections.html', 'Fabrics & Yarns'], ")
helpers = open('helpers.js', encoding='utf8').read()
s = s.replace("const write = (f, html)", helpers + "\nconst write = (f, html)", 1)
a = s.index("function newsCardHome"); b = s.index("\n", a)
s = s[:a] + open('newscard.js', encoding='utf8').read().strip() + s[b:]
s = s.replace('<div class="news-wrapper"><div class="row g-4 news-row">${JJ.slice(0, 3).map(newsCardHome).join(\'\')}</div></div>', '<div class="row g-4">${JJ.slice(0, 3).map(newsCardHome).join(\'\')}</div>')
s = s.replace("<section class=\"testimonial-section", "${featureGrid('Our Promise', 'Crafted Responsibly, Delivered Reliably', PROMISE)}\n<section class=\"testimonial-section", 1)
s = s.replace("${ctaBand('Let’s create something extraordinary.'", "${faqSection('hf', FAQ.slice(0, 5))}\n${ctaBand('Let’s create something extraordinary.'")
i = s.index("page({ file: 'collections.html'"); j = s.index("// ---------- PRODUCT PAGES")
s = s[:i] + open('collections.js', encoding='utf8').read() + "\n" + s[j:]
s = s.replace("<div class=\"imgae-area\"><div class=\"row g-4\">${p.g.map", open('origin.html', encoding='utf8').read().strip() + "\n<div class=\"imgae-area\"><div class=\"row g-4\">${p.g.map", 1)
s = s.replace("<section class=\"section-padding pt-0\"><div class=\"container\">${title('You May Also Like'", "${steps('How to Order', 'Four Simple Steps', ORDER, 'section-bg')}\n<section class=\"section-padding\"><div class=\"container\">${title('You May Also Like'", 1)
s = s.replace("<section class=\"counter-section counter-two fix pb-0\">", open('about1.js', encoding='utf8').read().strip() + "\n<section class=\"counter-section counter-two fix pb-0\">", 1)
s = s.replace("<section class=\"section-padding\"><div class=\"container\"><div class=\"row g-4 align-items-center\"><div class=\"col-lg-6\"><div class=\"faq-content\">", open('about2.js', encoding='utf8').read().strip() + "\n<section class=\"section-padding\"><div class=\"container\"><div class=\"row g-4 align-items-center\"><div class=\"col-lg-6\"><div class=\"faq-content\">", 1)
s = s.replace("${ctaBand('Not sure which programme fits?'", "${steps('How It Works', 'Becoming a Trade Partner', ORDER, '')}\n${faqSection('wf', FAQ.slice(0, 4))}\n${ctaBand('Not sure which programme fits?'", 1)
s = s.replace("</div></div></div></div></section>` });\n\n// ---------- SEARCH", "</div></div></div></div></section>\n" + open('contact1.js', encoding='utf8').read().strip() + "` });\n\n// ---------- SEARCH", 1)
open('build.js', 'w', encoding='utf8').write(s)
print('ok')
