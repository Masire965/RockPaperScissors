#----------------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1
    for key in questions:
        print("---------------------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter(A, B, C or D): ").upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)

        question_num += 1

    display_scores(correct_guesses,guesses)
#----------------------
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

#----------------------
def display_scores(correct_guesses, guesses):
    print("---------------------")
    print("RESULTS ")
    print("---------------------")
    print("Answers: ", end = " ")
    for i in questions:
        print(questions.get(i), end = " ")
    print()

    print("Guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

#----------------------
def play_again():
    response = input("Do you want to play again?(yes/no): ").upper()
    if response == "YES":
        return True
    else:
        return False
#----------------------
questions = {
    "Who invented AC electrical system?": "B",
    "In 1876, who was awarded the first patent for telephone?": "A",
    "What is the official capital city of Australia?": "C",
    "Who is the author of the classic tragedy play, Romeo and Juliet?": "A"
}
options = [["A.Thomas Edison","B.Nikola Tesla","C.Guglielmo Marconi","D.Wright brothers"],
           ["A.Alexander Graham Bell","B.Elisha Gray","C.Antonia Meucci","D.Guglielmo Marconi"],
           ["A.Sydney","B.Melbourne","C.Canberra","D.Brisbane"],
           ["A.William Shakespeare","B.Charles Dickens","C.Mark Twain","D.Jane Austen"]]
new_game()

while play_again():
    new_game()

print("Byeeee!")


