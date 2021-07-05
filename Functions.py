#функция побуквенного письма
import time, sys, pygame
def wordprint(line):
    for i in line:
        print(i, end='', flush=True)
        time.sleep(0.001)
    print()
#функция титров
def titres():
    pygame.mixer.stop()
    pygame.mixer.Sound("Soundtracks/dark-souls-_you-died_-sound-effect-from-youtube.mp3").play()
    time.sleep(7)
    sys.exit()

# Функция инвентаря
inventory = []
def show_inventory():
    for i in inventory:
        print(i)
