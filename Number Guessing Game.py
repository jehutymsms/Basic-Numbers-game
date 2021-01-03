#This is one of the simple python projects yet an exciting one. 
# You can even call it a mini-game. Make a program in which the computer randomly 
# chooses a number between 1 to 10, 1 to 100, or any range. 
# Then give users a hint to guess the number. 
# Every time the user guesses wrong, he gets another clue, and his score gets reduced. 
# The clue can be multiples, divisible, greater or smaller, or a combination of all.
#You will also need functions to compare the inputted number with the guessed number, 
# to compute the difference between the two, 
# and to check whether an actual number was inputted or not in this python project.
import random
import time

def get_name():
    res =input("What is your name? ")
    return res

def question_game():
    res = input("Would you like to play a game? Y/N " )
    ye = ["Y", "yes", "y", "Yes"]
    ne = ["N", "No", "n", "no"]
    if res in ye:
        print("Awesome Lets play a number guessing game!!!")
        time.sleep(1)
        return game1()
    if res in ne:
        print("I am sorry to hear that. It was a pleasure to meet you. Goodbye")
    else:
        print("I am sorry. I am only programmed to except the responses listed.")
        question_game()
counter = 100 
def game1():
    number = random.randint(1 , 10)
    def game2():
        global counter
        print("Score = " + str(counter))
        if counter >= 0:
            respon = input("I have choosen a number between 1 and 10. What is your guess? ")
            try:
                respo = int(respon)
            except ValueError:
                print("I am sorry. I am only programmed to except whole numbers as a response. Try again") 
                game2()
            else:
                respo = int(respon)
                if respo == number:
                    print("YOU GOT IT!!! You scored " + str(counter) + " points.")
                elif respo <= number:
                    print("Your too low guess higher.")
                    counter -= 10
                    game2()
                elif respo >= number:
                    print("Your too high guess lower.")
                    counter -= 10
                    game2()  
    if counter == 0:
        game2()
    elif counter > 0:
        game2()   

def game_rules():
    print("Hello my name is Ada")

    name = get_name()

    print("Hello " + name + " it is a pleasure to meet you.")
    time.sleep(2)
    question_game()
game_rules()


