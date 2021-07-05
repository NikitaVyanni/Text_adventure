import random
from Functions import wordprint, titres

class CharactersAndBosses():
#функция характеристик персонажей
    def __init__(self, role, name, job, hobby, hp, damage, level, debuff_type=None, under_debuff=False):
        self.role = role
        self.name = name
        self.job = job
        self.hobby = hobby
        self.hp = hp
        self.dmg = damage
        self.level = level
        self.debuff_type = debuff_type
        self.under_debuff = under_debuff
#функция показа характеристик персонажа
    def introduce_yourself(self):
        wordprint(f'{self.role}')
        wordprint(f'Имя: {self.name}')
        wordprint(f'Работа: {self.job}')
        wordprint(f'Хобби: {self.hobby}')
        wordprint(f'hp: {self.hp}')
        wordprint(f'Урон: {self.dmg}')
        wordprint(f'Уровень: {self.level}')
# функция нанесения урона
    def damage(self, target):
        target.hp -= self.dmg
        wordprint(f'{target.name}, Hp: {target.hp}')

class Character(CharactersAndBosses):
    def damage(self, target):
        super().damage(target)
        if self.under_debuff:
            target.hp = target.hp-target.hp*0.1
            wordprint(f'Прокнуло {target.debuff_type}')

class Boss(CharactersAndBosses):
    # Функция урона
    def damage(self, target):
        super().damage(target)

        debuff_chance = random.randint(1, 1)
        if debuff_chance == 1:
            self.debuff(target)
    # Функция дебафа
    def debuff(self, target):
        target.under_debuff = True
        wordprint(f'{self.name} наложил на вас {self.debuff_type}')
