from website import create_app 

app = create_app()

if __name__ == "__main__":
    app.run(debug=True) # run flask application & start off webserver and debug means it reruns webserver because debug = true.     