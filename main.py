import tkinter as tk
from tkinter import ttk
from yahoo_fin import stock_info as si
from yahoo_fin import options

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
                
                #Title~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                ghost = tk.Label(font=("Calibri", 20), 
                        width=5,
                        background="black"  # Set the background color to black
                )
                ghost.grid(row=0,column=0) 

                ghost2 = tk.Label(font=("Calibri", 20), 
                        width=5,
                        background="black"  # Set the background color to black
                )
                ghost2.grid(row=0,column=3)

                greeting = tk.Label(text="Stock Screener",
                        font=("Calibri", 20), 
                        width=65,
                        foreground="white",  # Set the text color to white
                        background="black"  # Set the background color to black
                )
                greeting.grid(row=0,column=1)    
                

                #Ticker Search~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                search_box = tk.Frame(
                        master=root,
                        borderwidth=1
                )
                search_box.grid(row=1,column=1)

                self.entry = tk.Entry(master = search_box,fg="black", bg="white", width=27)
                self.entry.insert(0, "MSFT")
                self.entry.grid(row=1,column=2)


                hint = tk.Label(master = search_box,
                        text="Enter ticker eg. MSFT", 
                        width=30,
                )
                hint.grid(row=1,column=3,sticky="w")  



                #Chart~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                fig=plt.figure(figsize=(8,4))
                ax=fig.add_subplot(111)
                canvas=FigureCanvasTkAgg(fig,master=root)
                canvas.get_tk_widget().grid(row=3,column=1,sticky="w")

                self.update_btn = tk.Button(
                        master=root,
                        text="Update Chart",
                        font=("Calibri", 14),
                        width=15,
                        height=1,
                        bg="black",
                        fg="white",
                        command=lambda: self.plot(canvas,
                                ax, 
                                self.entry.get(), 
                                interval_value["text"],
                                self.strtDateEntry.get(),
                                self.endDateEntry.get())
                )
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
                        borderwidth=1
                )
                intervals.grid(row=4,column=1, pady=3, sticky="w")

                interval_text = tk.Label(master = intervals,
                        text="Current interval: ", 
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
                        width=3,
                        height=1,
                        command=lambda: dayDisplay()
                )
                self.oned_btn.grid(row=1,column=2, padx=10)

                self.week_btn = tk.Button(
                        master=intervals,
                        text="1wk",
                        width=3,
                        height=1,
                        command=lambda: weekDisplay()
                )
                self.week_btn.grid(row=1,column=3, padx=10)

                self.month_btn = tk.Button(
                        master=intervals,
                        text="1mo",
                        width=3,
                        height=1,
                        command=lambda: monthDisplay()
                )
                self.month_btn.grid(row=1,column=4, padx=10)


                #Date selection~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                dateFrame = tk.Frame(
                        master=root,
                        borderwidth=1
                )
                dateFrame.grid(row=5,column=1, pady=3)

                stdateFrame = tk.Frame(
                        master=dateFrame,
                )
                stdateFrame.grid(row=1,column=1, padx = 20, sticky="w")

                startdate_text = tk.Label(master = stdateFrame,
                        text="Start Date: ", 
                )
                startdate_text.grid(row=1,column=0)  

                self.strtDateEntry = tk.Entry(master = stdateFrame,fg="black", bg="white", width=10)
                self.strtDateEntry.insert(0, "01/01/2021")
                self.strtDateEntry.grid(row=1,column=1)

                edateFrame = tk.Frame(
                        master=dateFrame,
                )
                edateFrame.grid(row=1,column=2,padx = 20, sticky="e")

                enddate_text = tk.Label(master = edateFrame,
                        text="End Date: ", 
                )
                enddate_text.grid(row=1,column=1)  

                self.endDateEntry = tk.Entry(master = edateFrame,fg="black", bg="white", width=10)
                self.endDateEntry.insert(0, "02/17/2021")
                self.endDateEntry.grid(row=1,column=2)

                #Info Downloads~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                


                infoframe = tk.Frame(
                        master=root,
                        background="black", 
                        borderwidth=1
                )
                infoframe.grid(row=6,column=1, pady=3)

                down_text = tk.Label(master = infoframe,
                        font=("Calibri", 12),
                        text="Download: ", 
                )
                down_text.grid(row=1,column=0)  


                self.anal_btn = tk.Button(
                        master=infoframe,
                        text="Analyst Info",
                        height=1,
                        command=lambda: self.down_anal(self.entry.get())
                )
                self.anal_btn.grid(row=1,column=2, padx=10)

                self.bs_btn = tk.Button(
                        master=infoframe,
                        text="Balance Sheet",
                        height=1,
                        command=lambda: self.down_bs(self.entry.get())
                )
                self.bs_btn.grid(row=1,column=3, padx=10)

                self.cf_btn = tk.Button(
                        master=infoframe,
                        text="Cash Flows",
                        height=1,
                        command=lambda: self.down_cf(self.entry.get())
                )
                self.cf_btn.grid(row=1,column=4, padx=10)

                researchframe = tk.Frame(
                        master=root,
                        background="blue", 
                        borderwidth=1
                )
                researchframe.grid(row=7,column=1, pady=3)

                self.gain_btn = tk.Button(
                        master=researchframe,
                        text="Top day gainers",
                        height=1,
                        command = lambda: self.topg()
                )
                self.gain_btn.grid(row=1,column=2, padx=10)

                self.loss_btn = tk.Button(
                        master=researchframe,
                        text="Top day losers",
                        height=1,
                        command = lambda: self.topl()
                )
                self.loss_btn.grid(row=1,column=3, padx=10)

                self.active_btn = tk.Button(
                        master=researchframe,
                        activebackground='black'
                        ,activeforeground='green'
                        ,background='black'
                        ,foreground='lime'
                        ,relief='solid',
                        text="Top most active",
                        height=1,
                        command = lambda: self.topact()
                )
                self.active_btn.grid(row=1,column=4, padx=10)

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
                
                ax.clear()         # clear axes from previous plot

                
                df1 = si.get_data(ticker, start_date = stDate, end_date = eDate, interval = interval)
                df1['close'].plot(kind='line', 
                        legend=True, 
                        ax=ax, 
                        color='b',
                        marker='o', 
                        fontsize=10)
                ax.set_title(ticker + ' chart')
                ax.set_ylabel('Share prices ($)')
                ax.set_xlabel('Date')
                ax.grid(b=None, which='major', axis='both')
                canvas.draw()
                


root=tk.Tk()
root.title("Stock Screener")
app=Application(master=root)
app.mainloop()


