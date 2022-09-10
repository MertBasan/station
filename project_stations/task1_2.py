#library that allows to build the General User Interface(GUI)
from tkinter import *
#Getting the functions from "Stations.py"
from Stations import *


station=Stations("railway_stations.csv")


#GUI starts from here
root= Tk()
root.title("Train station finder")


canvas1 = Canvas(root, width = 500, height = 500,  relief = 'raised')
canvas1.pack()


#the fisrt list that contains the information of approx results of the user input
def show_list(s):
    x= list(station.match(s))
    global liste1
    liste1=Listbox(root,selectmode="multiple")
    liste1.config(width=30,height=10)
    canvas1.create_window(230,330,window=liste1)

    for each_item in range(len(x)):
        liste1.insert(END, x[each_item])
        liste1.itemconfig(each_item)

    button_show= Button(root,text="Select suggestion",command=show_selected)
    canvas1.create_window(230,470,window=button_show)






#another list that contains user's selection 
def show_selected():
    station.suggestions 
    sname = liste1.curselection()
    final=Listbox(root)
    final.config(width=40,height=1)
    final.curselection()
    canvas1.create_window(230,430,window=final)
    for i in sname:
        op = liste1.get(i)
        choice=station.get_result(op)
        final.insert(END,choice)
    
    
    

#Gui labels, entries and buttons

label1 = Label(root, text='Type the station you want to find:',font="Helvatica")
label1.config(font=('helvetica', 10))
canvas1.create_window(230, 150, window=label1)

label2=Label(root,text=("Welcome to the station finder please input the station or abbreviation name below. \n It is also fine if you do not remember the exact name of the station. \nThe system will generate the approximate results !"))
label2.config(font=('helvatica',10))
canvas1.create_window(250,100,window=label2)

choices = Entry(root)
canvas1.create_window(230, 180, window=choices)

#button that get the match algorithm and print the list
buttonMatches = Button(root,text='Find the Matches',command=lambda:show_list(str(choices.get())),bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(230, 220, window=buttonMatches)


root.mainloop()






