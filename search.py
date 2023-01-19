# # Your code goes here...
import tkinter as tk
import tkinter.font as tkFont
import csv
from tkinter import *
from tkinter.ttk import *

window = tk.Tk()
fontStyle = tkFont.Font(family="Lucida Grande", size=15)
smallerfontStyle = tkFont.Font(family="Lucida Grande", size=12)
title = tk.Label(text="University Search", font=fontStyle)
title.pack()
greeting = tk.Label(text="Enter the name of the university you're interested in:", font=fontStyle)
greeting.pack()
padding = tk.Label(text=" ", font=fontStyle)
padding.pack()

entry = tk.Entry()
entry.pack()

def search():
    sWindow = tk.Tk()
    name = entry.get()
    count=1
    too_many=False
    school_list=[]
    csv_file = csv.DictReader(open('university-data.csv'))
    for row in csv_file:
        if(name in row['INSTNM']):
            # my_list.append(row['INSTNM']+":\nAddress: "+row["CITY"]+", "+row['STABBR']+" "+row['ZIP']+"\nWebsite: "+row['INSTURL']+"\nTuition (in): "+row['TUITIONFEE_IN']+"\nTuition (out): "+row['TUITIONFEE_OUT']+"\nAdmission Rate: "+row['ADM_RATE']+"\nAverage SAT Score overall:"+row['SAT_AVG']+"\nSAT Reading Midpoint Score:"+row['SATVRMID']+"\nSAT Math Midpoint Score:"+row['SATMTMID']+"\nSAT Writing Midpoint Score:"+row['SATWRMID']+"\nACT English Midpoint Score:"+row['ACTENMID']+"\nACT Math Midpoint Score:"+row['ACTMTMID']+"\nACT Writing Midpoint Score:"+row['ACTWRMID'])
            school_list.append(row['INSTNM'])
            count=count+1
            if(count>20):
                too_many=True
                break
    
    if(too_many):
        retry = tk.Label(sWindow, text="Over 20 schools contain your identifier in their name. Please make your indentifier more specific and re-input it in the search bar.", font=smallerfontStyle)
        retry.pack()
        count=1
    else:
        biggerfontStyle = tkFont.Font(family="Times New Roman", size=20)    
        found = tk.Label(sWindow, text="Found Schools:", font=biggerfontStyle)
        found.pack()
        sorted_school_list=[]
        for sch in school_list:
            small="ZZZZZZZZZZZZ"
            for x in school_list:
                if(x<small and x not in sorted_school_list):
                    small=x
            sorted_school_list.append(small)

    posCount=0
    for sch in sorted_school_list:
        school = tk.Label(sWindow, text=sch, font=smallerfontStyle)
        school.pack()
    
    choose = tk.Label(sWindow, text="Out of the above schools, choose one to input and find specific information over:", font=biggerfontStyle)
    choose.pack()
    
    schEntry = tk.Entry(sWindow)
    schEntry.pack()
    schName=""

    def info():    
        schName=schEntry.get()
        print("info")
        print('school Name: '+schName)
        csv_file = csv.DictReader(open('university-data.csv'))
        notFoundSchool=False
        if(schName not in sorted_school_list):
                newWindow = Toplevel(window)                
                Label(newWindow, text ="That is not one of the listed schools. Please try again.", font=fontStyle).pack()
        else:
            for row in csv_file:
                if(schName == row['INSTNM']):
                    newWindow = Toplevel(window)
                    specificInfo="Name: "+row['INSTNM']+"\nAddress: "+row["CITY"]+", "+row['STABBR']+" "+row['ZIP']+"\nWebsite: "+row['INSTURL']+"\nTuition (in): "+row['TUITIONFEE_IN']+"\nTuition (out): "+row['TUITIONFEE_OUT']+"\nAdmission Rate: "+row['ADM_RATE']+"\nAverage SAT Score overall:"+row['SAT_AVG']+"\nSAT Reading Midpoint Score:"+row['SATVRMID']+"\nSAT Math Midpoint Score:"+row['SATMTMID']+"\nSAT Writing Midpoint Score:"+row['SATWRMID']+"\nACT English Midpoint Score:"+row['ACTENMID']+"\nACT Math Midpoint Score:"+row['ACTMTMID']+"\nACT Writing Midpoint Score:"+row['ACTWRMID']
                    Label(newWindow, text =specificInfo, font=fontStyle).pack()
    
    schButton = tk.Button(sWindow, text ='Specific School Info', command = info, bg="green")
    schButton.pack()

B = tk.Button(window, text ="Search", command = search, bg="green")

B.pack()

window.mainloop()