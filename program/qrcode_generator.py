import qrcode

# Hello World! 로 QR 코드 생성
img = qrcode.make('https://url.kr/Hv4kPc')

# 생성된 이미지를 helloworld_qrcode.png로 저장
img.save('stop_nsl_qrcode.png')