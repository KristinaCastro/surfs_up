# import Flask
from flask import Flask

# Create an app being sure to pass __name__
app = Flask(__name__)

# Define what to do when a user goes to the index route 
@app.route('/')
def hello_world():
    return 'Hello world'

if __name__ == "__main__":
    app.run(debug=True)
    

    
