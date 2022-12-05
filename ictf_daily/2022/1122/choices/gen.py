#!/usr/bin/env python3

import os
from random import choice

def mk(folder):
    try:
        os.mkdir(folder)
    except FileExistsError as e:
        pass

# make folder called 0 if not exist
# put up and down in 0

levels = 17

for i in range(levels):
    os.system(f"rm -rf files/{i}")

mk('files/0')

flag = open("files/0/flag.txt", "w")
flag.write("jctf{red_flags_and_fake_flags_form_an_equivalence_class}")
flag.close()
os.system("zip -j -0 files/0/up-0.zip files/0/flag.txt")

flag = open("files/0/flag.txt", "w")
flag.write("ictf{th3re_are_po1nts_to_b3_scored._ther3_are_gam3s_to_be_won.}")
flag.close()
os.system("zip -j -0 files/0/down-0.zip files/0/flag.txt")

last_real = "down"

for i in range(1, levels):
    mk(f"files/{i}")
    new_real = choice(["up", "down"])
    not_new_real = "down" if new_real == "up" else "up"
    not_last_real = "down" if last_real == "up" else "up"

    os.system(f"zip -j -0 files/{i}/{new_real}-{i}.zip files/{i-1}/up-{i-1}.zip files/{i-1}/down-{i-1}.zip")
    os.system(f"cp files/{i-1}/{not_last_real}-{i-1}.zip files/{i-1}/{last_real}-{i-1}.zip")
    os.system(f"zip -j -0 files/{i}/{not_new_real}-{i}.zip files/{i-1}/up-{i-1}.zip files/{i-1}/down-{i-1}.zip")

    last_real = new_real

print(last_real)