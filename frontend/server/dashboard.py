import dash
import dash_core_components as dcc
import dash_html_components as html
from .riesgo_asociado import fig

# Read style of internet (css file)
external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
# Init my app dash and define my style CSS
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# Define my layout
# Adding more CSS styles
colors = {"background": "#111111", "text": "#7FDBFF"}

# Define LAYOUT
# This use HTML tags
# html.H1 : The <h1> to <h6> tags are used to define HTML headings.
# html.Div : The <div> tag defines a division or a section in an HTML document.
# app.layout = html.Div(children=[
app.layout = html.Div(
    style={"backgroundColor": colors["background"]},
    children=[
        html.Img(
            src=app.get_asset_url("Logo con corazon-01.png"),
            alt="helPharma-Team12",
            width="200",
        ),
        html.H1(
            children="Biologic therapy for Psoriasis treatment | Failure estimation diagnostic decision support system"
        ),
        html.Div(
            children="""
        Team 12 - DS4A_2020.
    """
        ),
        # html.Label('Multi-Select Dropdown of Risk Levels'),
        html.Div(
            className="row",
            children=[
                html.Div(
                    [
                        dcc.Dropdown(
                            id="dropdown-options",
                            options=[
                                {"label": "No Aplica", "value": "No Aplica"},
                                {"label": "Riesgo Alto", "value": "Riesgo Alto"},
                                {
                                    "label": "Riesgo Intermedio",
                                    "value": "Riesgo Intermedio",
                                },
                            ],
                            value=["No Aplica", "Riesgo Alto", "Riesgo Intermedio"],
                            multi=True,
                        ),
                        dcc.Graph(id="example-graph", animate=True, figure=fig),
                    ],
                    className="six columns",
                ),
                # html.Div(
                #     [
                #         dcc.Dropdown(
                #             id="dropdown-options2",
                #             options=[
                #                 {
                #                     "label": "SEGUIMIENTO PRESENCIAL",
                #                     "value": "SEGUIMIENTO PRESENCIAL",
                #                 },
                #                 {
                #                     "label": "Alta del Programa",
                #                     "value": "Alta del Programa",
                #                 },
                #             ],
                #             value=["SEGUIMIENTO PRESENCIAL", "Alta del Programa"],
                #             multi=True,
                #         ),
                #         dcc.Graph(id="example-graph2", animate=True, figure=fog),
                #     ],
                #     className="six columns",
                # ),
            ],
        ),
    ],
)
