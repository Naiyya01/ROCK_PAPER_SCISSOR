import imghdr
from pickle import PicklingError
from tkinter import *
from PIL import Image, ImageTk
from random import choices, randint

from numpy import imag

#main window 
root = Tk()
root.title("ROCK PAPER SCISSORS")
root.configure(background="pink")

#picture 
rock_img = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper .png"))
scissors_img = ImageTk.PhotoImage(Image.open("scissors.png"))
scissors_img_comp = ImageTk.PhotoImage(Image.open("scissors_comp.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper_comp.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock_comp.png"))

#insert_pictures
user_label = Label(root,image=scissors_img, bg= "pink")
comp_label = Label(root,image=scissors_img_comp, bg="pink")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

#scores
playerScore = Label(root,text=0,font=100,bg="pink", fg="black")
computerScore = Label(root,text=0,font=100,bg="pink", fg="black")
computerScore.grid(row=1,column=1)
playerScore.grid(row=1,column=3)

#indicators
user_indicators = Label(root, font=50,text="USER" , bg="pink", fg="black")
comp_indicators = Label(root, font=50,text="COMPUTER" , bg="pink", fg="black")
user_indicators.grid(row=0, column=3)
comp_indicators.grid(row=0, column=1)

#messages
msg = Label(root, font=50, bg="pink", fg="black")
msg.grid(row=3, column=2)

#update messages
def updateMessage(x):
    msg['text']= x

#update user score 
def updateUserScore():  
    score= int(playerScore["text"])
    score+=1
    playerScore["text"]= str(score)

#update computer score
def updateCompScore():
    score= int(computerScore["text"])
    score+=1
    computerScore["text"]= str(score)

#check winner
def checkWin(player,computer):
    if player==computer:
        updateMessage("its a tie !!!")
    elif player == "rock":
        if computer=="paper":
            updateMessage("you loose")
        else:
            updateMessage("you win")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("you loose")
            updateCompScore()
        else:
            updateMessage("you win")
            updateUserScore()
    elif player=="scissor":
        if computer=="rock":
            updateMessage("you loose")
            updateCompScore()
        else:
            updateMessage("you win")
            updateUserScore()

    else:
        pass


#update choices

choices = ["rock","paper","scissor"]
def updateChoices(x):
    #for computer
    compChoice = choices[randint(0,2)]
    if compChoice=="rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice=="paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissors_img_comp)


    #for user
    if x=="rock":
        user_label.configure(image=rock_img)
    elif x=="paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissors_img) 

    checkWin(x,compChoice)      
 
#button
rock = Button(root, width=20, height=2, text="ROCK",bg="#0ABDE3", fg="white", command= lambda:updateChoices("rock")).grid(row=2,column=1)
paper = Button(root, width=20, height=2, text="PAPER",bg="red", fg="white", command= lambda:updateChoices("paper")).grid(row=2,column=2)
scissor = Button(root, width=20, height=2, text="SCISSOR",bg="green", fg="white", command= lambda:updateChoices("scissor")).grid(row=2,column=3)



root.mainloop()