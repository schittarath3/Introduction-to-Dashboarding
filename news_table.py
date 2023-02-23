from dash import html
from dash import dcc
import yahooquery as yq
from datetime import datetime 


# Generates html table with the latest articles for company associated with ticker
def generate_news_table(symbol="aapl", limit=5):
    news_raw = yq.search(symbol)["news"][:limit] # get the latest n articles for the ticker from yq
    return html.Table(
        [html.Tr([html.Th("News", colSpan=3)], # creates header
                 id = "news-table-header")] + 
        [html.Tr(
           [html.Td(html.Img(src=article["thumbnail"]["resolutions"][-1]["url"], height="70px", width="70px") 
                    if "thumbnail" in article else ""), # loads thumbnail
            html.Td(html.A(article["publisher"] + ": " + article["title"], href=article["link"], 
                           target="_blank", rel="noopener noreferrer")), # creates hyperlink
            html.Td(datetime.fromtimestamp(article["providerPublishTime"]).strftime("%d/%m/%Y, %H:%M:%S"))] # creates time from epoch
        ) for article in news_raw],
        className = "table"
    )
