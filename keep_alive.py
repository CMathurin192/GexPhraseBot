#Caleb Mathurin 05/30/2021 - all the code in this file sets up a server to run this script on (from: https://youtu.be/S6pBLq8Jv_A)
from flask import Flask
from threading import Thread

app = Flask("")

@app.route("/")
def home():
  return "I'm alive"

def run():
  app.run(host = "0.0.0.0", port = 8080)

def keep_alive():
  t = Thread(target = run)
  t.start()