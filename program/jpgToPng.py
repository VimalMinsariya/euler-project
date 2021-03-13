#Image compress

from subprocess import call
from PIL import Image

dir = '/Users/yslee/Downloads/'
fname = '4차선전전.png'
cmd = 'pngquant --ext compress.png '+dir+fname
call(cmd, shell=True)

im = Image.open(dir+'4차선전전compress.png') # 이미지 불러오기
im.show() # 이미지 보여주기