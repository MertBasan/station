#interface library
from tkinter import *
#csv file library
import csv 


#GUI starts from here
root=Tk()
root.title("Station Finder Basic")

canvas1=Canvas(root,width=350,height=350, relief="raised")
canvas1.pack()

#function that finds the perfect match 
def station_finder(input):
    final=Listbox(root)
    final.config(height=1,width=20)
    canvas1.create_window(180,180,window=final)
    file=open('railway_stations.csv',"r")
    reader= csv.reader(file)

    for line in reader:
        if line[0].lower()== input:
            final.insert(END,line[1])
            break   
        elif line[1].lower()== input:
            final.insert(END,line[0])
            break
            
    else:
        final.insert(END,"Not Found !")



#gui labels entries and buttons
label1= Label(root,text="Type the station or the abbrevation the system \n system will return you the match !")
label1.config(font=('helvetica', 10))
canvas1.create_window(180, 50, window=label1)

entry= Entry(root)
canvas1.create_window(180, 100, window=entry)

buttonMatches = Button(root,text='Find the Match',command=lambda:station_finder(entry.get()),bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(180, 130, window=buttonMatches)

root.mainloop()




