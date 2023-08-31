# Install and load quantmod
install.packages("quantmod")
library(quantmod)

# Define the stock symbol and the date range
stock_symbol <- "AAPL"
start_date <- as.Date("2020-01-01")
end_date <- as.Date("2021-12-31")

# Download stock price data
getSymbols(stock_symbol, from = start_date, to = end_date)

# Calculate daily returns
daily_returns <- dailyReturn(Cl(get(stock_symbol)))

# Calculate basic metrics
summary(daily_returns)

# Create a time series plot of stock prices
chartSeries(get(stock_symbol), theme = "white")

# Create a histogram of daily returns
hist(daily_returns, breaks = 30, main = "Daily Returns Histogram", xlab = "Returns")
