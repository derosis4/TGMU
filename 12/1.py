
class NotInplenetedExeptions(Exception):
    ...
def human_spider():
    while True:
        print("Отлично, выберете место!")
        answer = input("Свободные места: 2-2(1), 8-4(2), 9-16(3)")
        if 1 <= int(answer) <= 3:
            if answer == '1':
                print("Отлично, приятного просмотра!")
            elif answer == '2':
                print("Отлично, приятного просмотра!")
            elif answer == '3':
                print("сломано сиденье")
                repeat = input("Выберете другое место")
                if repeat.strip() == 'нет':
                    print("До свидания, будем ждать")
                    break
                elif repeat.strip() == '1':
                    print("Отлично, приятного просмотра!")
                    break
                elif repeat.strip() == '2':
                    print("Отлично, приятного просмотра!")
                    break
        else:
            raise NotInplenetedExeptions("нужно ввести цифру от 1 до 3")
def brother():
    print("Отлично, выберете место!")
    choose = input("Свободные места: 1-8(1), 5-5(2), 7-2(3)")
    if 1 <= int(choose) <=3:
        if choose == '1':
            print("Отлично, приятного просмотра!")
        elif choose == '2':
            print("Отлично, приятного просмотра!")
        elif choose == '3':
            print("Отлично, приятного просмотра!")
    else:
        raise NotInplenetedExeptions("нужно ввести цифру от 1 до 3")
print("Здравстуйте,Добро пожаловать в нашем кинатеатре!")

enter = input ("Желайте зайти?(да/нет)")

if 'да' == enter:
    print("Добро пожаловать")
    choose = input("В какой кино пойдете:человек паук(1), Оно(2), Брат(3)")
    if 1 <= int(choose) <=3:
        try:
            if '1' == choose:
                human_spider()
            elif choose == '2':
                raise NotInplenetedExeptions("""Извините, закончились билеты""")
            elif choose == '3':
                brother()
        except NotInplenetedExeptions as e:
            print(f"{e}")
    else:
        raise NotInplenetedExeptions("нужно ввести цифру от 1 до 3")
elif 'нет' == enter:
    print("До свидания, будем ждать")
else:
    raise NotInplenetedExeptions("Ответ либо да, либо нет")


