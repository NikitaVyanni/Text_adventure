# 192 СТР
# Музыка и звуки
import os
import pygame, random, time, sys
from Functions import wordprint, titres, show_inventory, inventory
from Bossfight import boss_fight
from Classes import CharactersAndBosses, Character, Boss
try:
    import pygame
except ModuleNotFoundError:
    print("Библиотека pygame не установлена. Устанавливаю...")
    os.system("pip3 install pygame") # os.system() позволяет выполнить любую системную команду
    import pygame



pygame.mixer.init()
backside_inferno = pygame.mixer.Sound('Soundtracks/text-adventure-musicbackside_t1UWQqb7.mp3')
backside_inferno.set_volume(0.4)

backside_alien = pygame.mixer.Sound("Soundtracks/Text-adventure-1_Jt844aCw.mp3")
backside_alien.set_volume(0.6)

pygame.mixer.Sound('Soundtracks/Among_us.mp3').play()
time.sleep(4)
mk_sound = pygame.mixer.Sound('Soundtracks/Mk.mp3')
mk_sound.set_volume(0.3)
mk_sound.play()
try:
    while True:
        wordprint('Выберите персонажа:')
        wordprint('1) Аберфорт Дамблдор')
        wordprint("2) Алан 'ДАТЧ' Шеффер")
        wordprint("3) Канеки Кен-кун")

        choice_character = int(input())
        if choice_character == 1:
            # Аберфорт
            character = Character('Перс', 'Аберфорт', 'брат Альбуса', 'сидеть', 67, 295, '3')
        if choice_character == 2:
            # Алан Датч Шеффер
            character = Character('Перс', 'Алан "ДАТЧ" Шеффер', 'Шварц', 'Убивать хищника', 145, 140, '11\10 (он же Шварц пффф...)')
        if choice_character == 3:
            # Канеки Кен-кун
            character = Character('Перс', 'Канеки Кен-кун', 'в Антейку', 'пить кофе', 100, 100, "12\10 (он же Канеки Кен-кун пффффффффффффффф...)")
        character.introduce_yourself()
        mk_sound.fadeout(3000)
        time.sleep(3)
        backside_inferno.play(-1)

        wordprint("Вы стоите перед двумя пещерами")
        wordprint("1)Войти в правую пещеру")
        wordprint("2)Войти в левую пещеру")
        cave = int(input())

        good_cave = random.randint(1, 1)#отрубать плохую пещеру СДЕСЬ

        if cave == good_cave:
            #Выбор сундука
            wordprint("Вы в водопаде. Перед вами 3 сундука.")
            wordprint("1) Выбрать первый сундук.")
            wordprint("2) Выбрать второй сундук.")
            wordprint("3) Выбрать третий сундук.")
            bad_chest = random.randint(2, 2)#отрубать мимика СДЕСЬ
            chest = int(input())
            # Мимик
            if chest == bad_chest:
                wordprint("На вас напал мимик. Конец.")
                titres()

            if chest != bad_chest:
                trashure = random.randint(2, 2)#отрубать подземелье СДЕСЬ
                first_time_here = 'yes'
                while True:
                    if trashure == 1:
                        if first_time_here == 'yes':
                            wordprint("Вы нашли клад.")
                            inventory.append('1_клад')
                            wordprint('Ваш инвентарь:')
                            show_inventory()
                            # ветка ада
                        wordprint("Вы идёте дальше. Перед вами река. Рядом с ней стоит человек с лодкой.")
                        wordprint("1) Спросить у человека с лодкой, может ли он вас перевезти.")
                        wordprint("2) Попробовать переплыть реку.")
                        river = int(input())
                        if river == 1:
                            wordprint("Человек с лодкой просит вас ему заплатить за переправу.")
                            wordprint("1) Заплатить.")
                            wordprint("2) Отказать.")
                            price = int(input())
                            if "1_клад" not in inventory:
                                price = 2
                            if price == 1:
                                wordprint("Человек взял с вас плату и переправил через реку. Вы оказались в аду. Вас встречает проводник.")
                                wordprint("1) Пойти с проводником.")
                                wordprint("2) Пойти без проводника.")
                                guide = int(input())
                                if guide == 1:
                                    wordprint("Вы прошли с проводником по всем 9 кругам \"ad international\", оставьте отзыв пожалуйста.")
                                    review = input()


                                    # Боссфайт. Начало.
                                    #характеристики первого босса
                                    lucifer = Boss('Босс', 'Люцифер', 'владыка ада', 'играть в карты с Иудой', 1000, 66.6, 1, "горение")
                                    boss_fight(lucifer, 'IA', character)

                                # фейлы
                                if guide == 2:
                                    wordprint("Демоны первого круга приняли вас за грешника. Теперь вы вечно скорбите. Конец.")
                                    titres()
                            if price == 2:
                                wordprint("Человек отказал вам в переправе.")
                                river = 2
                                wordprint("Вам нечем заплатить за переправу.")
                                titres()
                        if river == 2:
                            wordprint("Вы попробовали переплыть реку и всё забыли. Конец.")
                            titres()

                    if trashure == 2:
                        wordprint("Вы нашли проход в подземелье.")
                        wordprint("1)Спустится в подземелье.\n2)Пройти вглубь пещеры.")
                        choice = int(input())

                        if choice == 1:
                            wordprint("Вы оказались в подземелье, полном магических существ.")
                            wordprint("1)Пойти к гиппогрифам.")
                            wordprint("2)Пойти к нарлам.")
                            fantastic_beasts=int(input())
                            if fantastic_beasts == 1:
                                wordprint("1)Поклониться.")
                                wordprint("2)Не кланяться.")
                                bow=int(input())
                                if bow == 1:
                                    wordprint("1)Полететь на гиппогрифе.")
                                    wordprint("2)Пойти дальше.")
                                    gippogrif = int(input())
                                    # ветка Гарри Поттера
                                    if gippogrif == 1:
                                        wordprint("Гиппогриф прилетел к визжащей хижине.")
                                        wordprint("1)Пойти в хижину.")
                                        wordprint("2)Идти к Хогвартсу.")
                                        shrieking_hut = int(input())
                                        if shrieking_hut == 1:
                                            wordprint("Вы в визжащей хижине.")
                                            wordprint("1) Пойти по тайному ходу в Хогвартс.")
                                            wordprint("2) Остаться переночевать.")
                                            night = int(input())
                                            if night == 1:
                                                wordprint("Вы в Хогвартсе. Куда вы пойдёте?")
                                                wordprint("1) Выручай-комната.")
                                                wordprint("2) Кабинет Дамблдора.")
                                                if shrieking_hut == 1:
                                                    wordprint("Напомни, а как пройти к выручай комнате?")
                                                    wordprint("1) В коридоре третьего этажа.")
                                                    wordprint("2) В коридоре восьмого этажа.")
                                                    helproom = int(input())
                                                    if helproom == 1:
                                                        wordprint("Шо, не фан чтоли?")
                                                        wordprint("Вас попрали рил-фэны. Конец.")
                                                        titres()
                                                    if helproom == 2:
                                                        wordprint("А поподробнее?")
                                                        wordprint("1) Надо три раза пройти по коридору, думая о помощи.")
                                                        wordprint("2) Всм?")
                                                        particular = int(input())
                                                        if particular == 1:
                                                            wordprint("Фига ты умный. Молодес)))")
                                                            wordprint("Вы в выручай-комнате. А теперь второй фан-тест!")
                                                            wordprint("Какой отряд тренировался в этой комнате?")
                                                            wordprint("1) Отряд Дамблдора.")
                                                            wordprint("2) Отряд Сириуса Блэка.")
                                                            wordprint("3) Отряд Феникса.")
                                                            test = int(input())
                                                            if test == 1:
                                                                wordprint("Да, следующий вопрос!")
                                                                wordprint("Какому факультету принадлежал крестраж диадема?")
                                                                wordprint("1) Гриффендору.")
                                                                wordprint("2) Пуффендую.")
                                                                wordprint("3) Когтеврану.")
                                                                wordprint("4) Слизерину.")
                                                                hogwarts = int(input())
                                                                if hogwarts == 3:
                                                                    wordprint("Вы выиграли ААААААВТОМОБИИИИЛЬ. Последний вопрос.")
                                                                    wordprint("Как раньше звали Лорда Волан-де-Морта?")
                                                                    wordprint("1) Том Марволо Реддл.")
                                                                    wordprint("2) Ньют Саламандр.")
                                                                    wordprint("3) Геллерт Грин-де-Вальд.")
                                                                    lord = int(input())
                                                                    if lord == 1:
                                                                        wordprint("Вот он.")
                                                                        lord_vol_de_mort = Boss('Босс', 'Лорд Волан-де-Морт', 'Тёмный Лорд', 'Наводить суету в Хогвартсе', 2500, 100, 1, "горение")
                                                                        boss_fight(lord_vol_de_mort, "HP", character)
                                                                    else:
                                                                        wordprint("Нет. Конец.")
                                                                        titres()
                                                            if test == 2:
                                                                    wordprint("Нет. Конец")
                                                                    titres()
                                                        if particular == 2:
                                                            wordprint("В прямом. Конец.")
                                                            titres()
                                            if night == 2:
                                                wordprint("Мне было лень делать эту ветку, так что конец.")
                                                time.sleep(1)
                                                wordprint("Просто конец.")
                                                time.sleep(0,5)
                                                wordprint("Ээээм...")
                                                time.sleep(2)
                                                wordprint("Конец?")
                                                titres()


                                        if shrieking_hut == 2:
                                            wordprint("Вас схватили дементоры. Конец.")
                                            titres()

                                    # ветка Хищника
                                    if gippogrif == 2:
                                        wordprint("Гиппогрифы привели вас к космическому кораблю в лесу.")
                                        backside_inferno.fadeout(3500)
                                        time.sleep(3.5)
                                        pygame.mixer.Sound('Soundtracks/zvuk-hischnika.mp3').play()
                                        time.sleep(8)
                                        backside_alien.play(-1, fade_ms = 3500)
                                        wordprint("1) Зайти в корабль.")
                                        wordprint("2) Не заходить.")
                                        ship = int(input())
                                        if ship == 1:
                                            wordprint("Перед вами загадка с двоичным кодом.")
                                            wordprint("Правила игры:")
                                            wordprint("Переведите данное число из 10-ичной СС в 2-ичную СС.")
                                            random_number = random.randint(1, 10)
                                            print(random_number)
                                            answer = input()
                                            if answer == format(random_number, 'b'):
                                                wordprint("Молодец.")
                                                wordprint("Маршрут построен.")
                                                wordprint("Вы прилетели на базу хищников.")
                                                wordprint("Хищники дали вам выбор:")
                                                wordprint("1)Сразиться с Чужим.")
                                                wordprint("2)Сбежать.")
                                                aliens = int(input())
                                                if aliens == 1:
                                                    alien = Boss("Босс", "Чужой", "Пугать людей", "Драться с Хищником", 600, 80, 2, "Отравление")
                                                    boss_fight(alien, 'AvP', character)
                                                if aliens == 2:
                                                    wordprint("Вы сбежали с базы хищников. Теперь вы не сможете снова туда вернуться.")
                                                    wordprint(f"{character.name} was an Imposter")
                                                    wordprint("Хищники захватили вашу планету.")
                                                    wordprint("Какая ваша любимая карта в Among Us?")
                                                    wordprint("1) Skeld")
                                                    wordprint("2) Polus")
                                                    wordprint("3) Mira HQ")
                                                    map = int(input())
                                                    if map == 1:
                                                        wordprint("Вы прожили остаток жизни на Mira HQ.")
                                                    if map == 2:
                                                        wordprint("Вы прожили остаток жизни на Skeld.")
                                                    if map == 3:
                                                        wordprint("Вы прожили остаток жизни на Polus.")
                                                    wordprint("Конец. Achievement LoL complete.")
                                                titres()
                                            else:
                                                wordprint("Не молодец. Конец.")
                                                titres()
                                if bow == 2:
                                    wordprint("Вы разозлили гиппогрифов. Конец.")
                            if fantastic_beasts == 2:
                                wordprint("Конец.")
                            break

                        if choice == 2:
                            trashure = 1
                        first_time_here = 'no'

        if cave != good_cave:
            wordprint("Вы упали. Конец.")
            titres()


except ValueError:
    wordprint("Технические неполадки.")
except KeyboardInterrupt:
    wordprint("\nИди паспи.")

#
# Дальше по сюжету.
# 1)по ветке ада
# Там если персонаж выбирет "пройти с проводником", то он проходит дальше по 9 кругам ада и встречается с {self.name}ом. Там {self.name} ему говорит типа тебя зовут так-то, ты кто-то,и пришёл к пещерам за тем-то, а потом сбрасывает его в бесконечную яму за все его грехи в прошлом и блаблабла.
# Так мы сливаем концовку в аду. В конце пишем не "конец.", а что-то типа "achievement complete. IA (inferno achievement)"
#СЛИТО
# 2)по ветке подземелья
# Если мы ЛЕТИМ на гиппогрифе, то прилетаем в Хогсмит, там будет что-то с дементорами или оборотнями или ревущей хижиной, а может со всем, и там мы должны попасть к выручай-комнате, чтобы узнать, что мы вообще такое. НО. Нас никто не дольжен видеть, потому что нас могут принять за Сириуса Блэка, на которого идёт охота.
# Когда мы попадаем в выручай комнату, там будет "игра в спички" с манекеном для тренировок, если мы выигрываем, комната рассказывает кто и что мы вообще такое, вообщем, тоже что и {self.name}. А ДАЛЬШЕ, уже вопрос, продолжать ветку или нет, потому что как в случае с адом, тупиковой она не кажеться. это решим позже.
# 3)Если мы ИДЕМ ДАЛЬШЕ, то выходим в лес, с инопланетным кораблём. Там будет загадка с "кубиком 3на3". Выигрываем, летим на базу хищников, дальше линия с чужним(точнее боем с ним) и в итоге мы-лидер хищников, и они нам рассказывают, кто и что мы такое. Это явно тупиковая линия, по этому там будет писаться не "конец.", а что-то типа "AvP achievement complete. AWPa."
#СЛИТНО
# ДЛЯ ИДЕЙ:
# виселица, угадай-ка, переведивдвоичнуюсистему-ка, спички
# титры с отзывом и последними словами (сделать отдельный файл)
# особые предметы
# отрицательные эффекты
