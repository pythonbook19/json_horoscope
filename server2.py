from bottle import route, run, view
from horoscope import generate_prophecies
from datetime import datetime as dt
from random import random


@route("/")
@view("predictions222")
def index():
  now = dt.now()

  x = random()

  return {
    "date": f"{now.year}-{now.month}-{now.day}",
    "prophecies": generate_prophecies(5,3),
    "special_date": x > 0.5,
    "x": x,
  }


run(
  host="localhost",
  port=8097,
  debug=True
)
