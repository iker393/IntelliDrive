import random
import time
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
#from threading import Thread, Event


app = Flask(__name__)
app.config['SECRET_KEY']="secret"
socket = SocketIO(app)


# Useless list, made for first testing
'''
lista = ['hola', 'adios', 'hello', 'goodbye']
i=0
'''

#Render HTML
@app.route("/")
def main():
        return render_template("index.html")

#What should process data, gathered with what's on OBDTests
@socket.on('message')
def msghand(msg):
        while True:
            data = {'value': random.randint(0, 100)}
            time.sleep(0.1)
            emit('data', data)


# What handled the list, needs to be removed
'''
    global i
    if i< len(lista):
       socket.send(lista[i])
       i+=1
'''

if __name__ == '__main__':
    app.run(debug=True)
