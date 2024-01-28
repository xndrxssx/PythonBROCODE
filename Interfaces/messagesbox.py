from tkinter import *
from tkinter import messagebox

def click():
    #messagebox.showinfo(title='This is an info messagebox', message='You are a person')
    
    #while(True):
        #messagebox.showwarning(title='Warning', message='You are a potato')
    
    #messagebox.showerror(title='ERRO', message='You arent a person')
    #if messagebox.askokcancel(title='ask ok cancel', message='Do you wanto to do the thing'):
    #    print("You did")
    #else:
    #    print("You didnt")
    
    #if messagebox.askretrycancel(title='ask ok cancel', message='Do you want to retry the thing'):
    #    print("You did")
    #else:
    #    print("You didnt")
    
    #if messagebox.askyesno(title='ask yes or no', message='Do you like cake?'):
    #    print("I like cake too")
    #else:
    #    print("Why do you not like cake?")
    
    #answer = messagebox.askquestion(title='ask question', message='Do you like pie?')
    #if(answer == 'yes'):
    #    print("I like it too")
    #else:
    #    print(":(")
    
    answer = messagebox.askyesnocancel(title='Yes no cancel', message='Do you like to code?', icon='info')
    if(answer==True):
        print("You like to code")
    elif(answer==False):
        print("Why are you here?")
    else:
        print("?")    
    
window = Tk()

button = Button(window, command=click, text='CLICK ME')
button.pack()

window.mainloop()
