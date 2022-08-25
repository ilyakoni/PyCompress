import os
import ffmpeg
from pathlib import Path

pat="\\uncompressed\\"
outpath='\\compressed\\'
os.chdir(os.path.dirname(__file__)+pat)
list = os.listdir()
p = Path(os.getcwd())
os.path.join(p.parent)


l = len(list)
i=0
for i in range (l):
    sex = (os.path.dirname(__file__)+pat+list[i])
    stream = ffmpeg.input(sex)
    print('compressing '+list[i])
    outputname=str(os.path.dirname(__file__)+outpath+ list[i])
    stream = ffmpeg.output(stream, outputname, **{'c:v': 'libx265'})
    ffmpeg.run(stream)
    os.remove(list[i])
    print('compressed! '+ list[i])
for i in range (9):
    print('Compressing process completed press any key to exit...')

      