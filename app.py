from flask import Flask, render_template

app = Flask('FullCalendar Demo')

events = [
  {
    'todo' : 'Tutorial for Boris',
    'date' : '2020-12-07',
  },
  {
    'todo' : 'Eat Hotpot',
    'date' : '2020-12-08',
  }
]

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/calendar')
def calendar():
  return render_template('calendar.html', events = events)