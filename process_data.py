from yahooquery import Ticker
import pandas as pd
import plotly.express as px # library for creating the most common figures
import plotly.graph_objects as go # Another ploting library from plotly
from plotly.subplots import make_subplots



# Let's make a reusable function to create the price indciator for different symbols
def price_indicator(symbol="aapl"):
    ticker = Ticker(symbol)
    open_price = ticker.price[symbol]["regularMarketOpen"]
    current_price = ticker.price[symbol]["regularMarketPrice"]

    delta_fig = go.Figure()

    delta_fig.add_trace(go.Indicator(
                    title = {"text": f"{symbol.upper()} Current Price"},
                    delta = {'reference': open_price, "valueformat": ".2f"},
                    mode = "number+delta",
                    value = current_price,
                    number = {"prefix": "$", "valueformat": ".2f"}))
    return delta_fig

# Another function to create charts for different tickers
def candlestick_chart(symbol="aapl", period="1y", interval="1d"):
    # Because we are creating a new python file, we need
    # to reinstantiate our ticker variable
    ticker = Ticker(symbol)
    history = ticker.history(period, interval).reset_index(level=[0,1]) # 1 year period, 1 day intervals

    fig = make_subplots(rows=2, cols=1, 
                    shared_xaxes=True, 
                    subplot_titles=(f'{symbol.upper()} OHLC', 'Volume'), 
                    row_heights=[0.7, 0.3]
                   )

    # Creates a Candlestick graph using 
    fig.add_trace(go.Candlestick(x=history['date'], 
                    open=history['open'],
                    high=history['high'],
                    low=history['low'],
                    close=history['close'],
                    showlegend=False),
                    row=1, col=1,
                 )

    fig.add_trace(go.Bar(x=history['date'], y=history['volume'], showlegend=False), row=2, col=1)
    fig.update(layout_xaxis_rangeslider_visible=False)
    
    return fig
