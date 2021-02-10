from flask import Flask
app = Flask(__name__)    #Whenever we make a website using Flask, it's an app. Making an instance of Flask class present in flask.

@app.route('/')
def hello():
    return 'Hello World' #Until here Hello World will be printed on local host/

#To go beyond localhost/

@app.route('/Souvik')
def Souvik():
    return 'Hello Souvik. How are you doing today?'

#If you the above program run now, the program will execute but there will be no link to browse.
#For that we need to write app.run()

#app.run()
app.run(debug=True)      #Using debug=True automatically changes in the client if the code is changed here. Only the page needs to
                         #be refreshed.