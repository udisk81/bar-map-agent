import sys
import os.path

import os
import glob
import urllib.request
import json
import gzip

import urllib
import sys
import subprocess


def fetch(url):
    req = urllib.request.Request(url)
    req.add_header('user-agent', 'pr-downloader/0.7-752-g613ba1d')
    return opener.open(req)


path_bin, _ = os.path.split(sys.argv[0])
proxy = open(path_bin + '/proxy.ini').read().strip()
path_oldpr = path_bin + '/pr-downloader-old.exe'

if '--download-map' not in set(sys.argv):
    cmds = [path_oldpr] + list(sys.argv[1:])
    subprocess.call(cmds)
    sys.exit()

assert '--filesystem-writepath' == sys.argv[1]
assert '--download-map' == sys.argv[3]

path_maps = sys.argv[2] + '/maps'
if not os.path.exists(path_maps):
    os.makedirs(path_maps)

mapname = sys.argv[4]
mapname = urllib.parse.quote(mapname)

proxy_handler = urllib.request.ProxyHandler({'https': proxy})
opener = urllib.request.build_opener(proxy_handler)

u = f'https://files-cdn.beyondallreason.dev/find?category=map&springname={mapname}'
meta = fetch(u)
meta = json.load(meta)[0]

filename = meta['filename']

print('md5', meta['md5'])
hash_ = meta['md5'] + '  ' + filename + '\n'
hash_ = gzip.compress(hash_.encode())
with open(path_maps + '/' + filename + '.md5.gz', 'wb') as f:
    f.write(hash_)

url = meta['mirrors'][0]
req = fetch(url)

print(filename)
path = path_maps + '/' + filename
f_out = open(path, 'wb')
while True:
    data = req.read(1024 * 16)
    if len(data) < 1: break
    f_out.write(data)
