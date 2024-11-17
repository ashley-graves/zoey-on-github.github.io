import os
import sys
import mimetypes
from pyffmpeg import FFmpeg
from subprocess import run

directory = os.fsdecode(sys.argv[2])

f = open("head.html", "r", encoding="utf-8")
head = f.read()
f.close()

f = open(sys.argv[1], "w", encoding="utf-8")
f.write(head)
f.write('\n\n<body>\n')


for file in os.listdir(directory):
    filename = os.fsdecode(file)
    thumbfile = filename[0:filename.rindex(".")] + ".jpg"

    path = os.path.join(directory, filename)
    thumb = os.path.join("thumbs", thumbfile)

    p = run(executable='ffmpeg', args=["", "-n", "-i", path, "-vf", "scale=100:100:force_original_aspect_ratio=increase", "-frames:v", "1", thumb])
    if p.returncode != 0:
        print("[!!!!!] ERROR: NON-ZERO EXIT CODE")
        exit()

    f.write(('  <a href="%s">\n') % path)
    f.write(('      <img src="%s" />\n') % thumb)
    f.write(('  </a>\n'))

f.write('</body>\n\n</html>')
f.close()
