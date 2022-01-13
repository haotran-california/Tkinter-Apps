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

        #parse query into variables 
        college = query[1]
        major = query[2]
        admitGPA = query[3]
        admitRate = query[4]
        enrollGPA = query[5]
        admits = query[7]
        applicants = query[8]

        description = ["College:", "Major:", "Admit GPA:", "Admit Rate:", "Enroll GPA:", "Admits:", "Applicants:"]
        data = [college, major, admitGPA, admitRate, enrollGPA, admits, applicants]

        #display 
        for i in range(len(data)): 
            descriptionLbl = Label(master=display, text=description[i])
            dataLbl = Label(master=display, text=data[i])
            descriptionLbl.grid(row=i, column=0, sticky=W)
            dataLbl.grid(row=i, column=1)

        exitBtn = Button(master=display, text="Exit", command=display.quit)
        exitBtn.grid(row = 7, column=0, sticky=W)

        return query

    return openResultWindow

#BUTTON FUNCTION
@newWindow
def submitSearch(): 
    queryResult = search(selectSchool.get(), selectMajor.get())
    return queryResult


schools = ["UCB", "UCD", "UCI", "UCLA", "UCR", "UCSB", "UCSC", "UCSD"]

#MAIN PROGRAM WIDGETS 
selectSchool = ttk.Combobox(window, value=schools, state="readonly")
selectSchool.current(0)
selectSchool.bind("<<ComboboxSelected>>", comboSelect)
selectSchool.grid(row=1, column=0)

majors = loadSelectMajor(selectSchool.get())

selectMajor = ttk.Combobox(window, value=majors, state="readonly")
selectMajor.current(0)
selectMajor.grid(row=2, column=0)

submitBtn = Button(text="Submit", command=submitSearch)
submitBtn.grid(row=3, column=0, sticky=W)

exitBtn = Button(text="Exit", command=window.quit)
exitBtn.grid(row = 3, column=1, sticky=W)

window.mainloop()