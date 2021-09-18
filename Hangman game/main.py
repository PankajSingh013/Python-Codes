#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import words
import logos
from IPython.display import clear_output


# In[ ]:



print(logos.logo)
print('------------------------------------------------')
#Step 1
#word_list = ["aardvark", "baboon", "camel"]

#choose a random word
choosen_word= random.choice(words.words)
print('word is :',choosen_word)

#create an empty list and assing '_' to each position
display=[]
word_length=len(choosen_word)
for i in range(word_length):
    display+='_'
print(display)

lives=6
end_of_game=False
while not end_of_game:
    #take input guess from user
    guess=input("Guess the letter: ").lower()
    clear_output()
    
    if guess in display:
        print(f'You already guessed corrctly letter {guess}')
    
    #check if guess is correct or not. IF correct replace the '_' with the guess letter
    for position in range(word_length):
        letter=choosen_word[position]
        if letter == guess:
            display[position]=guess
    
    print('----------------')
    print(display)
    
    if guess not in choosen_word:
        lives-=1
        print(f'You already guessed {guess} which is not in final word list. {lives} left out of 6')
        if lives==0:
            end_of_game=True
            print("You Lose :( ")
    
    
    if '_' not in display:
        end_of_game=True
        print('You Win')
    
    print(logos.stages[lives])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




