import math
from PIL import Image, ImageDraw, ImageFont
import os


def image_function(i, word, font_size, font_color):
    name = str(i) + ".jpg"
    out_name = word + name
    image = Image.open(name)
    font_type = ImageFont.truetype('Arial.ttf', font_size)
    draw = ImageDraw.Draw(image)
    draw.text(xy=(10, 10), text=(word + str(i)), fill=font_color, font=font_type, stroke_width=round(font_size/50),
              stroke_fill=(255, 255, 255))
    image = image.save('converted/' + out_name)
    print("Image {} is done".format(i))


def make_directory(path):
    try:
        os.mkdir(path)
    except OSError as error:
        print(error)


def save_img(number, folder, word):
    try:
        name = word + str(number) + ".jpg"
        import_name = "converted/" + name
        folderName = str(folder) + "/"
        image = Image.open(import_name)
        filepath = 'processed/' + folderName + name
        image = image.save(filepath)
        print("Image {} is moved successfully".format(number))
    except:
        file.write("image {} has moving error \n".format(number))


def set_prefix():
    global prefix
    pinput = input("Do you want to add a prefix(y/n) : ")
    if pinput == 'y' or pinput == 'Y':
        prefix = input('Enter your prefix : ')
        print('--> prefix set to \'{}\' '.format(prefix))
        if len(prefix) > 5:
            print('--> warning : prefix is too long !!')
            print('--> No prefix ')
            prefix = ""
    else:
        print('--> No prefix ')
        prefix = ''
    return prefix


imageCount = 0
Colors = {"red": (181, 24, 32), "green": (12, 90, 16), "blue": (6, 8, 45), "black": (0, 0, 0)}
file = open('report.txt', 'w+')
start = int(input("Enter starting number : "))
end = int(input("Enter ending number : "))
pr = set_prefix()
make_directory('converted')
print('--> converted folder created successfully')
fontS = int(input("Enter Font Size (50px) : "))
if fontS < 30:
    print("--> Font too small\n--> Font size : 30 ")
    fontS = 30
else:
    print("--> Font size : {} ".format(fontS))
print('Colour list - red | green | blue | black')
inpu = input("Enter Font Colour : ").strip()
if inpu != "red" and inpu != "green" and inpu != "blue" and inpu != "black":
    print("--> Font colour : black ")
    fontC = (0, 0, 0)
else:
    print("--> Font colour : {} ".format(inpu))
    fontC = Colors[inpu]
for i in range(start, end + 1):
    try:
        image_function(i, pr, fontS, fontC)
        imageCount += 1
    except:
        file.write("image {} has error \n".format(i))
inp = input("Do you want to divide images(y/n) : ")
if inp == "Y" or inp == "y":
    currentImg = start
    make_directory('processed')
    print('-> processed folder created successfully')
    folCount = int(input('Enter how many folders : '))
    if folCount > 1:
        for j in range(1, folCount + 1):
            path = 'processed/' + str(j)
            make_directory(path)
            currentImgEnd = int(currentImg + math.floor((end - start + 1) / folCount) - 1)
            for k in range(currentImg, currentImgEnd + 1):
                save_img(k, j, pr)
            currentImg = currentImgEnd + 1
    else:
        print("process terminated ! ")
null_val = input("all done")
file.close()
