# the-best-random-team

Group Members: Will Albers, Ajaita Saini, Abhinav Tekulapally, Sameer Vijay, James Wang

PM: Drake Eidukas

## Project Overview:
Our project uses a Raspberry Pi, Arduino, and battery pack to light and power an LED strip. We built a website that displays a number of buttons representing varying lighting patterns and on/off commands, and with each button press, an HTTP request is made. On the Raspberry Pi, we are using Flask to receive these requests and relay them to the Arduino over serial communication. The Arduino then lights up the LED strip based on the designated pattern

## Installation instructions
1) Install python-pip with
`sudo apt-get install python-pip`
2) Install required python libraries through pip
`pip install --user -r requirements.txt`
3) Run the server with `python app.py`
4) Go to [localhost:5000](http://localhost:5000)
