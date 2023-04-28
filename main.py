import random
import time
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
#from threading import Thread, Event


#enviar datos en vivo
app = Flask(__name__)
app.config['SECRET_KEY']="secret"
socket = SocketIO(app)

'''
lista = ['hola', 'adios', 'hello', 'goodbye']
i=0
'''

#importa el html(web)
@app.route("/")
def main():
        return render_template("index.html")


@socket.on('message')
def msghand(msg):
        while True:
            data = {'value': random.randint(0, 100)}
            time.sleep(0.1)
            emit('data', data)




#    global i
#    if i< len(lista):
#       socket.send(lista[i])
#       i+=1


if __name__ == '__main__':
    app.run(debug=True)
