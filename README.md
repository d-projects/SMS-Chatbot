# SMS-Chatbot

reply.py is an program that when run allows a user to text a certain number and have a conversation with an AI Chatbot.

A Twilio account is required to allow for the SMS communication. Once created, a number has to be chosen.
Since the program is not set up on a server, I used ngrok to webhook the program to allow internet connection to the Twilio API.
Finally, the ngrok webhook URL has to be copied and pasted in the webhook entry under the chosen phone number, with a "/sms" added to the end of the URL.



