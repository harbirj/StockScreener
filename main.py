import tkinter as tk
from tkinter import ttk
from yahoo_fin import stock_info as si
from yahoo_fin import options

from tkinter import * 
from tkinter.ttk import *

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


from pandas import DataFrame


dow_tickers = si.tickers_dow()
sp500_tickers = si.tickers_sp500()
nasdaq_tickers = si.tickers_nasdaq()
other_tickers = si.tickers_other()



class Application(tk.Frame):
        def __init__(self, master=None):
                tk.Frame.__init__(self,master)
                self.createWidgets()

        def createWidgets(self):

                #Button images~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                photo = PhotoImage(file = r"C:\Users\User\Desktop\Python coding\finance\StockScreening\StockScreener\images\button_update.png")

                ainfo = PhotoImage(file = r"C:\Users\User\Desktop\Python coding\finance\StockScreening\StockScreener\images\button_Ainfo.png")
                bsimg = PhotoImage(file = r"C:\Users\User\Desktop\Python coding\finance\StockScreening\StockScreener\images\button_BS.png")
                cfimg = PhotoImage(file = r"C:\Users\User\Desktop\Python coding\finance\StockScreening\StockScreener\images\button_CF.png")

                dayimg = PhotoImage(file = r"C:\Users\User\Desktop\Python coding\finance\StockScreening\StockScreener\images\button_d.png")
                wkimg = PhotoImage(file = r"C:\Users\User\Desktop\Python coding\finance\StockScreening\StockScreener\images\button_wk.png")
                moimg = PhotoImage(file = r"C:\Users\User\Desktop\Python coding\finance\StockScreening\StockScreener\images\button_mo.png")

                gainimg = PhotoImage(file = r"C:\Users\User\Desktop\Python coding\finance\StockScreening\StockScreener\images\button_gain.png")
                lossimg = PhotoImage(file = r"C:\Users\User\Desktop\Python coding\finance\StockScreening\StockScreener\images\button_lose.png")
                actimg = PhotoImage(file = r"C:\Users\User\Desktop\Python coding\finance\StockScreening\StockScreener\images\button_act.png")


                #Title~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                ghost = tk.Label(font=("Calibri", 24), 
                        width=7,
                        background="gray15"  
                )
                ghost.grid(row=0,column=0, sticky='w') 

                ghost2 = tk.Label(font=("Calibri", 24), 
                        width=6,
                        background="gray15"  
                )
                ghost2.grid(row=0,column=3, sticky='w')

                greeting = tk.Label(text="Stock Screener",
                        font=("Calibri", 24), 
                        width=50,
                        foreground="white",  
                        background="gray15"  
                )
                greeting.grid(row=0,column=1, sticky='w')    
                
                #Ticker live~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                live = tk.Label(text="Current Price:",
                        font=("Calibri", 12), 
                        width=11,
                        fg='white',
                        background="gray25"  
                )
                live.grid(row=1,column=0, sticky='w') 

                self.price = tk.Label(font=("Calibri", 12), 
                        width=10,
                        fg='white',
                        background="gray25"  
                )
                self.price.grid(row=2,column=0,sticky='nw')


                #Ticker Search~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                search_box = tk.Frame(
                        master=root,
                        background="gray25",
                        borderwidth=1
                )
                search_box.grid(row=1,column=1)

                self.entry = tk.Entry(master = search_box,fg="black", bg="white", width=20)
                self.entry.insert(0, "MSFT")
                self.entry.grid(row=1,column=2,sticky="w")


                hint = tk.Label(master = search_box,
                        text="Enter ticker (eg. MSFT)",
                        background="gray25",
                        fg= 'white', 
                        width=20,
                )
                hint.grid(row=1,column=1,padx =5,sticky="e")  



                #Chart~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                fig=plt.figure(figsize=(8,4))
                fig.patch.set_facecolor('lightgray')
                ax=fig.add_subplot(111)
                canvas=FigureCanvasTkAgg(fig,master=root)
                canvas.get_tk_widget().grid(row=3,column=1,sticky="w")

                self.update_btn = tk.Button(
                        master=root,
                        text="Update",
                        font=("Calibri", 13),
                        activebackground='gray25',
                        bg="gray25",
                        borderwidth=0,
                        fg="white",
                        image = photo,
                        command=lambda: self.plot(canvas,
                                ax, 
                                self.entry.get(), 
                                interval_value["text"],
                                self.strtDateEntry.get(),
                                self.endDateEntry.get())
                )
                self.update_btn.image= photo
                self.update_btn.grid(row=2,column=1, padx=3, pady=3)


                #Intervals~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                def dayDisplay():
                        interval_value["text"] = "1d"

                def weekDisplay():
                        interval_value["text"] = "1wk"

                def monthDisplay():
                        interval_value["text"] = "1mo"


                intervals = tk.Frame(
                        master=root,
                        background="gray25",
                        borderwidth=1
                )
                intervals.grid(row=4,column=1, pady=1, sticky="w")

                interval_text = tk.Label(master = intervals,
                        text="Current interval: ",
                        background="gray25",
                        fg='white', 
                )
                interval_text.grid(row=1,column=0)  

                interval_value = tk.Label(master=intervals,
                        width = 6,
                        relief=tk.RIDGE, 
                        text="1d")
                interval_value.grid(row=1, column=1)

                self.oned_btn = tk.Button(
                        master=intervals,
                        text="1d",
                        activebackground='gray25',
                        bg="gray25",
                        borderwidth=0,
                        fg="white",
                        image = dayimg,
                        command=lambda: dayDisplay()
                )
                self.oned_btn.image= dayimg
                self.oned_btn.grid(row=1,column=2, padx=5)

                self.week_btn = tk.Button(
                        master=intervals,
                        text="1wk",
                        activebackground='gray25',
                        bg="gray25",
                        borderwidth=0,
                        fg="white",
                        image = wkimg,
                        command=lambda: weekDisplay()
                )
                self.week_btn.image= wkimg
                self.week_btn.grid(row=1,column=3, padx=5)

                self.month_btn = tk.Button(
                        master=intervals,
                        text="1mo",
                        activebackground='gray25',
                        bg="gray25",
                        borderwidth=0,
                        fg="white",
                        image = moimg,
                        command=lambda: monthDisplay()
                )
                self.month_btn.image= moimg
                self.month_btn.grid(row=1,column=4, padx=5)


                #Date selection~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                dateFrame = tk.Frame(
                        master=root,
                        background="gray25",
                        borderwidth=1
                )
                dateFrame.grid(row=5,column=1, pady=3)

                stdateFrame = tk.Frame(
                        master=dateFrame, 
                        background="gray25" 
                )
                stdateFrame.grid(row=1,column=1, padx = 20, sticky="w")

                startdate_text = tk.Label(master = stdateFrame,
                        text="Start Date: ",
                        foreground="white",  
                        background="gray25"  
                )
                startdate_text.grid(row=1,column=0)  

                self.strtDateEntry = tk.Entry(master = stdateFrame,fg="black", bg="white", width=10)
                self.strtDateEntry.insert(0, "01/01/2021")
                self.strtDateEntry.grid(row=1,column=1)

                edateFrame = tk.Frame(
                        master=dateFrame,  
                        background="gray25" 
                )
                edateFrame.grid(row=1,column=2,padx = 20, sticky="e")

                enddate_text = tk.Label(master = edateFrame,
                        text="End Date: ", 
                        foreground="white",  
                        background="gray25" 
                )
                enddate_text.grid(row=1,column=1)  

                self.endDateEntry = tk.Entry(master = edateFrame,fg="black", bg="white", width=10)
                self.endDateEntry.insert(0, "02/17/2021")
                self.endDateEntry.grid(row=1,column=2)

                #Info Downloads~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                


                infoframe = tk.Frame(
                        master=root,
                        background="gray25", 
                        borderwidth=1
                )
                infoframe.grid(row=6,column=1, pady=15)

                down_text = tk.Label(master = infoframe,
                        font=("Calibri", 12),
                        background="gray25",
                        fg= 'white',
                        text="Download: ", 
                )
                down_text.grid(row=1,column=0)  


                self.anal_btn = tk.Button(
                        master=infoframe,
                        text="Analyst Info",
                        bg="gray25",
                        fg="black",
                        activebackground='gray25',
                        borderwidth=0,
                        image = ainfo,
                        command=lambda: self.down_anal(self.entry.get())
                )
                self.anal_btn.image= ainfo
                self.anal_btn.grid(row=1,column=2, padx=10)

                self.bs_btn = tk.Button(
                        master=infoframe,
                        text="Balance Sheet",
                        bg="gray25",
                        fg="black",
                        activebackground='gray25',
                        borderwidth=0,
                        image = bsimg,
                        command=lambda: self.down_bs(self.entry.get())
                )
                self.bs_btn.image=bsimg
                self.bs_btn.grid(row=1,column=3, padx=10)

                self.cf_btn = tk.Button(
                        master=infoframe,
                        text="Cash Flows",
                        bg="gray25",
                        fg="black",
                        activebackground='gray25',
                        borderwidth=0,
                        image = cfimg,
                        command=lambda: self.down_cf(self.entry.get())
                )
                self.cf_btn.image=cfimg
                self.cf_btn.grid(row=1,column=4, padx=10)

                researchframe = tk.Frame(
                        master=root,
                        background="gray25", 
                        width=100,
                        borderwidth=1
                )
                researchframe.grid(row=7,column=1, pady=15)

                self.gain_btn = tk.Button(
                        master=researchframe,
                        activebackground='gray25',
                        bg="gray25",
                        borderwidth=0,
                        fg="white",
                        image = gainimg,
                        command = lambda: self.topg()
                )
                self.gain_btn.image= gainimg
                self.gain_btn.grid(row=1,column=2, padx=50)

                self.loss_btn = tk.Button(
                        master=researchframe,
                        activebackground='gray25',
                        bg="gray25",
                        borderwidth=0,
                        fg="white",
                        image = lossimg,
                        command = lambda: self.topl()
                )
                self.loss_btn.image= lossimg
                self.loss_btn.grid(row=1,column=3, padx=50)

                self.active_btn = tk.Button(
                        master=researchframe,
                        activebackground='gray25',
                        bg="gray25",
                        borderwidth=0,
                        fg="white",
                        image = actimg,
                        command = lambda: self.topact()
                )
                self.active_btn.image= actimg
                self.active_btn.grid(row=1,column=4, padx=50)

                dispframe = tk.Frame(
                        master=root,
                        background="white", 
                        borderwidth=1
                )
                dispframe.grid(row=8,column=0,columnspan =5, pady=3,sticky="w")


                cols = ('Symbol','Name','Price (Intraday)','Change','% Change')
                self.listBox = ttk.Treeview(master=dispframe,
                        columns=cols,
                        show='headings')
                # set column headings
                for col in cols:
                        self.listBox.heading(col, text=col)  
                self.listBox.pack(side='left')


                self.vsb = ttk.Scrollbar(master=dispframe, orient="vertical", command=self.listBox.yview)
                self.vsb.pack(side='right', fill='y')

                self.listBox.configure(yscrollcommand=self.vsb.set)

                
        def down_anal(self,ticker):
               info = si.get_analysts_info(ticker)
               filename = ticker + 'AnalystInfo.txt'
               f = open(filename, "x") 
               print(info, file=f)

        def down_bs(self,ticker):
                balance = si.get_balance_sheet(ticker) 
                filename = ticker + 'BalanceSheet.txt'
                f = open(filename, "x") 
                print(balance, file=f)

        def down_cf(self,ticker):
                cashf = si.get_cash_flow(ticker) 
                filename = ticker + 'CashFlow.txt'
                f = open(filename, "x") 
                print(cashf, file=f)
                

        def topg(self):
                topgain = si.get_day_gainers()

                self.listBox.delete(*self.listBox.get_children())
                for x in range(25):
                        self.listBox.insert("", "end", values=(topgain.loc[x,'Symbol'],
                                topgain.loc[x,'Name'],
                                '$' + str(topgain.loc[x,'Price (Intraday)']),
                                '+' + str(topgain.loc[x,'Change']),
                                topgain.loc[x,'% Change']))

        def topl(self):
                toploss = si.get_day_losers()

                self.listBox.delete(*self.listBox.get_children())
                for x in range(25):
                        self.listBox.insert("", "end", values=(toploss.loc[x,'Symbol'],
                                toploss.loc[x,'Name'],
                                '$' + str(toploss.loc[x,'Price (Intraday)']),
                                toploss.loc[x,'Change'],
                                toploss.loc[x,'% Change']))        
                     
        def topact(self):
                topact = si.get_day_most_active()

                self.listBox.delete(*self.listBox.get_children())
                for x in range(25):
                        self.listBox.insert("", "end", values=(topact.loc[x,'Symbol'],
                                topact.loc[x,'Name'],
                                '$' + str(topact.loc[x,'Price (Intraday)']),
                                topact.loc[x,'Change'],
                                topact.loc[x,'% Change']))   
        
        

        def plot(self,canvas,ax, ticker, interval,stDate,eDate):
                
                answer = si.get_live_price(ticker)
                self.price["text"] = '  $' + str("{:6.2f}".format(answer))

                ax.clear()         # clear axes from previous plot

                
                df1 = si.get_data(ticker, start_date = stDate, end_date = eDate, interval = interval)
                df1['close'].plot(kind='line', 
                        legend=True, 
                        ax=ax, 
                        color='xkcd:lightish blue',
                        marker='.', 
                        fontsize=10)
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)
                ax.set_facecolor("whitesmoke")
                ax.set_title(ticker + ' chart')
                ax.set_ylabel('Share prices ($)')
                ax.set_xlabel('Date')
                ax.grid(b=None, which='major', axis='both')
                canvas.draw()

        

root=tk.Tk()
root.title("Stock Screener")
root.configure(bg='gray25')
app=Application(master=root)
app.mainloop()


