def day8_1():
    import math

    def paint_calc(height, width, cover):
        cans = (height * width) / cover  # рахуюю кількість банок фарби
        cans = math.ceil(cans)  # заокруглюю до більшого кількість банок
        print(f"You will need {cans} cans of paint")  # видаю кількість банок

    test_h = int(input("Height of wall: "))  # получаю висоту стіни
    test_w = int(input("Width of wall: "))  # получаю ширину стіни
    coverage = 5  # задаю скільки квадратних метрів може пофарбувати банка фарби
    paint_calc(height=test_h, width=test_w, cover=coverage)  # викликаю функцію і задаю параметри


def day8_2():
    def prime_checker(number):
        divided = 1
        prime = True
        for i in range(2, number):
            if number % i == 0:
                divided = i
                prime = False
        if prime:
            print(f"It is a prime number")
        else:
            print(f"It is a not prime number")
            print(f"it is divided into {divided} ")

    n = int(input("Check this number: "))
    prime_checker(number=n)


def day8():
    logo = """           
     ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
    a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
    8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
    "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
     `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
                88             88                                 
               ""             88                                 
                              88                                 
     ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
    a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
    8b         88 88       d8 88       88 8PP""""""" 88          
    "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
     `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
                  88                                             
                  88           
    """
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def caesar(text_code, shift_code, direction_code):
        code_text = ""
        for letter in text_code:
            if alphabet.count(letter) == 1:
                if direction_code == "encode":
                    position = alphabet.index(letter) + shift_code
                    while position > len(alphabet) - 1:
                        position = position - len(alphabet)
                else:
                    position = alphabet.index(letter) - shift_code
                    while position < 0:
                        position = position + len(alphabet)
                code_text += alphabet[position]
            else:
                code_text += letter
        print(f"The encoded text is {code_text}")

    restart = "yes"
    while restart == "no":
        caesar(text, shift, direction)
        restart = input("Do you want to restart the cipher program? yes, or no\n").lower()


day8()
