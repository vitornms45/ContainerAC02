from flask import Flask

app = Flask(__name__)

@app.route('/')
def ra():
    return "Meu nome é Victor Nunes Moraes Silva e meu RA é 2200569"

app.run(debug=True, use_debugger=False, use_reloader=False)