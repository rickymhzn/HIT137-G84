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
        self.window.geometry("1366x768")
        self.window.title("Point of Sale")
        self.window.configure(background='white')
       
        change_input = StringVar()
        cash_input = StringVar()
        tax_input = StringVar()
        subtotal_input = StringVar()
        total_input = StringVar()
        item = StringVar()
        qty = StringVar()
        amount = StringVar()
        choice = StringVar()

       
        #Creating Main Frame for content
        MainFrame = Frame(self.window, bg="white")
        MainFrame.grid(padx=8,pady=8)
        ###=========> Create Menu frame for Food and Items
        MenuFrame = Frame(MainFrame, bg="white", bd=3 , width=1000, height=758, padx=5, pady=5, relief=RIDGE)
        MenuFrame.pack(side=LEFT)
        ###======> Receipt Frame for listing items
        ReceiptFrame = Frame(MainFrame, bg="white", bd=3 , width=350, height=300, padx=5, pady=5, relief=RIDGE)
        ReceiptFrame.pack(side=TOP)
        ###======> Calculation Frame for listing items
        CalculationFrame = Frame(MainFrame, bg="white", bd=3 , width=350, height=400, padx=5, pady=5, relief=RIDGE)
        CalculationFrame.pack(side=TOP)
        ###======> Action Frame for listing items
        ActionFrame = Frame(MainFrame, bg="white", bd=3 , width=350, height=50, padx=5, pady=5, relief=RIDGE)
        ActionFrame.pack(side=TOP)
        ###========> Menu Frame Content
        #create a tab based menu
        menu_tab = ttk.Notebook(MenuFrame,width=995,height=740)
        menu_button_height = 3 #all menu button height
        menu_button_width = 15 #all menu button width
        menu_button_font = font.Font(size=14,family='Helvetica') #all menu button Fonts
        #creating new tabs using frame widget
        food_menu_tab = Frame(menu_tab,width=955, height=755)
        drinks_meun_tab = Frame(menu_tab,width=955, height=755)
        special_menu_tab = Frame(menu_tab,width=955, height=755)

        menu_tab.add(food_menu_tab,text="Food")
        menu_tab.add(drinks_meun_tab, text="Drinks")
        menu_tab.add(special_menu_tab, text="Special")
        menu_tab.pack(expand=1, fill="both")
        ### Food menu tab content  ###
        ############# Menu additem button Function ##############
        def mixed_olives():
            price = 5.3
            tax = 3
            self.POS_receipt.insert("",'end',values=("Mixed Olives", "1","5.3"))
            for child in self.POS_receipt.get_children():
                price += float(self.POS_receipt.item(child,"values")[2])
                subtotal_input.set(str(price))
                # tax_input.set(str('$%.2f'%(((price-5.3)*tax)/100)))
                # total_input.set(str('$%.2f'%((price-5.3)+((price-5.3)*tax))))   
        def add_item(title,item_price):
            # price = 5.3
            tax = 3
            self.POS_receipt.insert("",'end',values=(title, "1",item_price))
            for child in self.POS_receipt.get_children():
                price = item_price+float(self.POS_receipt.item(child,"values")[2])
                subtotal_input.set(str('$%.2f'%(price-item_price)))
                tax_input.set(str('$%.2f'%(((price-item_price)*tax)/100)))
                total_input.set(str('$%.2f'%((price-item_price)+((price-item_price)*tax))))            
                
        self.mixed_olives = Button(food_menu_tab, padx=10,pady=10,width=menu_button_width,height=menu_button_height,font=menu_button_font,text='Mixed Olives',command=mixed_olives)
        self.mixed_olives.grid(row=1,column=1,padx=2,pady=2)
        self.foccacia = Button(food_menu_tab, padx=10,pady=10,width=menu_button_width,height=menu_button_height,font=menu_button_font,text='Foccacia',command=lambda: add_item("Foccacia",2.3))
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
        ### Drinks menu tab content ###
        self.button1 = Button(drinks_meun_tab, padx=2,pady=2,text='Hello')
        self.button1.grid(row=1,column=1,padx=2,pady=2)

        ### Special menu tab content ### 
        self.button1 = Button(special_menu_tab, padx=2,pady=2,text='Hello')
        self.button1.grid(row=0,column=1,padx=2,pady=2)
        #### Menu buttons Actions #####
        # def mixed_olives_callback():
        #     pritn
       
     
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
        
        self.POS_receipt.column("Item",width=120)
        self.POS_receipt.column("Qty",width=100)
        self.POS_receipt.column("Amount",width=100)
        
        self.POS_receipt.pack(fill=BOTH,expand=1)
        ###========> Receipt Frame Content
        self.sub_total_lbl = Label(CalculationFrame,text="Sub Total", bd=3)
        self.sub_total_lbl.grid(row=1,column=1)
        self.sub_total_txt = Entry(CalculationFrame,textvariable="subtotal_input",bd=1,width=24)
        self.sub_total_txt.grid(row=1,column=2,padx=3)
        
        self.tax_lbl = Label(CalculationFrame,text="Tax", bd=3)
        self.tax_lbl.grid(row=2,column=1)
        self.tax_txt = Entry(CalculationFrame,textvariable="tax_input",bd=1,width=24)
        self.tax_txt.grid(row=2,column=2,padx=3)
        
        self.total_lbl = Label(CalculationFrame,text="Total", bd=3)
        self.total_lbl.grid(row=3,column=1)
        self.total_txt = Entry(CalculationFrame,textvariable="total_input",bd=1,width=24)
        self.total_txt.grid(row=3,column=2,padx=3)
        ### =====> Action Buttons
      
        
       ###### Remove item function ####
        def remove_item():
            price = 0.0
            tax = 2.5
            for item in self.POS_receipt.get_children():
                price += float(self.POS_receipt.item(item,"values")[2])
            subtotal_input.set(str('$%.2f'%(price)))
            tax_input.set(str('$%.2f'%((price * tax)/100)))
            total_input.set(str('$%.2f'%((price)+((price *tax)/100))))
            selected_item = (self.POS_receipt.selection()[0])
            self.POS_receipt.delete(selected_item)
        #################################    
        self.remove_item = Button(ActionFrame,padx=2,width=10,height=1,bd=2,text="Remove Item",command=remove_item)
        self.remove_item.grid(row=1,column=1,pady=2)
        ######### Reset all function #######
        def resetAll():
            for item in self.POS_receipt.get_children():
                self.POS_receipt.delete(item)
        ####################################
        self.reset_button = Button(ActionFrame,padx=2,width=10,height=1,bd=2,text="Reset all",command=resetAll)
        self.reset_button.grid(row=1,column=2,pady=2)
        
        self.payment_button = Button(ActionFrame,padx=2,width=10,height=1,bd=2,text="Pay")
        self.payment_button.grid(row=2,column=1,pady=2)
        ########## Exit function ########
        def exit_pos():
            window.destroy()
        ################################
        self.exit_button = Button(ActionFrame,padx=2,width=10,height=1,bd=2,text="Exit",command=exit_pos)
        self.exit_button.grid(row=3,column=1,pady=2)
        
window = Tk()  #create blank window
app = POS(window)
window.mainloop() #Keep screen open until closed to break loop