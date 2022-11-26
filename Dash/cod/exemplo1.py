from dash import Dash, html, dcc


app = Dash(__name__)

app.layout=html.Div(
    children=[
        html.H1('Boas vindas'),
        dcc.Graph(
            figure={
                'data':[
                    {'y':[1,2,3,4], 'type':'line', 'name':'A'},
                    {'y':[1,2,3,4], 'type':'box', 'name':'B'},
                ],
                'layout':{

                }
            }
        )
        ]
    )

app.run_server(debug=True)