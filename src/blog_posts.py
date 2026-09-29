# -*- coding: utf-8 -*-
from blog_posts_a import POSTS_A
from blog_posts_b import POSTS_B
POSTS = sorted(POSTS_A + POSTS_B, key=lambda p: p["date"], reverse=True)
