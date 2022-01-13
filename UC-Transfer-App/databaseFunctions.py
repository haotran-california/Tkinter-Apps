import sqlite3

#SQL FUCTIONS
def search(school, major): 
    #returns data for a particular major from a particular school in the form of a row object
    conn = sqlite3.connect("UC_Transfer.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM {} WHERE Major = (?)".format(school), (major, ))
    result = cur.fetchall()

    return result[0]
    
def loadSelectMajor(school): 
    #returns a list of all majors from a particular school
    conn = sqlite3.connect("UC_Transfer.db")
    cur = conn.cursor()
    cur.execute("SELECT Major FROM {}".format(school))
    results = cur.fetchall()
    major_list = []
    for major in results: 
        major_list.append(major[0])
   
    return major_list