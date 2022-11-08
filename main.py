import random
from constants import *


class Game:

    def __init__(self) -> None:
        self.elements = None
        self.finded = []
        self.lives = [LIFE_SYMBOL for _ in range(LIVES_NUMBER)]
        self.tryed = []

    def build_finded_list(self) -> None:
        n = int(len(self.elements)/3)
        rand = [random.randint(0, len(self.elements)) for _ in range(n)]
        for i, el in enumerate(self.elements):
            if el == ' ' or el == ',' or el == '.' or el == "'" or el == "à" or el == "è" or el == "ì" or el == "ù":
                self.finded.append(el)
                self.tryed.append(el)
            else:
                self.finded.append('_')
            if i in rand:
                self.finded[i] = self.elements[i]

    def check_lives(self) -> bool:
        if len(self.lives) == 0:
            print(
                f"\n{LOSE}\nLa frase da trovare:\n{str(''.join(self.elements)).capitalize()}")
            return True
        return False

    def check_victory(self, phrases: str) -> bool:
        if phrases.lower() == ''.join(self.elements):
            print(
                f"\n{VICTORY}\nLa frase da trovare:\n{phrases.capitalize()}")
            return True
        return False

    def check_tryed(self, letter: str) -> bool:
        if letter not in self.tryed:
            self.tryed.append(letter)
            return True
        else:
            self.lose_life()
            return False

    def lose_life(self) -> None:
        self.lives.pop()

    def check_letter(self, letter: str) -> None:
        if letter in self.elements:
            for i, l in enumerate(self.elements):
                if l == letter:
                    self.finded[i] = letter
        else:
            self.lose_life()

    def read_phrases(self) -> None:
        with open(TEXT_FILE, 'r') as f:
            lists = f.read().splitlines()
        rand = random.randint(0, len(lists)-1)
        self.elements = list(lists[rand].lower())

    def run(self) -> None:
        print(HEADER)
        self.read_phrases()
        self.build_finded_list()
        while True:
            print(
                f"\n\nPossibilità rimanenti ({len(self.lives)}): {str(' '.join(self.lives))}\n")
            print(str(''.join(self.finded)).capitalize())
            letter = input('\ninserisci una lettera o prova la frase:\n')
            if len(list(letter)) > 1:
                if self.check_victory(letter):
                    break
                else:
                    self.lose_life()
            else:
                if self.check_tryed(letter):
                    self.check_letter(letter)
                if self.check_victory(''.join(self.finded)):
                    break
            if self.check_lives():
                break


if __name__ == '__main__':

    def main():
        g = Game()
        g.run()

    main()
