from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

app = Flask(__name__)

def create_driver():
	global browser
	CHROME_DRIVER_PATH = 'C:/Users/dulha/AppData/Local/chromedriver.exe'
	capabilities = { 'chromeOptions':  { 'useAutomationExtension': False}}

	options = Options()
	options.headless = True
	browser = webdriver.Chrome(executable_path = CHROME_DRIVER_PATH, desired_capabilities=capabilities, options = options)
	browser.get("http://elbot-e.artificial-solutions.com/cgi-bin/elbot.cgi")

def get_response():
	global browser
	response_html = browser.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td[2]")
	response_text = response_html.get_attribute('innerHTML')
	response = response_text.replace(" <!-- Begin Response !--> ", "").replace(" <!-- End Response !-->", "")
	return response

@app.route("/sms", methods = ['POST'])
def reply():
	global session
	global browser
	input_text = request.form.get('Body')

	if (input_text.lower() == 'open'):
		create_driver()
		session = True
		response = get_response()

	elif (not session):
		response = "Type 'open' to start chatting and type 'close' once you are done."


	elif (input_text.lower() == 'close'):
		browser.quit()
		session = False
		response = "Chat Session Closed"

	else:
		input_box = browser.find_element_by_name("ENTRY")
		input_box.send_keys(input_text)
		input_box.send_keys(Keys.RETURN)
		response = get_response()

	reply = MessagingResponse()
	reply.message(response)
	return str(reply)
		


if __name__ == "__main__":
	session = False
	app.run(debug=True)









