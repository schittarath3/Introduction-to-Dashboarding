from dash import Dash # The actual Dash app that will be run
from dash import html # Contains html components
from dash import dcc  # Contains commonly user-interaction components
from dash import Input, Output # Used for callbacks

import process_data # Our own import, used to load data from yahooquery
import news_table
import app_callbacks

# Build App
app = Dash(__name__)

price_chart = process_data.candlestick_chart("aapl", "1y", "1d")
price_metric = process_data.price_indicator("aapl")
news_table = news_table.generate_news_table("aapl")

app.layout = html.Div (
    # Children HTML elements can be nested
    children = [ # Children can be specified explicitly using the parameter tag
        html.Header( # Or implicitly
            [html.H1(children="Stock Dashboard"), 
             html.Span([
                 dcc.Input(id='my-input', type='text', placeholder="input ticker symbol", className="form-control"),
                 html.Button(id='submit-button-state', n_clicks=0, children='Submit', className="btn btn-outline-primary")],
                 className = "d-flex"
             )],
            className = "navbar"
        ),
        "This dashboard displays metrics about your favorite stock tickers",
        html.Div([
            dcc.Graph(
                id='price-metric', # IDs can be added to elements to manipulate using callbacks
                figure=price_metric
            ),
            html.Span(news_table,
                    id = "news-table")
            ], 
            id = "first-data"),
        dcc.Graph(
            id='price-history',
            figure=price_chart
        ),
    ]
)


if __name__ == '__main__':
    app.run_server(debug=True)
