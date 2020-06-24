from yahoo_fin import stock_info as si #to get share market price
import yfinance as yf #gives market data from yahoo_finance
import matplotlib.pyplot as plt #to plot results

#gets live price of Apple
x=si.get_live_price("aapl")

#prints them in dollars
print("$",x)

#downloads automatically the data of apple for the given time
data = yf.download('AAPL','2020-06-01','2020-06-23')

plt.xlabel('Time',fontsize=20)
plt.ylabel('Rate in $',fontsize=20)

data.Close.plot()

plt.show()
