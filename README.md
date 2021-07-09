# StockScreener
 Stock screening application that features ability to view current price, historical data, and download financial information for any stock.
 Also features the ability to search for stocks by viewing top gainers/losers/most active stocks of the day.
 
______________________________________________________________

Implementation:

I started with access to the Yahoo finance API from the **yfinance** library for the source of my data. I chose Yahoo finance since it is updated frequently and provides a large variety of data which is great for a featured stock screener.

UI: The interface is created using **tkinter** package for Python. Using tkinter I was able to create the application window as well as all of the buttons, boxes and textboxes.

Graph: The graph for the stock prices is visualized through the **Matplotlib** library. Using this library I am able to have control every detailed part of the graph including the intervals and spacing of the x/y-axis. This was very important for this project because the graph needed to be able to quickly update for different stocks with different price ranges and interval requirements.

______________________________________________________________


Challenges:

One of the biggest challenges I faced was with the updating the live stock price ticker. Tkinter is great for basic functions such as buttons but live information update without hogging resources was a bit of a challenge. I was able to solve this problem using a separate function which trigger **.after** command that allows something to be executed after a certain amount of delay.

______________________________________________________________


Takeaways:

For next time, I would definitely try to explore a different library for creating the UI. Tkinter is great as a starting point but does not allow the user to create anything more than basic shapes for UI. In this project I eventually settled on pictures for some of the buttons as a compromise to elevate the UI but would definitely prefer a built in library to generate more elegant design languages.


![alt text](https://raw.githubusercontent.com/harbirj/StockScreener/main/images/stockscreener.png)
