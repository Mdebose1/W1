import random

def show_directions():
    print("Try to guess the word by choosing letters to fill in the blanks. You get 7 guesses. If you guess correctly, you win.")
# guesses = ()
wrong_guesses = (7)

word_list = ["bookcase", "Texas", "island", "magaizne", "bicycle", "margarita"]

done=False
while not done:
    word = random.choice(word_list)

    no_words = []
    for i in word:
     no_words.append("_")
     print(no_words)

    if no_words not in word:
         no_words -= 1
        
 
    if no_words == 0:
     print("You got it!")

    done = False
while not done:
        print(no_words)
    
letter_to_guess = input("What letter would you like to choose?")
    # print(letter_to_guess) 
if wrong_guesses == 0:
        done == True
        print("Game Over. Thank you for playing.")
        
        
for i, letter in enumerate(word):
        if letter == letter_to_guess:
            # print(i, letter)
            no_words[i] = letter

#     for letters in word:
#      if letters.lower not in word:
#         print("_", end ='')
#     else: 
#         print("_", end ='')

#         guesses = (len(word))
#         guesses=guesses.lower()
#         if guesses.lower() not in word:
#                     wrong_guess -= 1
#                     if wrong_guess == 0:
#                         done = True
# if done == True:
#     print("JJJJJJJ")


# guess = "suns"
# from re import U
# word_to_guess = list(guess)

# no_words = []
# for i in word_to_guess:
#     no_words.append("_")
# print(no_words)
    
# letter_to_guess = input("What letter would you like to choose?")
# # print(letter_to_guess) 

# for i, letter in enumerate(guess):
#     if letter == letter_to_guess:
#         # print(i, letter)
#         no_words[i] = letter
# print(no_words)
    # if done:
    #     print("So sorry! The word was 'word'")
    # else:
    #     print("Congratulations! You got it!")


    



# for letters in word_list:
        




# print(random.choice(word_list))
