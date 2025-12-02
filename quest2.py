class Person:
    def __init__(self, name, attempt=2, knowledge=0):
        self.name = name
        self.attempt = attempt
        self.knowledge = knowledge
        self.reward_given = False

    def decrease_attempt(self, amount):
        self.attempt -= amount
        print(f"Количество попыток уменьшилось на {amount}. Осталось {self.attempt}")

    def increase_knowledge(self, amount):
        self.knowledge += amount
        print(f"Количество баллов увеличилось на {amount}.")

    def give_reward(self):
        if not self.reward_given and self.knowledge >= 2:
            print(f"Поздравляем, {name}! Дарим вам диплом победитля нашей викторины.")
            self.reward_given = True
            exit()

def geography():
    try:
        while person.attempt > 0:
            print("Хорошо, ответьте на вопрос!")
            answer = input("Самая полноводная река в России: Енисей(1), Амазонка(2), Лена(3)?")

            if not answer.isdigit() or int(answer) not in [1, 2, 3]:
                raise ValueError("Необходимо ввести целое число от 1 до 3!")

            if answer == '2':
                print("Да вы Правы!")
                person.increase_knowledge(1)
                geography_bonus()
            elif answer == '1':
                print("Нет!")
                person.decrease_attempt(1)
            elif answer == '3':
                print("Нет!")
                person.decrease_attempt(1)

            repeat = input("Хотите ответить на вопрос ещё раз?(да/нет):")
            if repeat.strip().lower() != 'да':
                print("В другой раз!")
                break
        else:
            print("У вас закончилилсь попытки!")
    except Exception as err:
        print(f"Произошла ошибка: {err}")

def geography_bonus():
    try:
        print("Дополнительный вопрос по Географии!")
        answer = input("Самая маленькая страна в мире: Ватикан(1), Бахрейн(2), Лихтинштейн(3)?")

        if not answer.isdigit() or int(answer) not in [1, 2, 3]:
            raise ValueError("Необходимо ввести целое число от 1 до 3!")

        if answer == '1':
            print("Да вы правы!")
            person.increase_knowledge(1)
            person.give_reward()
        else:
            print("Ответ неверный.")
            person.decrease_attempt(1)
    except Exception as err:
        print(f"Произошла ошибка: {err}")

def chemistry():
    try:
        while person.attempt > 0:
            print("Хорошо, ответьте на вопрос!")
            answer = input("В каком состоянии не может находится C02: жидком(1), твердом(2), Газообразном(3)?")

            if not answer.isdigit() or int(answer) not in [1, 2, 3]:
                raise ValueError("Необходимо ввести целое число от 1 до 3!")

            if answer == '1':
                print("Да!")
                person.increase_knowledge(1)
                geography_bonus()
            elif answer == '2':
                print("Нет!")
                person.decrease_attempt(1)
            elif answer == '3':
                print("Вы серьёзно?!")
                person.decrease_attempt(1)

            repeat = input("Хотите ответить на вопрос ещё раз ?(да/нет):")
            if repeat.strip().lower() != 'да':
                print("В другой раз")
                break
        else:
            print("У вас закончилсь попытки!")
    except Exception as err:
        print(f"Произошла ошибка: {err}")
print("Приветствуем в нашей викторине!")
name = input("Введите ваше имя:")
person = Person(name)

enter = input("Желаете присоединиться (да/нет)?")

if 'да' == enter:
    print(f"Добро пожаловать, {name}!")

    answer = input("По какой тематике вы хотите выбрать вопрос: География(1), Химия(2), История(3)?")

    if not answer.isdigit() or int(answer) not in [1, 2, 3]:
        raise ValueError("Необходимо ввести целое число от 1 до 4!")

    if answer == '1':
        geography()
    elif answer == '2':
        chemistry()
    elif answer == '3':
        print("Извините мы не успели составить вопросы по истории!")
elif 'нет' == enter:
    print("Ждем вас в следющем году!")