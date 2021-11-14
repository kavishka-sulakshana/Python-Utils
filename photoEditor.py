import math

from PIL import Image, ImageDraw, ImageFont
import os


def image_function(i):
    name = str(i) + ".jpg"
    image = Image.open(name)
    font_type = ImageFont.truetype('Arial.ttf', 50)
    draw = ImageDraw.Draw(image)
    draw.text(xy=(10, 10), text=str(i), fill=(0, 0, 0), font=font_type, stroke_width=1, stroke_fill=(255, 255, 255))
    image = image.save('converted/' + name)
    print("Image {} is done".format(i))


def make_directory(path):
    try:
        os.mkdir(path)
    except OSError as error:
        print(error)


def save_img(number, folder):
    try:
        name = str(number) + ".jpg"
        import_name = "converted/" + name
        folderName = str(folder) + "/"
        image = Image.open(import_name)
        filepath = 'processed/' + folderName + name
        image = image.save(filepath)
        print("Image {} is moved successfully".format(number))
    except:
        file.write("image {} has moving error ".format(number))


imageCount = 0
file = open('report.txt', 'w+')
start = int(input("Enter starting number : "))
end = int(input("Enter ending number : "))
make_directory('converted')
print('-> converted folder created successfully')
for i in range(start, end + 1):
    try:
        image_function(i)
        imageCount += 1
    except:
        file.write("image {} has error ".format(i))
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
            currentImgEnd = int(currentImg + math.floor((end - start + 1) / folCount)-1)
            for k in range(currentImg, currentImgEnd+1):
                save_img(k, j)
            currentImg = currentImgEnd + 1
    else:
        print("process terminated ! ")
null_val = input("all done")
file.close()
