"""Turn the client's source photos (assets-src/) into optimised, semantically named
WebP files in public/assets/img/. Run: python3 scripts/build-images.py"""
import os
from PIL import Image, ImageOps

SRC = 'assets-src'
OUT = 'public/assets/img'
SIZES = (1600, 1000, 600)

# semantic name -> source file
MANIFEST = {
    # heroes / heros backgrounds (landscape preferred)
    'hero-lawn-mowing-moreton-bay':        'lawn-mowing-2.jpg',
    'hero-acreage-mowing-somerset':        'root-480478278.jpg',
    'hero-hedge-trimming-moreton-bay':     'fb-475344934.jpg',
    'hero-garden-cleanup-moreton-bay':     'root-d6181f13.jpg',
    'hero-mulching-moreton-bay':           'root-a59f6b52.jpg',
    'hero-about-green-estates':            'garden-1.jpg',
    'hero-contact-wamuran':                'root-IMG_4252.jpg',
    # service cards / features
    'ride-on-mowing-acreage-moreton-bay':  'root-IMG_3929.jpg',
    'ride-on-mower-acreage-wamuran':       'acreage-mowing-2.jpg',
    'acreage-dam-mowing-somerset':         'acreage-mowing-1.jpg',
    'zero-turn-mower-caboolture':          'root-IMG_3559.jpg',
    'push-mowing-residential-lawn':        'fb-475981731.jpg',
    'push-mower-striped-lawn-morayfield':  'wix-imgi-6.jpg',
    'push-mower-front-lawn-north-lakes':   'wix-imgi-4.jpg',
    'hedge-trimming-shaped-hedges':        'hedge-2.jpg',
    'hedge-trimming-long-hedge':           'hedge-4.jpg',
    'hedge-trimming-round-hedge-house':    'root-IMG_3916.jpg',
    'hedge-trimming-formal-hedges':        'root-IMG_3917.jpg',
    'hedge-trimming-townhouse-hedges':     'root-1a78f953.jpg',
    'garden-cleanup-before-overgrown':     'root-67c6d520.jpg',
    'garden-cleanup-after-cleared':        'root-d6181f13.jpg',
    'yard-cleanup-before-long-grass':      'garden-before.jpg',
    'yard-cleanup-after-mown':             'garden-after.jpg',
    'garden-cleanup-tidy-yard':            'garden-4.jpg',
    'mulching-garden-bed-commercial':      'root-a59f6b52.jpg',
    'mulched-garden-bed-fenceline':        'root-15346f48.jpg',
    'garden-beds-trees-tidy':              'root-fc881762.jpg',
    'garden-maintenance-commercial-strip': 'root-2524515e.jpg',
    'commercial-lawn-mowing-units':        'root-ac5e8af5.jpg',
    'footpath-edging-strathpine':          'root-508197597.jpg',
    'branded-trailer-green-estates':       'hedge-5.jpg',
    'freshly-mown-lawn-redcliffe':         'street-side-mowing.jpg',
    'walkway-mowing-edging':               'walkway-mowing.jpg',
    'acreage-mowing-shed':                 'root-481336650.jpg',
}

os.makedirs(OUT, exist_ok=True)
for name, src in MANIFEST.items():
    p = os.path.join(SRC, src)
    im = ImageOps.exif_transpose(Image.open(p)).convert('RGB')
    for s in SIZES:
        outp = os.path.join(OUT, f'{name}-{s}.webp')
        if os.path.exists(outp):
            continue
        w, h = im.size
        if w > s:
            r = s / w
            im2 = im.resize((s, round(h * r)), Image.LANCZOS)
        else:
            im2 = im.copy()
        im2.save(outp, 'WEBP', quality=78, method=6)
    print(name, '<-', src, im.size)
print('done', len(MANIFEST))
