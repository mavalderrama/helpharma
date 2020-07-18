import sys
from dash.dependencies import Input, Output
import plotly.express as px
from server import app, ct


@app.callback(
    Output(component_id="example-graph", component_property="figure"),
    [Input(component_id="dropdown-options", component_property="value")],
)
def update_figure(input_value):
    figure = px.bar(ct, x="Consultas_totales", y=input_value, barmode="group")
    return figure


# Configuring APP running as Web
if __name__ == "__main__":
    # app.run_server(debug=True)
    if len(sys.argv) > 1:
        app.run_server(host="0.0.0.0", port=sys.argv[1])
    else:
        app.run_server(host="0.0.0.0", port=8080)
