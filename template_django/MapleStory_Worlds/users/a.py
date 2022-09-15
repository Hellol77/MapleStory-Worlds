import os
os.environ.get("DJANGO_SETTINGS_MODULE", "MapleStory-Worlds.settings")

import django
django.setup()

from django.contrib.auth.hashers import make_password


a = "1234"
hashed_pass = make_password(a)
print(hashed_pass)