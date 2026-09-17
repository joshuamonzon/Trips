import re, base64, pathlib, sys
root = pathlib.Path(__file__).parent
src = (root / 'compare.src.html').read_text()

def repl(m):
    key = m.group(1)
    if key.startswith('t:'):
        p = root / 'thumb' / (key[2:] + '.jpeg')
    else:
        p = root / 'img' / (key + '.jpeg')
    return base64.b64encode(p.read_bytes()).decode()

out = re.sub(r'@@([\w:]+)@@', repl, src)
assert '@@' not in out
(root / 'compare.html').write_text(out)

# test wrapper mimicking the publish skeleton
wrapped = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
           '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
           '<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}'
           'body{margin:0;font:14px system-ui;background:#f7f7f5}img{max-width:100%}[hidden]{display:none!important}</style>'
           '</head><body>' + out + '</body></html>')
(root / 'test.html').write_text(wrapped)
print('compare.html', len(out), 'bytes;', 'test.html', len(wrapped))
