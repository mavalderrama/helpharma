import sys
from server import app

# Configuring APP running as Web
if __name__ == "__main__":
    # app.run_server(debug=True)
    if len(sys.argv) > 1:
        app.run_server(host="0.0.0.0", port=sys.argv[1])
    else:
        app.run_server(host="0.0.0.0", port=8080, debug=True)
