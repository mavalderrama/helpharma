# coding=utf-8

import dash_html_components as html

title = html.Div(
    className="title", children=[html.H1("About Team 12 Players")], id="models_title",
)


layout = html.Div(
    [
        html.H1("About Team 12 Players"),
        html.Div(
            html.Div(
                [
                    html.Label(
                        "Alvaro Brunal",
                        style={"font-weight": "bold", "font-size": "x-large"},
                    ),
                    html.Div("Sales and Slides Guy"),
                    html.Label(
                        "Juan Pablo Daza",
                        style={"font-weight": "bold", "font-size": "x-large"},
                    ),
                    html.Div("TCP/IP 4000"),
                    html.Label(
                        "Alejandro Valderrama",
                        style={"font-weight": "bold", "font-size": "x-large"},
                    ),
                    html.Div("Master Jedi"),
                    html.Label(
                        "Camilo Cardona",
                        style={"font-weight": "bold", "font-size": "x-large"},
                    ),
                    html.Div("Mountain Climber and Data Watcher"),
                    html.Label(
                        "Jean Pierre Díaz",
                        style={"font-weight": "bold", "font-size": "x-large"},
                    ),
                    html.Div("Algorithm Virtuoso"),
                    html.Label(
                        "Jorge Rivera",
                        style={"font-weight": "bold", "font-size": "x-large"},
                    ),
                    html.Div("Family Man and Dog Lover"),
                ]
            ),
            style={"text-align": "center"},
        ),
        html.H1("Teachers", style={"padding-top": "50px", "padding-bottom": "15px"}),
        html.Div(
            html.Div(
                [
                    html.Label(
                        "Natesh Pillai",
                        style={"font-weight": "bold", "font-size": "x-large"},
                    ),
                    html.Div("Beat it Guy"),
                    html.Label(
                        "Jimmy Jing",
                        style={"font-weight": "bold", "font-size": "x-large"},
                    ),
                    html.Div("Fast and Furious"),
                    html.Label(
                        "German Prieto",
                        style={"font-weight": "bold", "font-size": "x-large"},
                    ),
                    html.Div("El Tiburón de la Montaña"),
                ]
            )
        ),
    ],
    style={"text-align": "center"},
)
