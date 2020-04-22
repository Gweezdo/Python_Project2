elements_file = open("elements1_20.txt", 'r')

elem_list = []

temp = elements_file.readline().strip().lower()

while temp:
    elem_list.append(temp)
    temp = elements_file.readline().strip().lower()

elements_file.close()

def get_names():

    print("List any 5 of the first 20 elements in the Period table")
    

    guess_list = []

    while len(guess_list) < 5:
        guess = input("Enter the name of an element: ").lower()
        if guess.isalpha():
            if guess in guess_list:
                print("Sorry, " + "\"" + guess.title() + "\"" + " was allready entered")
            else:
                guess_list.append(guess)
        elif guess.isdigit():
            print("Sorry, guess is digit, please try again")
        else:
            print("\"" + guess + "\"" + " is not alphabetical, please try again")

    return guess_list

guess_list = get_names()
correct_list = []
incorrect_list = []

for i in range(len(guess_list)):

    if guess_list[i] in elem_list:
        correct_list.append(guess_list[i].title())

    else:
        incorrect_list.append(guess_list[i].title())

score = len(correct_list) * 20

print(str(score) + "% Correct\n" + "Found: " + str(correct_list) + "\n" + "Not found: " + str(incorrect_list), end="")