from flask import Flask

app = Flask(__name__)
print(__name__)

@app.route('/index')
@app.route('/')
def index():
    return <html><head><title>Hotels</title></head><body><h1> Hello! </h1></body></html>


# so now let's detect whether or not the app is running as a standalone; if so run it on flask buit-in development server.
# in order to do so, we're gonna use a decision construct:
if __name__ == "__main__":
    app.run(debug=True) # debug=True because we're running in development mode, not in production mode
    
