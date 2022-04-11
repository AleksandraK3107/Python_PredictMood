# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 19:32:33 2021

"""

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer    
import tkinter

# stworzenie okna tkinter
fen = tkinter.Tk()
fen.geometry("430x200")

def action():
    sid_obj = SentimentIntensityAnalyzer()
 
    sentiment_dict = sid_obj.polarity_scores(entry1.get())
     
    # przewidywanie, czy zdanie/slowo jest pozytywne, negatywne, czy neutralne
    if sentiment_dict['compound'] >= 0.05 :
        lbl0 = tkinter.Label(fen, text = " Positive ", fg='green')
        lbl0.place (x = 230, y = 50)
 
    elif sentiment_dict['compound'] <= - 0.05 :
        lbl0 = tkinter.Label(fen, text = " Negative ", fg='red')
        lbl0.place (x = 230, y = 50)
 
    else :
        lbl0 = tkinter.Label(fen, text = "  Neutral  ", fg='blue')
        lbl0.place (x = 230, y = 50)
        
    

def clear_text():
    entry1.delete(0,'end')
   
lbl1 = tkinter.Label(fen, text = "Enter your sentence:")
lbl1.place (x = 50, y = 20)
entry1 = tkinter.Entry(fen)
entry1.place (x = 230, y = 20)
lbl2 = tkinter.Label(fen, text = "Result:")
lbl2.place (x = 50, y = 50)
Mood = tkinter.Button(fen, text = "Predict the mood", command = action)
Mood.place(x = 230, y = 80, width = 165)
Clear = tkinter.Button(fen,text="Clear", command=clear_text)
Clear.place(x = 50, y = 80, width = 165)                

fen.mainloop()
