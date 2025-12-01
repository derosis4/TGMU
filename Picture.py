import cv2
from PIL import Image
image1 = cv2.imread("image.png")
image = Image.open("image.png")
print(f"высота, ширина, глубина, тип = {image1.shape, image.mode}")
choose = input("Что делаем с картинской:применить к ней эффект(1), сохранить(2)")
if choose == "1":
    choose = input("Какой эффект применить к ней: черно-белое изображение(1), отразить по вертикали(2),отразить по горизонтали(3)")
    if choose == "1":
        for x in range(image.size[0]):
            for y in range(image.size[1]):
                pixel = image.getpixel((x, y))
                avg = (pixel[0] + pixel[1] + pixel[2]) // 3
                image.putpixel((x,y),(avg, avg, avg))
    elif choose == "2":
        for x in range(image.size[0]):
            for y in range(image.size[1]):
                pixel = image.getpixel((-x, y))
                image.putpixel((x,y),(pixel[0] , pixel[1] , pixel[2]))
    elif choose == "3":
        for x in range(image.size[0]):
            for y in range(image.size[1]):
                pixel = image.getpixel((x, -y))
                image.putpixel((x,y),(pixel[0] , pixel[1] , pixel[2]))
    else:
        print("Неверное значение")
    image.show("image.png")
elif choose == "2":
    is_valid = True
    while is_valid:
        image1 = input("Введите название файла: ")
        try:
            image.save(image1)
            print(f"Изображение сохранено как{image1}")
            is_valid = False

        except Exception as e:
            print(f"Ошибка сохранения: {e}, Пожалуйста, введите корректное имя файла")