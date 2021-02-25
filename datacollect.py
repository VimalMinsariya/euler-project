from bs4 import BeautifulSoup
from pandas import DataFrame
from pandas import ExcelFile
import numpy

xlsx = ExcelFile("http://itpaper.co.kr/demo/py/senior_lsf.xlsx")
df = xlsx.parse(xlsx.sheet_names[0])

print(df)

map_svg = None
with open('map_seoul.svg', 'r') as f:
    map_svg = f.read()

soup = BeautifulSoup(map_svg, features="html.parser")
paths = soup.select('path[id]')

colors = ['#F1EEF6', '#D4B9DA', '#C994C7', '#DF65B9', '#DD1C77', '#980043']

for p in paths:
    #print(p['id'])

    # 데이터프레임에서 지역명에 대한 복지시설 수 조회하기
    tmp_df = df.query("COUNTY == '" + p['id'] + "'")
    #print(tmp_df)

    # 복지시설 수
    try:
        count = tmp_df.loc[tmp_df.index[0], 'NUMBER']
        #print("%s >> %d" % (p['id'], count ))
    except IndexError:
        pass

    if count > 250:
        color_index = 5
    elif count > 200:
        color_index = 4
    elif count > 150:
        color_index = 3
    elif count > 100:
        color_index = 2
    elif count > 50:
        color_index = 1
    else:
        color_index = 0

    # 가져온 svg 이미지의 path 태그들의 fill 속성에 선정한 단계의 색상값 적용
    p['fill'] = colors[color_index]

new_svg = soup.prettify()

with open('seoul_map_on.svg', 'w') as f:
    f.write(new_svg)