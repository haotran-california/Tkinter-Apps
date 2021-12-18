from tkinter import filedialog
import sqlite3

#DEFINE SQL FUNCTIONS
def SignIn(username, password): 
    #Create a new database or connect a previous one 
    conn = sqlite3.connect("users.db")

    #Create a cursor object to exectue SQL commands 
    cur = conn.cursor()

    #If username exists within database then check if passwords match 
    if checkUserExists(username) == True: 
        cur.execute("SELECT password FROM userLogin WHERE username = (?)", (username, ))
        p = cur.fetchall()
        if password == p[0][0]: 
            return True

    #Commit changes 
    conn.commit()

    #Close connection 
    conn.close()
    

def checkUserExists(username): 
    #Create a new database or connect a previous one 
    conn = sqlite3.connect("users.db")

    #Create a cursor object to exectue SQL commands 
    cur = conn.cursor()

    #Check if user exists 
    cur.execute("SELECT username FROM userLogin")
    usernameData = cur.fetchall()
    for user in usernameData: 
        if user[0] == username: 
            return True 

    #account for unclosed connection in main? since this technicall doesn't change the code 
    return False



def CreateAccount(username, password): 
    #Create a new database or connect a previous one 
    conn = sqlite3.connect("users.db")

    #Create a cursor object to exectue SQL commands 
    cur = conn.cursor()

    #If username exists in the database then insert username and password 

    if checkUserExists(username) == False: 
        cur.execute("INSERT INTO userLogin (username, password) VALUES (?, ?)", 
                    (username, password) )

    #Commit changes 
    conn.commit()

    #Close connection 
    conn.close()


def intializeDataTable(): 
    #Create a new database or connect a previous one 
    conn = sqlite3.connect("users.db")

    #Create a cursor object to exectue SQL commands 
    cur = conn.cursor()

    #Create inital data table 
    cur.execute("""CREATE TABLE userLogin
                    (username text, 
                     password text)""")

    #Commit changes 
    conn.commit()

    #Close connection 
    conn.close()

#DEFINE FUNCTIONS
def Input(): 
    #select file 
    select_file = filedialog.askopenfilename(title="Select File", filetypes=(("Text Files", "*.txt"),))
    file = open(select_file, "r")

    #parse text file 
    words = {}
    for l in file:
        sentence = l.split()
        for w in sentence:
            words[w] = words.get(w, 0) + 1

    #sort the dictionary by value
    sorted_words = {k: v for k, v in sorted(words.items(), key = lambda v: v[1], reverse = True)}



