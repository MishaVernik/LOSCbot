from flask import Flask, request
import urllib.request
import requests
import time
from threading import Timer


app = Flask(__name__)
app.config['DEBUG'] = False
print("START __ 0001")
check_if_one = 0
what_now = 0
number_of_repeats = 0
sleeping_time = 0
link = ""

@app.route("/btn_find")
def get_ses():
    global check_if_one

    global what_now
    global number_of_repeats 
    global sleeping_time 
    global link
    if check_if_one == 1:
        return "Success"
    counter = 1
    #http%3A%2F%2Ffbkraken.com%2FZXQSXq&number=17&sleeping=6.0&start=Start
    print("THIS IS WHICH STEP IS NOW : " + str(what_now))
    what_now += 1
    if number_of_repeats == 0:
        number_of_repeats = int(request.args.get('number'))
    if sleeping_time == 0 :
        sleeping_time = float(request.args.get('sleeping'))
    if link == "":
        s = request.args.get('text')
        link = s
    print(link)
    #response = urllib.request.urlopen(request.form['text'])    
    while number_of_repeats > 0:
        if (sleeping_time*(counter) >= 24):
            break
        counter +=1
        number_of_repeats -= 1  
        send_request(link)
        print('#'*40)
        print(number_of_repeats)
        print('#'*40)        
        time.sleep(sleeping_time)
    
    html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Clicker chooser Online</title>
     <script src="//code.jquery.com/jquery-1.11.3.min.js"></script>
    <script src="//code.jquery.com/jquery-migrate-1.2.1.min.js"></script>
</head>
<body>
<h2 align="center">Welcome to the Clicker.online!{number_repeats}</h2>

  <script>
   jQuery(document).ready(function() {
            $.ajax({                                
                url: '/btn_find'
            });
    });
    location.reload();
  </script>

</body>
</html>
'''
    if number_of_repeats <= 0:
        check_if_one = 1
        return "Success"
    print("NUMBER OF REPEATS : " + str(number_of_repeats))
    html = html.replace("{number_repeats}", str(number_of_repeats))
    html = html.replace("{link}", str(link))
    html = html.replace("{sleeping}", str(sleeping_time))
    #t = Timer(5.0, app.run)
    #t.start()
    return html

 

def send_request(s):
    try:            
        r = requests.get(s)
        r.raise_for_status()
        print('#'*40)
        print("YES")
        print('#'*40)     
        if r.status_code == 200:        
            return 1           
    except requests.exceptions.HTTPError as err:        
        send_request(s)

 
    

@app.route('/')
def source():
    global check_if_one
    global what_now
    global number_of_repeats 
    global sleeping_time 
    global link
    check_if_one = 0
    what_now = 0
    number_of_repeats = 0
    sleeping_time = 0
    link = ""
    print("WHY ___")
    html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Clicker chooser Online</title>
 
</head>
<body>
<h2 align="center">Welcome to the Clicker.online0001!</h2>
<form action="/btn_find">
    <h3>Link</h3>
    <p align="center">
        <input name="text" type="text" value="">
    </p>
    <h3>Number of repeats</h3>
     <p align="center">
        <input name="number" type="text" value="">
    </p>
    <h3>Sleeping time</h3>
     <p align="center">
        <input name="sleeping" type="text" value="">
    </p>
    <p align="center">
        <input name="start" id="BTN" type="submit" value="Start" >
    </p>
</form>
<script>
 

</body>
</html>
'''
    
    return html
