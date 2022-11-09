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
        self.window.geometry("1366x780")
        self.window.title("Point of Sale")
        self.window.configure(background='white')
       
             
        #Creating Main Frame for content
        MainFrame = Frame(self.window, bg="white")
        MainFrame.grid(padx=8,pady=8)
        ###=========> Create Menu frame for Food and Items
        MenuFrame = Frame(MainFrame, bg="white", bd=3 , width=1000,height=500, padx=5, pady=5, relief=RIDGE)
        MenuFrame.pack(side=LEFT)
        ImageFrame = Frame(MainFrame, bg="white", bd=3 , width=1000,height=2600, padx=5, pady=5, relief=RIDGE)
        ImageFrame.pack(side=LEFT)
        ###======> Receipt Frame for listing items
        ReceiptFrame = Frame(MainFrame, bg="white", bd=3 , width=350, height=300, padx=5, pady=5, relief=RIDGE)
        ReceiptFrame.pack(side=TOP)
        ###======> Calculation Frame
        CalculationFrame = Frame(MainFrame, bg="white", bd=3 , width=350, height=400, padx=5, pady=5, relief=RIDGE)
        CalculationFrame.pack(side=TOP)
        ###======> Action Frame
        ActionFrame = Frame(MainFrame, bg="white", bd=3 , width=350, height=50, padx=2, pady=2, relief=RIDGE)
        ActionFrame.pack(side=TOP)
        
        table_input = StringVar()
        change_input = StringVar()
        change_input.set("$ 0.00")
        cash_input = StringVar()
        tax_input = StringVar()
        tax_input.set("$ 0.00")
        subtotal_input = StringVar()
        subtotal_input.set("$ 0.00")
        total_input = StringVar()
        total_input.set("$ 0.00")
        payment_type = StringVar()
        payment_type.set("Cash")

        ###========> Menu Frame Content
        #create a tab based menu
        menu_tab = ttk.Notebook(MenuFrame,width=995,height=720)
        menu_button_height = 3 #all menu button height
        menu_button_width = 15 #all menu button width
        menu_button_font = font.Font(size=14,family='Helvetica') #all menu button Fonts
        #creating new tabs using frame widget
        food_menu_tab = Frame(menu_tab,width=955, height=720)
        drinks_meun_tab = Frame(menu_tab,width=955, height=720)

        menu_tab.add(food_menu_tab,text="Food")
        menu_tab.add(drinks_meun_tab, text="Drinks")
        menu_tab.pack(expand=1, fill="both")
        ############# Functions ##############
        ###### add Menu items function
        def mixed_olives():
            price = 8.00
            tax = 3
            self.POS_receipt.insert("",'end',values=("Mixed Olives", "1","8.00"))
            for child in self.POS_receipt.get_children():
                price += float(self.POS_receipt.item(child,"values")[2])
                subtotal_input.set(str('$ %.2f'%(price-8.00)))
                tax_input.set(str('$ %.2f'%(((price-8.00)*tax)/100)))
                total_input.set(str('$ %.2f'%((price-8.00)+((price-8.00)*tax/100))))
        def foccacia():
            price = 8.00
            tax = 3
            self.POS_receipt.insert("",'end',values=("Foccacia", "1","8.00"))
            for child in self.POS_receipt.get_children():
                price += float(self.POS_receipt.item(child,"values")[2])
                subtotal_input.set(str('$ %.2f'%(price-8.00)))
                tax_input.set(str('$ %.2f'%(((price-8.00)*tax)/100)))
                total_input.set(str('$ %.2f'%((price-8.00)+((price-8.00)*tax/100))))  
        def caprese_salad():
            price = 15.00
            tax = 3
            self.POS_receipt.insert("",'end',values=("Capresr salad", "1","15.00"))
            for child in self.POS_receipt.get_children():
                price += float(self.POS_receipt.item(child,"values")[2])
                subtotal_input.set(str('$ %.2f'%(price-15.00)))
                tax_input.set(str('$ %.2f'%(((price-15.00)*tax)/100)))
                total_input.set(str('$ %.2f'%((price-15.00)+((price-15.00)*tax/100))))  
        def scallops():
            price = 22.00
            tax = 3
            self.POS_receipt.insert("",'end',values=("Scallps", "1","22.00"))
            for child in self.POS_receipt.get_children():
                price += float(self.POS_receipt.item(child,"values")[2])
                subtotal_input.set(str('$ %.2f'%(price-22.00)))
                tax_input.set(str('$ %.2f'%(((price-22.00)*tax)/100)))
                total_input.set(str('$ %.2f'%((price-22.00)+((price-22.00)*tax/100))))  
        def pickled_octopus():
            price = 14.00
            tax = 3
            self.POS_receipt.insert("",'end',values=("Pickled Octopus", "1","14.00"))
            for child in self.POS_receipt.get_children():
                price += float(self.POS_receipt.item(child,"values")[2])
                subtotal_input.set(str('$ %.2f'%(price-14.00)))
                tax_input.set(str('$ %.2f'%(((price-14.00)*tax)/100)))
                total_input.set(str('$ %.2f'%((price-14.00)+((price-14.00)*tax/100))))  
                
        def squid():
            price = 16.00
            tax = 3
            self.POS_receipt.insert("",'end',values=("Squid", "1","16.00"))
            for child in self.POS_receipt.get_children():
                price += float(self.POS_receipt.item(child,"values")[2])
                subtotal_input.set(str('$ %.2f'%(price-16.00)))
                tax_input.set(str('$ %.2f'%(((price-16.00)*tax)/100)))
                total_input.set(str('$ %.2f'%((price-16.00)+((price-16.00)*tax/100))))  
        def prawns():
            price = 18.00
            tax = 3
            self.POS_receipt.insert("",'end',values=("Prawns", "1","18.00"))
            for child in self.POS_receipt.get_children():
                price += float(self.POS_receipt.item(child,"values")[2])
                subtotal_input.set(str('$ %.2f'%(price-18.00)))
                tax_input.set(str('$ %.2f'%(((price-18.00)*tax)/100)))
                total_input.set(str('$ %.2f'%((price-18.00)+((price-18.00)*tax/100))))  
        def chilli_prawns():
            price = 16.00
            tax = 3
            self.POS_receipt.insert("",'end',values=("Chilli Prawns", "1","16.00"))
            for child in self.POS_receipt.get_children():
                price += float(self.POS_receipt.item(child,"values")[2])
                subtotal_input.set(str('$ %.2f'%(price-16.00)))
                tax_input.set(str('$ %.2f'%(((price-16.00)*tax)/100)))
                total_input.set(str('$ %.2f'%((price-16.00)+((price-16.00)*tax/100))))
        def coconut_prawns():
            price = 21.00
            tax = 3
            self.POS_receipt.insert("",'end',values=("Coconut Prawns", "1","21.00"))
            for child in self.POS_receipt.get_children():
                price += float(self.POS_receipt.item(child,"values")[2])
                subtotal_input.set(str('$ %.2f'%(price-21.00)))
                tax_input.set(str('$ %.2f'%(((price-21.00)*tax)/100)))
                total_input.set(str('$ %.2f'%((price-21.00)+((price-21.00)*tax/100))))
        def chicken_wings():
            price = 18.00
            tax = 3
            self.POS_receipt.insert("",'end',values=("Chicken wings", "1","18.00"))
            for child in self.POS_receipt.get_children():
                price += float(self.POS_receipt.item(child,"values")[2])
                subtotal_input.set(str('$ %.2f'%(price-18.00)))
                tax_input.set(str('$ %.2f'%(((price-18.00)*tax)/100)))
                total_input.set(str('$ %.2f'%((price-18.00)+((price-18.00)*tax/100)))) 
        def popcorn_croc():
            price = 21.00
            tax = 3
            self.POS_receipt.insert("",'end',values=("Popcorn Crocodile", "1","21.00"))
            for child in self.POS_receipt.get_children():
                price += float(self.POS_receipt.item(child,"values")[2])
                subtotal_input.set(str('$ %.2f'%(price-21.00)))
                tax_input.set(str('$ %.2f'%(((price-21.00)*tax)/100)))
                total_input.set(str('$ %.2f'%((price-21.00)+((price-21.00)*tax/100))))
        def spring_rolls():
            price = 18.00
            tax = 3
            self.POS_receipt.insert("",'end',values=("Spring rolls", "1","18.00"))
            for child in self.POS_receipt.get_children():
                price += float(self.POS_receipt.item(child,"values")[2])
                subtotal_input.set(str('$ %.2f'%(price-18.00)))
                tax_input.set(str('$ %.2f'%(((price-18.00)*tax)/100)))
                total_input.set(str('$ %.2f'%((price-18.00)+((price-18.00)*tax/100))))
        def coconut_margarita():
            price = 19.00
            tax = 3
            self.POS_receipt.insert("",'end',values=("Coconut Margarita", "1","19.00"))
            for child in self.POS_receipt.get_children():
                price += float(self.POS_receipt.item(child,"values")[2])
                subtotal_input.set(str('$ %.2f'%(price-19.00)))
                tax_input.set(str('$ %.2f'%(((price-19.00)*tax)/100)))
                total_input.set(str('$ %.2f'%((price-19.00)+((price-19.00)*tax/100))))
        def taquila():
            price = 9.00
            tax = 3
            self.POS_receipt.insert("",'end',values=("Taquila", "1","9.00"))
            for child in self.POS_receipt.get_children():
                price += float(self.POS_receipt.item(child,"values")[2])
                subtotal_input.set(str('$ %.2f'%(price-9.00)))
                tax_input.set(str('$ %.2f'%(((price-9.00)*tax)/100)))
                total_input.set(str('$ %.2f'%((price-9.00)+((price-9.00)*tax/100))))
        def white_wine():
            price = 19.00
            tax = 3
            self.POS_receipt.insert("",'end',values=("White wine", "1","19.00"))
            for child in self.POS_receipt.get_children():
                price += float(self.POS_receipt.item(child,"values")[2])
                subtotal_input.set(str('$ %.2f'%(price-19.00)))
                tax_input.set(str('$ %.2f'%(((price-19.00)*tax)/100)))
                total_input.set(str('$ %.2f'%((price-19.00)+((price-19.00)*tax/100))))
        def red_wine():
            price = 12.00
            tax = 3
            self.POS_receipt.insert("",'end',values=("Red wine", "1","12.00"))
            for child in self.POS_receipt.get_children():
                price += float(self.POS_receipt.item(child,"values")[2])
                subtotal_input.set(str('$ %.2f'%(price-12.00)))
                tax_input.set(str('$ %.2f'%(((price-12.00)*tax)/100)))
                total_input.set(str('$ %.2f'%((price-12.00)+((price-12.00)*tax/100)))) 
        def beers():
            price = 8.30
            tax = 3
            self.POS_receipt.insert("",'end',values=("Red wine", "1","8.30"))
            for child in self.POS_receipt.get_children():
                price += float(self.POS_receipt.item(child,"values")[2])
                subtotal_input.set(str('$ %.2f'%(price-8.30)))
                tax_input.set(str('$ %.2f'%(((price-8.30)*tax)/100)))
                total_input.set(str('$ %.2f'%((price-8.30)+((price-8.30)*tax/100)))) 
        def cider():
            price = 8.5
            tax = 3
            self.POS_receipt.insert("",'end',values=("Cider", "1","8.5"))
            for child in self.POS_receipt.get_children():
                price += float(self.POS_receipt.item(child,"values")[2])
                subtotal_input.set(str('$ %.2f'%(price-8.5)))
                tax_input.set(str('$ %.2f'%(((price-8.5)*tax)/100)))
                total_input.set(str('$ %.2f'%((price-8.5)+((price-8.5)*tax/100))))
        def coffee():
            price = 4.5
            tax = 3
            self.POS_receipt.insert("",'end',values=("Coffee", "1","4.5"))
            for child in self.POS_receipt.get_children():
                price += float(self.POS_receipt.item(child,"values")[2])
                subtotal_input.set(str('$ %.2f'%(price-4.5)))
                tax_input.set(str('$ %.2f'%(((price-4.5)*tax)/100)))
                total_input.set(str('$ %.2f'%((price-4.5)+((price-4.5)*tax/100))))
        def juice():
            price = 4.5
            tax = 3
            self.POS_receipt.insert("",'end',values=("Juice", "1","4.5"))
            for child in self.POS_receipt.get_children():
                price += float(self.POS_receipt.item(child,"values")[2])
                subtotal_input.set(str('$ %.2f'%(price-4.5)))
                tax_input.set(str('$ %.2f'%(((price-4.5)*tax)/100)))
                total_input.set(str('$ %.2f'%((price-4.5)+((price-4.5)*tax/100))))  
        ############# Calcualtion and otherFunctions ############## 
        ###### Remove item function ####
        def remove_item():
            selected_item = (self.POS_receipt.selection()[0])
            self.POS_receipt.delete(selected_item)
            price = 0.0
            tax = 3
            for item in self.POS_receipt.get_children():
                price += float(self.POS_receipt.item(item,"values")[2])
            subtotal_input.set(str('$ %.2f'%(price)))
            tax_input.set(str('$ %.2f'%((price * tax)/100)))
            total_input.set(str('$ %.2f'%((price)+((price *tax)/100))))
            cash_input.set("")
            change_input.set("$ 0.00")
            ######### Reset all function #######
        def resetAll():
            for item in self.POS_receipt.get_children():
                self.POS_receipt.delete(item)
            subtotal_input.set("$ 0.00")
            tax_input.set("$ 0.00")
            total_input.set("$ 0.00")
            change_input.set("$ 0.00")
            cash_input.set("")
        ####################################
        def payment_type_selected(selection):
            if(selection == 'Card'):
                cash_input.set(total_input.get())
                change_input.set("$ 0.00")
                selected_payment_type = "Card"
            else:
                cash_input.set("")
                change_input.set("$ 0.00")
                selected_payment_type = "Cash"
        def change():
            total_cost = 0.0
            tax = 3
            cash = float(cash_input.get())
            for item in self.POS_receipt.get_children():
                total_cost += float(self.POS_receipt.item(item,"values")[2])
            change_amt = cash -((total_cost)+(total_cost*tax)/100)
            print(change_amt)
            change_input.set("$ %.2F"%change_amt)
        #################################        
        ### Food menu tab content  ###
       
        self.mixed_olives = Button(food_menu_tab, padx=10,pady=10,width=menu_button_width,height=menu_button_height,font=menu_button_font,text='Mixed Olives',command=mixed_olives)
        self.mixed_olives.grid(row=1,column=1,padx=2,pady=2)
        self.foccacia = Button(food_menu_tab, padx=10,pady=10,width=menu_button_width,height=menu_button_height,font=menu_button_font,text='Foccacia',command=foccacia)
        self.foccacia.grid(row=1,column=2,padx=2,pady=2)
        self.caprese = Button(food_menu_tab, padx=10,pady=10,width=menu_button_width,height=menu_button_height,font=menu_button_font,text='Caprese Salad',command=caprese_salad)
        self.caprese.grid(row=1,column=3,padx=2,pady=2)
        self.scallops = Button(food_menu_tab, padx=10,pady=10,width=menu_button_width,height=menu_button_height,font=menu_button_font,text='Scallops',command=scallops)
        self.scallops.grid(row=1,column=4,padx=2,pady=2)
        self.pickled_octopus = Button(food_menu_tab, padx=10,pady=10,width=menu_button_width,height=menu_button_height,font=menu_button_font,text='Pickled Octopus',command=pickled_octopus)
        self.pickled_octopus.grid(row=1,column=5,padx=2,pady=2)
        self.squid = Button(food_menu_tab, padx=10,pady=10,width=menu_button_width,height=menu_button_height,font=menu_button_font,text='Squid',command=squid)
        self.squid.grid(row=2,column=1,padx=2,pady=2)
        self.prawns = Button(food_menu_tab, padx=10,pady=10,width=menu_button_width,height=menu_button_height,font=menu_button_font,text='Prawns',command=prawns)
        self.prawns.grid(row=2,column=2,padx=2,pady=2)
        self.chilli_prawns = Button(food_menu_tab, padx=10,pady=10,width=menu_button_width,height=menu_button_height,font=menu_button_font,text='Chilli Prawns',command=chilli_prawns)
        self.chilli_prawns.grid(row=2,column=3,padx=2,pady=2)
        self.coconut_prawns = Button(food_menu_tab, padx=10,pady=10,width=menu_button_width,height=menu_button_height,font=menu_button_font,text='Coconut Prawns',command=coconut_prawns)
        self.coconut_prawns.grid(row=2,column=4,padx=2,pady=2)
        self.chicken_wings = Button(food_menu_tab, padx=10,pady=10,width=menu_button_width,height=menu_button_height,font=menu_button_font,text='Chicken Wings',command=chicken_wings)
        self.chicken_wings.grid(row=2,column=5,padx=2,pady=2)
        self.popcron_croc = Button(food_menu_tab, padx=10,pady=10,width=menu_button_width,height=menu_button_height,font=menu_button_font,text='Popcron Crocodile',command=popcorn_croc)
        self.popcron_croc.grid(row=3,column=1,padx=2,pady=2)
        self.spring_rolls = Button(food_menu_tab, padx=10,pady=10,width=menu_button_width,height=menu_button_height,font=menu_button_font,text='Spring rolls',command=spring_rolls)
        self.spring_rolls.grid(row=3,column=2,padx=2,pady=2)
        ### Drinks menu tab content ###
        self.coconut_margarita = Button(drinks_meun_tab, padx=10,pady=10,width=menu_button_width,height=menu_button_height,font=menu_button_font,text='Coconut Margarita',command=coconut_margarita)
        self.coconut_margarita.grid(row=1,column=1,padx=2,pady=2)
        self.taquila = Button(drinks_meun_tab, padx=10,pady=10,width=menu_button_width,height=menu_button_height,font=menu_button_font,text='Taquila',command=taquila)
        self.taquila.grid(row=1,column=2,padx=2,pady=2)
        self.white_wine = Button(drinks_meun_tab, padx=10,pady=10,width=menu_button_width,height=menu_button_height,font=menu_button_font,text='White wine',command=white_wine)
        self.white_wine.grid(row=1,column=3,padx=2,pady=2)
        self.red_wine = Button(drinks_meun_tab, padx=10,pady=10,width=menu_button_width,height=menu_button_height,font=menu_button_font,text='Red wine',command=red_wine)
        self.red_wine.grid(row=1,column=4,padx=2,pady=2)
        self.beers = Button(drinks_meun_tab, padx=10,pady=10,width=menu_button_width,height=menu_button_height,font=menu_button_font,text='Beers',command=beers)
        self.beers.grid(row=1,column=5,padx=2,pady=2)
        self.cider = Button(drinks_meun_tab, padx=10,pady=10,width=menu_button_width,height=menu_button_height,font=menu_button_font,text='Cider',command=cider)
        self.cider.grid(row=2,column=1,padx=2,pady=2)
        self.coffee = Button(drinks_meun_tab, padx=10,pady=10,width=menu_button_width,height=menu_button_height,font=menu_button_font,text='Coffee',command=coffee)
        self.coffee.grid(row=2,column=2,padx=2,pady=2)
        self.juice = Button(drinks_meun_tab, padx=10,pady=10,width=menu_button_width,height=menu_button_height,font=menu_button_font,text='Juice',command=juice)
        self.juice.grid(row=2,column=3,padx=2,pady=2)
 
        ###========> Receipt Frame Content
        ### Treeview Widget for Receipt
        scroll_x = Scrollbar(ReceiptFrame,orient=HORIZONTAL)
        scroll_y = Scrollbar(ReceiptFrame,orient=VERTICAL)
        
        self.POS_receipt = ttk.Treeview(ReceiptFrame,height=20,columns=("Item","Qty","Amount"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        self.POS_receipt.heading("Item",text="Item")
        self.POS_receipt.heading("Qty",text="Qty")
        self.POS_receipt.heading("Amount",text="Amount")
        self.POS_receipt['show']='headings'
        
        self.POS_receipt.column("Item",width=150)
        self.POS_receipt.column("Qty",width=60)
        self.POS_receipt.column("Amount",width=90)
        
        self.POS_receipt.pack(fill=BOTH,expand=1)
        ###========> Calculation Frame Content
        self.sub_total_lbl = Label(CalculationFrame,text="Sub Total",width=22)
        self.sub_total_lbl.grid(row=1,column=1)
        self.sub_total_txt = Entry(CalculationFrame,textvariable=subtotal_input,bd=2,width=25)
        self.sub_total_txt.grid(row=1,column=2,padx=2)
        
        self.tax_lbl = Label(CalculationFrame,text="Tax",width=22)
        self.tax_lbl.grid(row=2,column=1)
        self.tax_txt = Entry(CalculationFrame,textvariable=tax_input,bd=2,width=25)
        self.tax_txt.grid(row=2,column=2,padx=2)
        
        self.total_lbl = Label(CalculationFrame,text="Total",width=22)
        self.total_lbl.grid(row=3,column=1)
        self.total_txt = Entry(CalculationFrame,textvariable=total_input,bd=2,width=25)
        self.total_txt.grid(row=3,column=2,padx=2)
        ### =====> Action Buttons
       
        self.remove_item = Button(ActionFrame,width=22,height=1,bd=2,text="Remove Item",bg="blue",fg="white",command=remove_item)
        self.remove_item.grid(row=1,column=1,pady=2)
       
        self.reset_button = Button(ActionFrame,width=22,height=1,bd=2,text="Reset all",bg="red",fg="white",command=resetAll)
        self.reset_button.grid(row=1,column=2,pady=2)
        ### Table number
        self.table_lbl = Label(ActionFrame,text="Table No.",width=22)
        self.table_lbl.grid(row=2,column=1)
        self.table_input = Entry(ActionFrame,textvariable=table_input,width=25,bd=2)
        self.table_input.grid(row=2,column=2)
        #### payment type
        self.payment_type_lbl = Label(ActionFrame,text="Payment type",width=22)
        self.payment_type_lbl.grid(row=3,column=1)
        # self.payment_type = Entry(ActionFrame,textvariable="payment_type",width=25,bd=2)
        self.payment_type = OptionMenu(ActionFrame, payment_type,"Cash", "Card",command=payment_type_selected)
        self.payment_type.config(width=22,bd=2)
        self.payment_type.grid(row=3,column=2)
        #### Cash
        self.cash_lbl = Label(ActionFrame,text="Amount",width=22)
        self.cash_lbl.grid(row=4,column=1)
        self.cash_input = Entry(ActionFrame,textvariable=cash_input,width=25,bd=2)
        self.cash_input.grid(row=4,column=2)
        ### Change
        self.change_lbl = Label(ActionFrame,text="Change",width=22)
        self.change_lbl.grid(row=5,column=1)
        self.change_input = Entry(ActionFrame,textvariable=change_input,width=25,bd=2)
        self.change_input.grid(row=5,column=2)
        ######## Pay
        self.payment_button = Button(ActionFrame,padx=2,width=45,height=2,bd=2,text="Pay",bg="green",fg="white",command=change)
        self.payment_button.grid(row=6,column=1,columnspan=2,pady=3)
        ########## Exit function ########
        def exit_pos():
            window.destroy()
        ################################
        self.exit_button = Button(ActionFrame,padx=2,width=45,height=2,bd=2,text="Exit",bg="red",fg="white",command=exit_pos)
        self.exit_button.grid(row=7,column=1,columnspan=2,pady=3)
        
window = Tk()  #create blank window
app = POS(window)
window.mainloop() #Keep screen open until closed to break loop