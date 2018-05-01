from flask import Flask, render_template, request, redirect, session, flash
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = "NinjaGold"

gold = 0
low = [10, 5, 2, -50]
high = [20, 10, 5, 50]
history = []
locations = ['Farm','Cave', 'House', 'Casino']
len_locations = len(locations)

@app.route('/')
def index():
    global gold
    history_length = len(history)
    return render_template('index.html', history=history,
            history_length=history_length, low=low, high=high,
            locations=locations, len_locations=len_locations,
            gold=gold)

@app.route('/process_money', methods=['post'])
def process_money():
    global gold
    # When an action is taken, identify the place_position. This will idicate
    # which list index to use for data from the low/high list and locations
    # list.
    position_request = int(request.form['place_position'])
    gain = random.randrange(low[position_request], high[position_request])
    #print(gain)
    gold += gain
    history.append("You entered a " + str(request.form['location']) 
    + " and gained " + str(gain) + " @ " + str(datetime.now()))
    #print(history)
    return redirect('/')

@app.route('/reset', methods=['post'])
def reset():
    global gold
    while len(history) > 0:
        history.pop()
    gold = 0
    return redirect('/')

app.run(debug=True)
