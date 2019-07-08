import os
from flask import Flask
app = Flask(__name__)
@app.route("/")
def main():
  return "WelCome Ajay !!! "

@app.route("/how are you")
def hello():
  return "I am good  , Thank you !!! "

if __name__ == "__main__":
  app.run()         
