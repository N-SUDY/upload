#Thank you LazyDeveloper for helping developers in this journey !
#Must Subscribe On YouTube @L_S_MEENA 

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '@CHATWITHANOTHERbot'


if __name__ == "__main__":
    app.run()
