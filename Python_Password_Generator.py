
import random

class PasswordGenerator:

    def __init__(self,randNum1,randNum2,randNum3,randNum4,randNum5,randNum6,randNum7,randNum8):
        self.randNum1 = randNum1
        self.randNum2 = randNum2
        self.randNum3 = randNum3
        self.randNum4 = randNum4
        self.randNum5 = randNum5
        self.randNum6 = randNum6
        self.randNum7 = randNum7
        self.randNum8 = randNum8

    def createPassword(self):
        characters= ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k','m',
                     'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I',
                     'J', 'K', 'M', 'N', 'O','p', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','@', '#', '$','%', '=', ':',
                     '?', '.', '/', '|', '~', '>','*', '(', ')']
        print(str(characters[self.randNum1])+str(characters[self.randNum2])+str(characters[self.randNum3])+str(characters[self.randNum4])+
              str(characters[self.randNum5])+str(characters[self.randNum6])+str(characters[self.randNum7])+str(characters[self.randNum8]))













pg = PasswordGenerator(random.randint(0,74),random.randint(0,74),random.randint(0,74),random.randint(0,74),random.randint(0,74),random.randint(0,74),random.randint(0,74),random.randint(0,74))
pg.createPassword()
