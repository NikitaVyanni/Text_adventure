# функция боссфайта
import time, random, pygame
from Functions import wordprint, titres, show_inventory, inventory
from Classes import Character, Boss, CharactersAndBosses

def fight(boss, achievement, character):
    while boss.hp >= 0 and character.hp >= 0:
        wordprint("Cколько ударов вы нанесёте?")
        punch = int(input())
        if punch < 0:
            for i in range(-punch):
                time.sleep(1)
                wordprint(f'{boss.hp}, ошибка')
                boss.hp += character.dmg
        elif punch <= 3:
            for i in range(punch):
                character.damage(boss)
        elif punch:
            wordprint(f'Ваш шанс на попадание: 1/{punch}')
            wordprint("Удачи!")
            for i in range(punch):
                time.sleep(1.5)
                hit_chance = random.randint(0, punch)
                if hit_chance == 1:
                    wordprint("Есть пробитие!")
                    character.damage(boss)
                else:
                    wordprint('Ой, не попал')
        wordprint(f"Босс ударил вас. -{boss.dmg} hp")
        boss.damage(character)
    if character.hp <= 0:
        wordprint("Better luck next time.")
    elif boss.hp <= 0:
        wordprint(f"Congratulations! Achievement {achievement} complete")
    titres()

pygame.mixer.init()
def boss_fight(boss, achievement, character):
    wordprint("Вы прошли в коридор ведущий к доджу с боссом.")
    wordprint("У вас будет 30 секунд на ответ.")
    wordprint("Выберите один из вариантов ответов исплользуя кнопки 1, 2 или 3.")
    worldtime = time.time()
    n = 0
    question1, question2, question3 = '', '', ''
    while n == 0:
        wordprint('Кто не учавствовал в отечественной войне 1812 года?')
        wordprint("1) Наполеон Бонапарт")
        wordprint("2) Михаил Кутузов")
        wordprint("3) Александр II")
        question1 = int(input())
        if time.time() > worldtime + 30:
            wordprint("Время вышло. Конец.")
            titres()
        elif question1 != 3:
            wordprint("Вы проиграли. Пройдите к доджу с боссом.")
            break

        wordprint("Столица Древнего Египта")
        wordprint("1) Мемфис")
        wordprint("2) Карфаген")
        wordprint("3) Каир")
        question2 = int(input())
        if time.time() > worldtime + 30:
            wordprint("Время вышло. Конец.")
            titres()
        elif question2 != 1:
            wordprint("Вы проиграли. Пройдите к доджу с боссом.")
            break

        wordprint("Своё государство жители Китая называли:")
        wordprint("1) Непобедимая империя")
        wordprint("2) Благородная империя")
        wordprint("3) Поднебесная империя")
        question3 = int(input())
        if time.time() > worldtime + 30:
            wordprint("Время вышло. Конец.")
            titres()
        elif question3 != 3:
            wordprint("Вы проиграли. Пройдите к доджу с боссом.")
            break
        # Заставляет цикл сработать только один раз
        n = 1

    if (question1, question2, question3) == (3, 1, 3):
        if time.time() < worldtime + 30:
            # призы (в зависимости от персов)
            if character.name == "Аберфорт Дамблдор":
                wordprint("Вы выиграли: Мантия-невидимка")
                inventory.append("2_Мантия-невидимка")
                character.hp += 100
                wordprint("hp+100")
            elif character.name == "Алан 'Датч' Шеффер":
                wordprint("Вы выиграли: НПП (наплечная плазменная пушка)")
                inventory.append("2_НПП")
                character.dmg += 100
                wordprint("dmg+100")
            elif character.name == "Канеки Кен-кун":
                wordprint("Вы выиграли: куинке")
                inventory.append("2_куинке")
                print(character.dmg)
                character.dmg += 150
                wordprint("dmg+150")
            show_inventory()


    boss.introduce_yourself()
    character.introduce_yourself()
    wordprint("Вы находитесь в додже, аккуратно, скользкий пол.")
    wordprint("1) Посмотреть направо.")
    wordprint("2) Посмотреть налево.")
    wordprint("3) Посмотреть вверх.")
    wordprint("4) Посмотреть вперёд.")
    bossfight1_question1 = int(input())
    if bossfight1_question1 == 1:
        wordprint("Босс ударил вас. GG.")
        titres()
    if bossfight1_question1 == 2:
        wordprint("Босс попробовал взять вас рукой.")
        wordprint("Что будете делать?")
        wordprint("1) Уклониться.")
        wordprint("2) Попробовать уклониться.")
        bossfight1_question2 = int(input())
        if bossfight1_question2 == 1:
            wordprint("Ты даже не попробовал?")
            boss.damage(character)
            print(character.hp)
            titres()
        if bossfight1_question2 == 2:
            wordprint("Вы уклонились.")
            wordprint("1) Контратаковать.")
            wordprint("2) Уйти в защиту.")
            bossfight1_final_question = int(input())
            if bossfight1_final_question == 1:
                wordprint("Успешная контратака.")
                fight(boss, achievement, character)

            if bossfight1_final_question == 2:
                wordprint("Вы отлетели на обрыв. Ваши последние слова?")
                last_words = input()

                if character.name == "Канеки Кен-кун":
                    last_words = input()
                    wordprint(f"{boss.name} сбил вас в пропасть.")
                    wordprint("1) Упасть.")
                    wordprint("2) Включить режим читов.")
                    cheatmode = input().lower()
                    if cheatmode == "включить режим читов" or cheatmode == "2":
                        wordprint("РЕЖИМ ЧИТОВ ВКЛЮЧЕН!!!")

                        character = Character('Dark Peasant', 'Бафнутый Канеки', 'в Оагири', 'нет, работает по профессии', 200, 200, 'ドナー')
                        character.introduce_yourself()

                        omae_wa = pygame.mixer.Sound('Soundtracks/omae_wa.mp3')
                        omae_wa.set_volume(0.4)
                        omae_wa.play()
                        fight(boss, achievement, character)
                        # wordprint("Вы включили режим читов. Ударить босса?")
                        # while boss.hp > 0 and character.hp > 0:
                        #     wordprint("1)Ударить")
                        #     wordprint("2)Выждать")
                        #     falcon_punch = int(input())
                        #     if falcon_punch == 1:
                        #         wordprint("Вы ударили босса ударом сокола.")
                        #         character.damage(boss)
                        #         if boss.hp < 0:
                        #             wordprint(f"Congratulations! Achievement {achievement} complete")
                        #     if falcon_punch == 2:
                        #         wordprint("Не тормози, сникерсни!")
                        #         boss.damage(character)
                        #         if character.hp < 0:
                        #             wordprint("You lose. GG")
                        titres()
                else:
                    wordprint(f"{boss.name} сбил вас в пропасть.")
                    titres()

        if bossfight1_question1 == 3:
            wordprint("Слишком банально. Банальный вопрос требует банальных решений.")
            boss.damage(character)

        if bossfight1_question1 == 4:
            wordprint("Босс зашёл вам за спину. Почти угадали.")
            boss.damage(character)
