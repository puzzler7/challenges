#!/usr/bin/env python3

import zipfile
import io

z = zipfile.ZipFile("output/flag.zip")

for i in range(100):
    files = {}
    for f in z.namelist():
        files[f] = z.read(f)
        print(f, len(files[f]))
        
    filename = max(files, key=lambda x:len(files[x]))
    content = io.BytesIO(files[filename])
    z = zipfile.ZipFile(content)
    print(filename)
z.extractall(path="output")