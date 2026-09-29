from PIL import Image
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = os.path.join(ROOT, "public/assets/img/logo-green-estates-gardening.webp")
im = Image.open(src).convert("RGBA")
# crop to the badge (mark only, above the wordmark gap at y=179)
mark = im.crop((0, 0, im.width, 179))
bbox = mark.split()[3].getbbox(); mark = mark.crop(bbox)
side = max(mark.size) + 24
def make(size, bg=None):
    canvas = Image.new("RGBA", (side, side), bg or (0, 0, 0, 0))
    canvas.alpha_composite(mark, ((side - mark.width) // 2, (side - mark.height) // 2))
    return canvas.resize((size, size), Image.LANCZOS)
out = os.path.join(ROOT, "public/assets/img")
make(192).save(os.path.join(out, "favicon.png"))
make(512).save(os.path.join(out, "icon-512.png"))
make(180, (249, 250, 247, 255)).convert("RGB").save(os.path.join(out, "apple-touch-icon.png"))
make(32).save(os.path.join(ROOT, "public/favicon.ico"), sizes=[(32, 32), (16, 16)])
print("favicons ok", mark.size)
