import re, sys, math
sys.path.insert(0, 'src')
import blog_posts
def text(h): return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", h)).strip()
def article_text(p):
    return " ".join([text(p["quick"]), text(p["body"]), " ".join(text(q) + " " + text(a) for q, a in p["faqs"]), text(p["cta_heading"]), text(p["cta_text"])])
def report(posts=None):
    rows = []
    for p in posts or blog_posts.POSTS:
        t = article_text(p).lower(); w = len(t.split()); kw = p["keyword"].lower()
        c = len(re.findall(r"(?<![a-z])" + re.escape(kw) + r"(?![a-z])", t))
        lo, hi = math.ceil(0.013 * w), math.floor(0.015 * w)
        rows.append((p["slug"], p["date"], kw, w, c, lo, hi, c / w * 100))
    return rows
if __name__ == "__main__":
    for r in report():
        print(f"{r[0]:40s} {r[1]}  '{r[2]}'  words={r[3]:5d}  count={r[4]:2d}  target={r[5]}-{r[6]}  now={r[7]:.2f}%")
