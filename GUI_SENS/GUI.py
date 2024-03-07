from tkinter import *
import subprocess
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os
import csv
import time

from days_left import days_until_next_test


##########################  WINDOW  ###############################################
window = Tk()
window.geometry('1366x768')
window.title('Beezy')
window.configure(background='#FFFFF0')
window.state('normal')

#####################  PAGES  ############################
def Mite_page():
    days_left = str(days_until_next_test())
    days_left_string = f'Days left until next test: {days_left}'
    Alerts_frame = Frame(main_frame, bg='#FFFFF0')
    lb1 = Label(Alerts_frame, text='Mite Testing System', font=('Bold', 30), bg='#FFFFF0')
    lb1.pack()
    lb2 = Label(Alerts_frame, text=days_left_string, font=('Bold', 15), bg='#FFFFF0')
    lb2.pack()

    days_left = int(-1)
    if days_left < 0:
        test_btn = Button(Alerts_frame, text='Run Test', font=('Bold', 15), bg='#4CAF50', fg='#FFFFFF',
                          #command=lambda: subprocess.run(['python', os.path.join(os.getcwd(), 'script_to_run_mite_detection.py')]))
                          command=lambda: subprocess.run(['python', '/home/pi/Desktop/GUI_SENS/script_to_use_treatment.py']))
        test_btn.pack()
    else:
        test_btn = Button(Alerts_frame, text='Run Test', font=('Bold', 15), bg='#F44336', fg='#FFFFFF', state=DISABLED)
        test_btn.pack()

    with open(os.path.join(os.getcwd(), 'example_plot.csv'), 'r') as f:
        treatment_requirement = str(f.read())

    if treatment_requirement == 'yes':
        treatment_btn = Button(Alerts_frame, text='Deploy Treatment (Recommended)', font=('Bold', 15), bg='#4CAF50', fg='#FFFFFF',
                               #command=lambda: subprocess.run(['python', os.path.join(os.getcwd(), 'script_to_run_mite_detection.py')]))
                               command=lambda: subprocess.run(['python', '/home/pi/Desktop/GUI_SENS/script_to_use_treatment.py']))
        treatment_btn.pack(pady=10)
    else:
        treatment_btn = Button(Alerts_frame, text='Deploy Treatment (Not Recommended)', font=('Bold', 15), bg='#F44336', fg='#FFFFFF',
                               #command=lambda: subprocess.run(['python', os.path.join(os.getcwd(), 'script_to_run_mite_detection.py')]))
                               command=lambda: subprocess.run(['python', '/home/pi/Desktop/GUI_SENS/script_to_use_treatment.py']))
        treatment_btn.pack(pady=10)

    Alerts_frame.pack(pady=20)


def Dashboard_page():
    Dashboard_frame = Frame(main_frame)
    lb = Label(Dashboard_frame, text='Dashboard', font=('Bold', 30), bg='#FFFFF0')
    lb.pack()

    data = pd.read_csv('/home/pi/Desktop/GUI_SENS/example_plot.csv')

    fig, ax1 = plt.subplots()

    # create first y-axis label
    ax1.plot(data['Time'], data['Temp'], color='tab:blue')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Temp', color='tab:blue')
    ax1.tick_params(axis='y', labelcolor='tab:blue')

    # create twin axes object for second y-axis label
    ax2 = ax1.twinx()
    ax2.plot(data['Time'], data['Humidity'], color='tab:green')
    ax2.set_ylabel('% Humidity', color='tab:green')
    ax2.tick_params(axis='y', labelcolor='tab:green')

    ax1.set_title('HUmidity/Temperature Plot')

    # modify x-axis tick labels to show only 5 equally spaced values
    num_rows = len(data)//5
    x_ticks = ax1.get_xticks()
    ax1.set_xticks(x_ticks[::num_rows])

    canvas = FigureCanvasTkAgg(fig, master=Dashboard_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

    Dashboard_frame.pack(pady=20)


###############  Indicators / page swicth  ########################
def hide_indicators():
    Dashboard_indicate.config(bg='#F2BA49')
    Alerts_indicate.config(bg='#F2BA49')


def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()


def indicate(lb, page):
    hide_indicators()
    lb.config(bg='#000000')
    delete_pages()
    page()


################################  OPTIONS FRAME  ##############################################

options_frame = Frame(window, bg='#F2BA49')

#Dashboard
Dashboard_btn = Button(options_frame, text='Dashboard', font=('Bold', 15), fg='#000000', bd=0, bg ='#F2BA49',
                       command=lambda: indicate(Dashboard_indicate, Dashboard_page) )
Dashboard_btn.place(x=10, y=50)

Dashboard_indicate = Label(options_frame, text='', bg = '#F2BA49')
Dashboard_indicate.place(x=3, y=50, width=5, height=40)

#Mite Testing System
Mite_testing_system_btn = Button(options_frame, text='Mite Testing System', font=('Bold', 15), fg='#000000', bd=0, bg ='#F2BA49' ,
                    command=lambda: indicate(Alerts_indicate, Mite_page))
Mite_testing_system_btn.place(x=10, y=100)

Alerts_indicate = Label(options_frame, text='', bg = '#F2BA49')
Alerts_indicate.place(x=3, y=100, width=5, height=40)



#render frame
options_frame.pack(side=LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=300,height=768)

####################    MAIN FRAME ##################################
main_frame = Frame(window, bg='#FFFFF0', highlightbackground='black', 
                   highlightthickness=2)
main_frame.pack(side=LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=768, width=1066)



window.mainloop()