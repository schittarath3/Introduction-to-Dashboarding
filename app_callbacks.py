import process_data # Our own import, used to load data from yahooquery
import news_table
import dash
from dash import Input, Output, State


@dash.callback(
    Output(component_id='price-history', component_property='figure'), #specifies the two outputs components and which
    Output(component_id='price-metric', component_property='figure'), # part of the component
    Output(component_id="news-table", component_property='children'),
    Input(component_id='my-input', component_property='value'), # specifies where to look for a change
    prevent_initial_call = True
)
def update_output_div(symbol):
    # returns the figure to the target component property BASED ON THE ORDER OF OUTPUTS
    return process_data.candlestick_chart(symbol, "1y", "1d"), process_data.price_indicator(symbol), news_table.generate_news_table(symbol)
