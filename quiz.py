from tkinter import*
from tkinter import messagebox
screen= Tk()
screen.title("_")
screen.geometry("400x500")
screen.resizable(False , False)

def show():
    fr.place_forget()
    fr1.place(x=0,y=0)


fr= Frame(screen , bg="#E3DAC9"  ,width=400, height=500)
fr.place(x=0 , y=0)

start= Label(fr, text="Hey!\n Ready to do a short quiz? \n This is called: \n How much do you know about Tkinter? \n Ready?" ,
font=("calibri" , 14))
start.place(x=50,y=180)
bt= Button(fr , text="Let's Go!" , font=("calibri" , 14 , "bold") , bg="#F4C2C2" , command=show)
bt.place(x=150,y=350)

lbl= Label(fr , text="QUIZ" , font=("georgia" , 24 , "bold"))
lbl.place(x=150 , y=40)
# page1-----------------

score=0

fr2= Frame(screen , width=400, height=500 , bg="#E3DAC9")
fr2.place_forget()

def next1():
    global a , score
    a=answer.get()
    if a== 2:
        score+=1
    if a==0:
        messagebox.showerror("enter the correct item")
    else:
        fr1.place_forget()
        fr2.place(x=0,y=0)

answer= IntVar(value=0)

fr1= Frame(screen , width=400, height=500 , bg="#E3DAC9")
fr1.place_forget()

qu1= Label(fr1, text="which widget creats a button?" , font=("caribri" , 14))
qu1.place(x=20,y=50)
r1= Radiobutton(fr1 , text="Text" , value="1" , variable=answer , font=("Roboto"))
r1.place(x= 30,y=130)

r2= Radiobutton(fr1 , text="Button"  , value="2" , variable=answer , font=("Roboto"))
r2.place(x=30,y=180)

r3= Radiobutton(fr1 , text="Label" , value="3" , variable=answer , font=("Roboto"))
r3.place(x=30,y=230)

r4= Radiobutton(fr1 , text="Frame"  , value="4" , variable=answer , font=("Roboto"))
r4.place(x=30,y=280)

b=Button(fr1 , text="Next" , bg="#9BB7D4" , font=("calibri" , 14 ,"bold") , command=next1)
b.place(x=150,y=370)

# page2------------------

fr3= Frame(screen , bg="#E3DAC9" , width=400 , height=500)
fr3.place_forget()

def next2():
    global b, score
    b=answer2.get()
    if b== 7:
        score+=1
    if b==0:
        messagebox.showerror("enter the correct item")
    else:
        fr2.place_forget()
        fr3.place(x=0,y=0)

qu2= Label(fr2 , text="Which widget lets the user type text?" , font=("caribri" , 14))
qu2.place(x= 20,y=50)

answer2= IntVar(value=0)

r5= Radiobutton(fr2 , text="Button" , value="5" , variable= answer2 , font=("Roboto"))
r5.place(x=30,y=130)

r6= Radiobutton(fr2 , text="Label" , value="6" , variable=answer2 , font=("Roboto"))
r6.place(x=30 ,y=180)

r7= Radiobutton(fr2 , text="Entry" , value="7" , variable=answer2 , font=("Roboto"))
r7.place(x=30,y=230)

r8= Radiobutton(fr2 , text="Frame" , value="8" , variable=answer2 , font=("Roboto"))
r8.place(x= 30 , y=280)

bn= Button(fr2 , text="Next" , bg="#9BB7D4" , font=("calibri" , 14, "bold") , command=next2)
bn.place(x=150 , y=370)

# page3----------------

fr4= Frame(screen , bg="#E3DAC9" , width=400 , height=500)
fr4.place_forget()

def next3():
    global c, score
    c=answer3.get()
    if c== 12:
        score+=1
    if c==0:
        messagebox.showerror("enter the correct item")
    else:
        fr3.place_forget()
        fr4.place(x=0,y=0)

answer3= IntVar(value="0")


qu3= Label(fr3 , text="What does 'bg' means in tkinter?" , font=("caribri" , 14))
qu3.place(x=20 , y=50)

r9= Radiobutton(fr3 , text="Begin" , value="9" , variable=answer3 , font=("Roboto"))
r9.place(x=30 , y=130)

r10= Radiobutton(fr3 , text="Button" , value="10" , variable=answer3 , font=("Roboto"))
r10.place(x=30 , y=180)

r11= Radiobutton(fr3 , text="Border" , value="11" , variable=answer3 , font=("Roboto"))
r11.place(x=30,y=230)

r12= Radiobutton(fr3 , text="Background" , value="12" , variable=answer3 , font=("Roboto"))
r12.place(x=30 , y=280)

but= Button(fr3 , text="Next" , bg="#9BB7D4" , font=("calibri" , 14, "bold") , command=next3)
but.place(x=150, y=370)

# page4----------------

fr5= Frame(screen , bg="#E3DAC9" , width=400 , height=500)
fr.place_forget

def next4():
    global d, score
    d=answer4.get()
    if d== 13:
        score+=1
    if d==0:
        messagebox.showerror("enter the correct item")
    else:
        fr4.place_forget()
        fr5.place(x=0,y=0)

answer4= IntVar(value=0)

qu4= Label(fr4 , text="What dose 'pack()' do?" , font=("caribri" , 14))
qu4.place(x=20 , y=50)

r13= Radiobutton(fr4 , text="Places widgets" , value="13" , variable=answer4 , font=("Robotp"))
r13.place(x=30 , y=130)

r14= Radiobutton(fr4 , text="Delets widgets" , value="14" , variable=answer4 , font=("Robotp"))
r14.place(x=30 , y=180)

r15= Radiobutton(fr4 , text="Closes the window" , value="15" , variable=answer4 , font=("Robotp"))
r15.place(x=30 , y=230)

r16= Radiobutton(fr4 , text="Changes the font" , value="16" , variable=answer4 , font=("Robotp"))
r16.place(x=30, y=280)

bbt= Button(fr4 , text="Next" , bg="#9BB7D4" , font=("calibri" , 14, "bold") , command=next4)
bbt.place(x=150 ,y=370)

# page5----------------

final= Frame(screen , bg= "#E3DAC9" , width=400, height=500)
final.place_forget()

def next5():
    global e, score
    e=answer5.get()
    if e== 19:
        score+=1
    if e==0:
        messagebox.showerror("enter the correct item")
    else:
        fr5.place_forget()
        final.place(x=0,y=0)
        result= Label(final , text=f"Quiz finished! \n you got {score} out of 5!" , font=("calibri" , 14))
        result.place(x=120 , y=150)

answer5= IntVar(value=0)

qu5= Label(fr5 , text="Which widget allows choosing one item?" , font=("caribri" , 14))
qu5.place(x=20,y=50)

r17= Radiobutton(fr5 , text="Label" , value="17" , variable=answer5 , font=("Roboto"))
r17.place(x=30 , y=130)

r18= Radiobutton(fr5 , text="Entry" , value="18" , variable=answer5 , font=("Roboto"))
r18.place(x=30 ,y=180)

r19= Radiobutton(fr5 , text="Radiobutton" , value="19" , variable=answer5 , font=("Roboto"))
r19.place(x=30 ,y=230)

r20= Radiobutton(fr5 , text="Mainloop" , value="20" , variable=answer5 , font=("Roboto"))
r20.place(x=30 ,y=280)

tb= Button(fr5 , text="Result" , bg="#9BB7D4" , font=("calibri" , 14, "bold") , command=next5)
tb.place(x=150 ,y=370)

# final page--------------------------

def tries():
    global score
    score= 0
    answer.set(0)
    answer2.set(0)
    answer3.set(0)
    answer4.set(0)
    answer5.set(0)

    final.place_forget()
    fr.place(x=0, y=0)

Bt= Button(final , text="Try Again" ,bg="#FFCCD3" , font=("calibri" , 16 , "bold") , command=tries)
Bt.place(x=150 , y=300)

screen.mainloop()