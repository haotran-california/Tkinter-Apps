from tkinter import * 
from tkinter import ttk
from databaseFunctions import search, loadSelectMajor

window = Tk()
window.title("UC Transfer GUI")
window.geometry("800x500")

#EVENT HANDLERS 
def comboSelect(event): 
    #when a new school is selected load the list of majors into the selectMajor combo-box
    majors = loadSelectMajor(selectSchool.get())
    selectMajor.config(value=majors)
    selectMajor.current(0)

#DECORATOR FUNCTION
def newWindow(fn): 
    def openResultWindow(): 
        query = fn()
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

#BUTTON FUNCTION
@newWindow
def submitSearch(): 
    queryResult = search(selectSchool.get(), selectMajor.get())
    return queryResult


schools = ["UCB", "UCD", "UCI", "UCLA", "UCR", "UCSB", "UCSC", "UCSD"]

#MAIN PROGRAM WIDGETS 
selectSchool = ttk.Combobox(window, value=schools)
selectSchool.current(0)
selectSchool.bind("<<ComboboxSelected>>", comboSelect)
selectSchool.grid(row=1, column=0)

majors = loadSelectMajor(selectSchool.get())

selectMajor = ttk.Combobox(window, value=majors)
selectMajor.current(0)
selectMajor.grid(row=2, column=0)

submitBtn = Button(text="Submit", command=submitSearch)
submitBtn.grid(row=3, column=0)

window.mainloop()