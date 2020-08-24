#!/usr/bin/env python
# coding: utf-8

# In[47]:


#!\users\annie\appdata\programs\python
from tkinter import *
from datetime import timedelta
import datetime
import decimal
import sys


# In[48]:


window = Tk()
window.title("TIME TRACKER")
window.geometry('400x450')
window.configure(bg='white')


# In[49]:


lb2= Label(window, text=" Click Start and begin work", font=("Time New Romans", 20),background='light blue')
lb2.grid(column=0, row=1)

lb4 = Label(window, font=("Times New Roman", 11),background='light blue')
lb4.grid(column=0, row=3)

#fuction that stores the time and date after the button is clicked
def calculate_date_time():
    now = datetime.datetime.now()
    date_time=now.strftime("Date:%Y-%m-%d  Start time:%H:%M")
    global only_date
    only_date=now.strftime("%H:%M")
    lb4.configure (text=date_time)
    return only_date


# In[50]:


#Start button
btn = Button(window, text="START",command=calculate_date_time,background='light blue')
btn.grid(column=0, row=2)

lbl3 = Label(window, text="Enter amount then click Stop", font=("Time New Romans", 20),background='light blue')
lbl3.grid(column=0, row=4)

lbl5 = Label(window, text="Amount per hour:", font=("Time New Romans", 20),background='light blue')
lbl5.grid(column=0, row=5)

#variable that holds how much he earns
earn_per_hour = Entry(window,width=10)
earn_per_hour.grid(column=0, row=6)
earn_per_hour.focus()

lbl9 = Label(window, text="Hours spent:", font=("Time New Romans", 20),background='light blue')
lbl9.grid(column=0,row=7)

lbl6 = Label(window, text="You have earned ($):", font=("Time New Romans", 20),background='light blue')
lbl6.grid(column=0,row=9)

lbl7 = Label(window, font=("Time New Romans", 10),background='light blue')
lbl7.grid(column=0,row=10)


# In[51]:


#function that stores your stop time and takes your start time and calculates your earnings
def money_made():
    #getting time for stop work
    global date_time2
    global total_hours
    global total_amount

    now2 = datetime.datetime.now()
    date_time2=now2.strftime("%H:%M")


    h=only_date
    delta = timedelta(hours=int(h.split(':')[0]), minutes=int(h.split(':')[1]))
    hour1 = delta.total_seconds()/3600
   

    h2=date_time2
    delta2 = timedelta(hours=int(h2.split(':')[0]), minutes=int(h2.split(':')[1]))
    hour2 = delta2.total_seconds()/3600
   
    
    #amount he earns
    amount_earned=float(earn_per_hour.get())
    
    
    total_hours=round(hour2-hour1,1)
    total_amount= total_hours*amount_earned
    
    #displays the hours spent working
    lbl8.configure(text=total_hours)

    #displays the amount earned
    lbl7.configure(text=total_amount)
    
    original_stdout=sys.stdout

    #passes all information to a csv file
    with open('C:/Users/Papa Jay/Desktop/Azubi work/codes/detail.csv','a') as writefile:
        sys.stdout= writefile
        info={'Time started':[only_date],'Time stopped':[date_time2],'Hours spent':[total_hours],'Amount earned':[total_amount]}
        info_frame=pd.DataFrame(info)
        writefile.write(str(info_frame))
        writefile.write('\n')
        writefile.close()
        sys.stdout=original_stdout


# In[ ]:


lbl8 = Label(window, font=("Time New Romans", 10),background='light blue')
lbl8.grid(column=0,row=8)  


   
 #stop button 
btn2 = Button(window, text="STOP",command=money_made,background='light blue')
btn2.grid(column=0, row=11)



window.mainloop()


# In[ ]:




