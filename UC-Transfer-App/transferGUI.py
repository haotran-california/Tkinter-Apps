from tkinter import * 
from tkinter import ttk
import sqlite3


window = Tk()
window.title("UC Transfer GUI")
window.geometry("800x500")

#EVENT HANDLERS 
def comboClick(event): 
    majors = loadSelectMajor(selectSchool.get())
    selectMajor.config(value=majors)
    selectMajor.current(0)


def newWindow(fn): 
    def openResultWindow(*args): 
        query = fn(*args)
        display = Toplevel()
        college = query[1]
        major = query[2]
        admitGPA = query[3]
        admitRate = query[4]
        enrollGPA = query[5]
        yeildRate = query[6]
        admits = query[7]
        applicants = query[8]
        enrolls = query[9]

        collegeLbl = Label(master = display, text=college)
        majorLbl = Label(master = display, text=major)
        admitGPALbl = Label(master = display, text=admitGPA)
        admitRateLbl = Label(master = display, text=admitRate)
        enrollGPALbl = Label(master = display, text=enrollGPA)
        yeildRateLbl = Label(master = display, text=yeildRate)
        admitsLbl = Label(master = display, text = admits)
        applicantsLbl = Label(master = display, text=applicants)
        enrollsLbl = Label(master = display, text =enrolls)

        collegeLbl.pack()
        majorLbl.pack()
        admitGPALbl.pack()
        admitRateLbl.pack()
        enrollGPALbl.pack()
        yeildRateLbl.pack()
        admitsLbl.pack()
        applicantsLbl.pack()
        enrollsLbl.pack()
        return query

    return openResultWindow


#SQL FUCTIONS
@newWindow
def search(school, major): 
    conn = sqlite3.connect("UC_Transfer.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM {} WHERE Major = (?)".format(school), (major, ))
    result = cur.fetchall()

    return result[0]
    
def loadSelectMajor(school): 
    conn = sqlite3.connect("UC_Transfer.db")
    cur = conn.cursor()
    cur.execute("SELECT Major FROM {}".format(school))
    results = cur.fetchall()
    major_list = []
    for major in results: 
        major_list.append(major[0])
   
    return major_list





schools = ["UCB", "UCD", "UCI", "UCLA", "UCR", "UCSB", "UCSC", "UCSD"]

#MAIN PROGRAM WIDGETS 
selectSchool = ttk.Combobox(window, value=schools)
selectSchool.current(0)
selectSchool.bind("<<ComboboxSelected>>", comboClick)
selectSchool.grid(row=1, column=0)

majors = loadSelectMajor(selectSchool.get())

selectMajor = ttk.Combobox(window, value=majors)
selectMajor.current(0)
selectMajor.bind("<<ComboboxSelected>>", comboClick)
selectMajor.grid(row=2, column=0)

submitBtn = Button(text="Submit", command= lambda: search(selectSchool.get(), selectMajor.get()))
submitBtn.grid(row=3, column=0)

window.mainloop()