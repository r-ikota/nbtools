"""
Copy Right 2018 Ryo IKOTA
BSD license
"""

import os
from nbconvert import HTMLExporter

htmlexporter = HTMLExporter()

html_dir = 'view-html'
if not os.path.exists(html_dir):
    os.mkdir(html_dir)

def convert(nbfile):
    f, ext = os.path.splitext(nbfile)
    htmlfile = os.path.join(html_dir, f + '.html')
    mtime = os.path.getmtime(nbfile)
    if os.path.exists(htmlfile):
        mtime2 = os.path.getmtime(htmlfile)
        if mtime2 > mtime:
            print(htmlfile + ': already exists.')
            return
        else:
            print(htmlfile + ': overwritten.')

    else:
        print(htmlfile + ': created.')

    output, resources = htmlexporter.from_filename(nbfile)
    html = output.encode(encoding='utf-8')

    with open(htmlfile, 'wb') as file:
        file.write(html)

def main():
    for fd in os.listdir():
        if os.path.isfile(fd):
            f,ext = os.path.splitext(fd)
            if ext=='.ipynb':
                convert(fd)

if __name__ == '__main__':
    main()
