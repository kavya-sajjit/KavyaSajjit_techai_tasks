#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 20 12:42:53 2025

@author: kavyasajjit
"""

import random

def importing_doc(doc="5_letter_words.txt"):
    arrwords=[]
    with open(doc,"r") as file: 
        for i in file:
            word = i.strip().lower()
            if len(word) == 5 and word.isalpha():
                arrwords.append(word)
                
    return arrwords

def wrd(arrwords):
    return random.choice(arrwords)

def wordle_ans(real,guess): 
    check=[]
    for j in range(5):
        if guess[j] == real[j]:
            check.append("🟩")
            
        elif guess[j] in real:
                    check.append("🟨")
        else:
                    check.append("⬜️")
    return "".join(check)

def gamee_start():
    words=importing_doc()
    print("Loaded", len(words), "words. Example:", words[:10])  # Debugging line
    real=wrd(words)
    rounds=6
    print("Time to begin, you know the drill, what will your 5 letter word be? Beware you only have 6 attempts")
    tries=0
    while tries < rounds:
            guess=input("Enter your word:").lower()
            
            if len(guess)!= 5 or guess not in words:
                print("whoops, that won't work. try another five letter word")
                continue
            result= wordle_ans(real, guess)
            print(result)
            
            if guess==real:
                if tries==0:
                    print("letsgoo, youre a genius (or psychic), tries: ", tries+1)
                else:
                    print("you got it in:",tries +1)
                return #game ends 
            tries=tries +1 
    print("hard luck... the word was:",real)
        
if __name__=="__main__":
    gamee_start()
    