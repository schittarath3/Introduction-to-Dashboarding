from dash import Dash # The actual Dash app that will be run
from dash import html # Contains html components
from dash import dcc  # Contains commonly user-interaction components
from dash import Input, Output # Used for callbacks

import process_data # Our own import, used to load data from yahooquery
import news_table 
import app_callbacks

# Build App
app = Dash(__name__)

# YOUR CODE HERE #1


app.layout = html.Div (
    # Children HTML elements can be nested
    children = [ # Children can be specified explicitly using the parameter tag
        html.Header( # Or implicitly
            [html.H1(children="Stock Dashboard"), 
             html.Span([
                 dcc.Input(id='my-input', type='text', placeholder="input ticker symbol", className="ADD CLASS HERE 1"),
                 html.Button(id='submit-button-state', n_clicks=0, children='Submit', className="ADD CLASS HERE 2")],
                 className = "d-flex"
             )],
            className = "ADD CLASS HERE 3"
        ),
        # YOUR CODE HERE #2
    ]
)


if __name__ == '__main__':
    app.run_server(debug=True)
