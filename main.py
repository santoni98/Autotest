import os
import shutil
import zipfile
from objObjectsCounter import objObjectsCounter
from objScale import objScale
from objTriangleCount import objTriangleCount
from textureDifference import textureDifference
from textureFill import textureFill
from textureMainCheck import textureMainCheck
from textureSolidColor import textureSolidColor

# get zip archive
with zipfile.ZipFile("models.zip", "r") as zip_ref:
    zip_ref.extractall("zip")

score = 0  # Баллы

# obj 1 unit
def obj(arg1, arg2):
    temp = objTriangleCount(arg1)
    constant_tris1 = arg2
    points = 0
    if temp >= constant_tris1 * 0.1:
        if temp < constant_tris1 * 1.75:
            points += 2
            if temp > constant_tris1:
                points += 1
    return points

def PointsTxtrCount(arg):
    points = 0
    if textureMainCheck(arg):
        points += 1
        if textureFill(arg) > 0.65:
            points += 1
    return points
    # ->

for i in range(10):
    i += 1  # Так надо
    # Первая папка
    if i == 1:
        # Сделать проверку содержимого архива
        if (os.path.exists('zip/1/wall_simple.obj')):
            if objObjectsCounter('zip/1/wall_simple.obj') == 1:
                score += obj('zip/1/wall_simple.obj', 100)
                # Проверка текстуры
                # 1 2 3
                score1 = 0
                score2 = 0
                score3 = 0
                if (os.path.exists('zip/1/wall_simple_tex1.png')):
                    if (os.path.exists('zip/1/wall_simple_tex2.png')):
                        if (os.path.exists('zip/1/wall_simple_tex3.png')):
                            score1 = PointsTxtrCount('zip/1/wall_simple_tex1.png')
                            score2 = PointsTxtrCount('zip/1/wall_simple_tex2.png')
                            score3 = PointsTxtrCount('zip/1/wall_simple_tex3.png')
                # Наименьший балл за текстуры
                minimal = score1
                if score2 < minimal:
                    minimal = score2
                if score3 < minimal:
                    minimal = score3
                score += minimal
        print(score)
    if i == 2:
        if (os.path.exists('zip/2/wall_lux.obj')):
            if objObjectsCounter('zip/2/wall_lux.obj') == 1:
                score += obj('zip/2/wall_lux.obj', 150)
                # Проверка текстуры
                # 1 2
                score1 = 0
                score2 = 0
                if (os.path.exists('zip/2/wall_lux_tex1.png')):
                    if (os.path.exists('zip/2/wall_lux_tex2.png')):
                        score1 = PointsTxtrCount('zip/2/wall_lux_tex1.png')
                        score2 = PointsTxtrCount('zip/2/wall_lux_tex2.png')
                # Наименьший бал за текстуры
                minimal = score1
                if score2 < minimal:
                    minimal = score2
                score += minimal
        print(score)
    if i == 3:
        if (os.path.exists('zip/3/wall_simple_window.obj')):
            if objObjectsCounter('zip/3/wall_simple_window.obj') == 1:
                score += obj('zip/3/wall_simple_window.obj', 150)
                # Проверка текстуры
                # 1 2 3
                score1 = 0
                score2 = 0
                score3 = 0
                if (os.path.exists('zip/3/wall_simple_window_tex1.png')):
                    if (os.path.exists('zip/3/wall_simple_window_tex2.png')):
                        if (os.path.exists('zip/3/wall_simple_window_tex3.png')):
                            score1 = PointsTxtrCount('zip/3/wall_simple_window_tex1.png')
                            score2 = PointsTxtrCount('zip/3/wall_simple_window_tex2.png')
                            score3 = PointsTxtrCount('zip/3/wall_simple_window_tex3.png')
                # Наименьший бал за текстуры
                minimal = score1
                if score2 < minimal:
                    minimal = score2
                if score3 < minimal:
                    minimal = score3
                score += minimal
        print(score)
    if i == 4:
        if (os.path.exists('zip/4/wall_lux_window.obj')):
            if objObjectsCounter('zip/4/wall_lux_window.obj') == 1:
                score += obj('zip/4/wall_lux_window.obj', 300)
                # Проверка текстуры
                # 1 2
                score1 = 0
                score2 = 0
                if (os.path.exists('zip/4/wall_lux_window_tex1.png')):
                    if (os.path.exists('zip/4/wall_lux_window_tex2.png')):
                        score1 = PointsTxtrCount('zip/4/wall_lux_window_tex1.png')
                        score2 = PointsTxtrCount('zip/4/wall_lux_window_tex2.png')
                # Наименьший бал за текстуры
                minimal = score1
                if score2 < minimal:
                    minimal = score2
                score += minimal
        print(score)
    if i == 5:
        if (os.path.exists('zip/5/roof_simple.obj')):
            if objObjectsCounter('zip/5/roof_simple.obj') == 1:
                score += obj('zip/5/roof_simple.obj', 200)
                # Проверка текстуры
                # 1
                if (os.path.exists('zip/5/roof_simple_tex1.png')):
                    if (os.path.exists('zip/5/roof_simple_tex2.png')):
                        if (os.path.exists('zip/5/roof_simple_tex3.png')):
                            score1 = PointsTxtrCount('zip/5/roof_simple_tex1.png')
                            score2 = PointsTxtrCount('zip/5/roof_simple_tex2.png')
                            score3 = PointsTxtrCount('zip/5/roof_simple_tex3.png')

                # Наименьший бал за текстуры
                minimal = score1
                if score2 < minimal:
                    minimal = score2
                if score3 < minimal:
                    minimal = score3
                score += minimal
        print(score)
    if i == 6:
        if (os.path.exists('zip/6/roof_lux.obj')):
            if objObjectsCounter('zip/6/roof_lux.obj') == 1:
                score += obj('zip/6/roof_lux.obj', 300)
                # Проверка текстуры
                # 1
                score1 = 0
                score2 = 0
                if (os.path.exists('zip/6/roof_lux_tex1.png')):
                    if (os.path.exists('zip/6/roof_lux_tex2.png')):
                        score1 = PointsTxtrCount('zip/6/roof_lux_tex1.png')
                        score2 = PointsTxtrCount('zip/6/roof_lux_tex2.png')
                # Наименьший бал за текстуры
                minimal = score1
                if score2 < minimal:
                    minimal = score2
                score += minimal
        print(score)
    if i == 7:
        if (os.path.exists('zip/7/roof_booth.obj')):
            if objObjectsCounter('zip/7/roof_booth.obj') == 1:
                score += obj('zip/7/roof_booth.obj', 200)
                # Проверка текстуры
                # 1 2 3
                score1 = 0
                score2 = 0
                score3 = 0
                if (os.path.exists('zip/7/roof_booth_tex1.png')):
                    if (os.path.exists('zip/7/roof_booth_tex2.png')):
                        if (os.path.exists('zip/7/roof_booth_tex3.png')):
                            score1 = PointsTxtrCount('zip/7/roof_booth_tex1.png')
                            score2 = PointsTxtrCount('zip/7/roof_booth_tex2.png')
                            score3 = PointsTxtrCount('zip/7/roof_booth_tex3.png')
                # Наименьший бал за текстуры
                minimal = score1
                if score2 < minimal:
                    minimal = score2
                if score3 < minimal:
                    minimal = score3
                score += minimal
        print(score)
    if i == 8:
        if (os.path.exists('zip/8/window_simple.obj')):
            if objObjectsCounter('zip/8/window_simple.obj') == 1:
                score += obj('zip/8/window_simple.obj', 150)
                # Проверка текстуры
                # 1
                score1 = 0
                if (os.path.exists('zip/8/window_simple_tex1.png')):
                    if textureMainCheck('zip/8/window_simple_tex1.png'):
                        score1 += 1
                        if textureFill('zip/8/window_simple_tex1.png') > 0.65:
                            score1 += 1
                # Наименьший бал за текстуры
                score += score1
        print(score)
    if i == 9:
        if (os.path.exists('zip/9/window_mid.obj')):
            if objObjectsCounter('zip/9/window_mid.obj') == 1:
                score += obj('zip/9/window_mid.obj', 200)
                # Проверка текстуры
                # 1
                score1 = 0
                if (os.path.exists('zip/9/window_mid_tex1.png')):
                    if textureMainCheck('zip/9/window_mid_tex1.png'):
                        score1 += 1
                        if textureFill('zip/9/window_mid_tex1.png') > 0.65:
                            score1 += 1
                # Наименьший бал за текстуры
                score += score1
        print(score)
    if i == 10:
        if(os.path.exists('zip/10/window_lux.obj')):
            if objObjectsCounter('zip/10/window_lux.obj') == 1:
                score += obj('zip/10/window_lux.obj', 300)
                # Проверка текстуры
                # 1
                score1 = 0
                if (os.path.exists('zip/9/window_mid_tex1.png')):
                    if textureMainCheck('zip/10/window_lux_tex1.png'):
                        score1 += 1
                        if textureFill('zip/10/window_lux_tex1.png') > 0.65:
                            score1 += 1
                # Наименьший бал за текстуры
                score += score1

shutil.rmtree("zip")
print(score)




# print(textureMainCheck('zip/1/wall_simple_tex2.png'))

# ОБРАЩЕНИЕ К ФУНКЦИИ
# objObjectsCounter('zip/1/wall_simple.obj')
# objTriangleCount('zip/1/wall_simple.obj')
# objScale('zip/1/wall_simple.obj')
# textureMainCheck('zip/1/wall_simple_tex2.png')
# print(textureFill())
# textureSolidColor
# textureDifference('zip/1/wall_simple_tex2.png', 'zip/1/wall_simple_tex2.png')

# УДАЛИТЬ ПАПКУ
# shutil.rmtree("10")
# os.remove("models.zip")

#
# obj:_______________________________________________
# -кол-во треугольников             +objTriangleCount
# -масштаб                          +objScale
# -кол-во объектов в obj            +objObjectsCounter
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# texture:___________________________________________
# -соотн стрн,степень 2,не > 2048   +textureMainCheck
# -заполненность текстуры(процент)  +textureFill
# -проверка на сплошную картинку    +textureSolidColor
# -проверка двух текстур на отличие +textureDifference
#
