from flask import Flask

app = Flask(__name__)

@app.route('/')
def ra():
    return "Meu RA é 2200569"

app.run(debug=True, use_debugger=False, use_reloader=False)