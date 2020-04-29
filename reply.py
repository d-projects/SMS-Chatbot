import os
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

s = requests.Session()

@app.route("/sms", methods = ['POST'])
def reply():
	message_received = request.form.get('Body')
	reply = MessagingResponse()
	response = s.post('http://elbot-e.artificial-solutions.com/cgi-bin/elbot.cgi', {'ENTRY':message_received})
	soup = BeautifulSoup(response.content, 'html.parser')
	input_table_row = soup.findAll('tr')[2]
	input_html = input_table_row.findChildren("td")[1].getText()
	reply.message(input_html)
	return str(reply)


if __name__ == "__main__":
	app.run(debug=True)





