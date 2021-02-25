from pytube import YouTube
import os.path
import ffmpeg

# 비디오 추출
def extract_video():
    yotube_address = input('address: ')
    yt = YouTube(yotube_address)
    yt.streams \
        .filter(progressive=True, file_extension='mp4') \
        .order_by('resolution') \
        .desc() \
        .first() \
        .download('/Users/yslee/Downloads/youtube')

# 오디오 추출

def extract_audio():
    yotube_address = input('address: ')
    yt = YouTube(yotube_address)
    vids = yt.streams.all()
    for i in range(len(vids)):
        print(i,'. ',vids[i])
    vnum = int(input("다운받을 번호는? "))
    parent_dir = '/Users/yslee/Downloads/youtube'
    vids[vnum].download(parent_dir)
    k = vids[vnum].download(parent_dir)
    print(k)
    ffmpeg.input(k).output(k[:-1]+'3')
    #os.remove(k)

extract_audio()
