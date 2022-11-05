# HIT137 - Group 84
# Name : Ricky Maharjan - ID-s359074
# Name : Abinab D C - ID-s360320
# Python GUI Interface for Poin of Sale
from tkinter import *
from tkinter import ttk
import tkinter.font as font


class POS:
    def __init__(self,window):
        self.window = window
        #getting screen width and height of display
        # width= window.winfo_screenwidth()
        # height= window.winfo_screenheight()
        #setting tkinter window size
        window.geometry("1366x768")
        window.title("Point of Sale")
        #Creating Main Frame for content
        MainFrame = Frame(self.window, bg="white")
        MainFrame.grid(padx=8,pady=8)
        ###=========> Create Left frame for Food and Items
        LeftFrame = Frame(MainFrame, bg="white", bd=3 , width=1000, height=758, padx=5, pady=5, relief=RIDGE)
        LeftFrame.pack(side=LEFT)
        ###========> Left Frame Content
        #create a tab based menu
        menu_tab = ttk.Notebook(LeftFrame,width=995,height=740)
        menu_button_height = 3
        menu_button_width = 15
        menu_button_font = font.Font(size=14,family='Helvetica')
        #creating new tabs using frame widget
        food_menu_tab = Frame(menu_tab,width=955, height=755)
        drinks_meun_tab = Frame(menu_tab,width=955, height=755)
        special_menu_tab = Frame(menu_tab,width=955, height=755)

        menu_tab.add(food_menu_tab, text="Food")
        menu_tab.add(drinks_meun_tab, text="Drinks")
        menu_tab.add(special_menu_tab, text="Special")
        menu_tab.pack(expand=1, fill="both")
        ### Food menu tab content  ###
        
        self.mixed_olives = Button(food_menu_tab, padx=10,pady=10,width=menu_button_width,height=menu_button_height,font=menu_button_font,text='Mixed Olives')
        self.mixed_olives.grid(row=1,column=1,padx=2,pady=2)
        self.foccacia = Button(food_menu_tab, padx=10,pady=10,width=menu_button_width,height=menu_button_height,font=menu_button_font,text='Foccacia')
        self.foccacia.grid(row=1,column=2,padx=2,pady=2)
        self.caprese = Button(food_menu_tab, padx=10,pady=10,width=menu_button_width,height=menu_button_height,font=menu_button_font,text='Caprese Salad')
        self.caprese.grid(row=1,column=3,padx=2,pady=2)
        self.scallops = Button(food_menu_tab, padx=10,pady=10,width=menu_button_width,height=menu_button_height,font=menu_button_font,text='Scallops')
        self.scallops.grid(row=1,column=4,padx=2,pady=2)
        self.pickled_octopus = Button(food_menu_tab, padx=10,pady=10,width=menu_button_width,height=menu_button_height,font=menu_button_font,text='Pickled Octopus')
        self.pickled_octopus.grid(row=1,column=5,padx=2,pady=2)
        self.squid = Button(food_menu_tab, padx=10,pady=10,width=menu_button_width,height=menu_button_height,font=menu_button_font,text='Squid')
        self.squid.grid(row=2,column=1,padx=2,pady=2)
        self.prawns = Button(food_menu_tab, padx=10,pady=10,width=menu_button_width,height=menu_button_height,font=menu_button_font,text='Prawns')
        self.prawns.grid(row=2,column=2,padx=2,pady=2)
        self.chilli_prawns = Button(food_menu_tab, padx=10,pady=10,width=menu_button_width,height=menu_button_height,font=menu_button_font,text='Chilli Prawns')
        self.chilli_prawns.grid(row=2,column=3,padx=2,pady=2)
        self.coconut_prawns = Button(food_menu_tab, padx=10,pady=10,width=menu_button_width,height=menu_button_height,font=menu_button_font,text='Coconut Prawns')
        self.coconut_prawns.grid(row=2,column=4,padx=2,pady=2)
        #  self.caprese = Button(food_menu_tab, padx=10,pady=10,text='Caprese Salad')
        # self.caprese.grid(row=1,column=3,padx=2,pady=2)
        #  self.caprese = Button(food_menu_tab, padx=10,pady=10,text='Caprese Salad')
        # self.caprese.grid(row=1,column=3,padx=2,pady=2)
        #  self.caprese = Button(food_menu_tab, padx=10,pady=10,text='Caprese Salad')
        # self.caprese.grid(row=1,column=3,padx=2,pady=2)
        ### Drinks menu tab content ###
        self.button1 = Button(drinks_meun_tab, padx=2,pady=2,text='Hello')
        self.button1.grid(row=1,column=1,padx=2,pady=2)

        ### Special menu tab content ### 
        self.button1 = Button(special_menu_tab, padx=2,pady=2,text='Hello')
        self.button1.grid(row=0,column=1,padx=2,pady=2)

        ###======> Right Frame for Calculation
        RightFrame = Frame(MainFrame, bg="white", bd=3 , width=350, height=758, padx=5, pady=5, relief=RIDGE)
        RightFrame.pack(side=RIGHT)
        ###========> Right Frame Content



        
window = Tk()  #create blank window
app = POS(window)
window.mainloop() #Keep screen open until closed to break loop