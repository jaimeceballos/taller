from twilio.rest import TwilioRestClient


def enviarsms(phone_number,vehiculo,precio):
	account_sid = 'AC762861eadfd9c52d5e9d66c04e5eda38'
	auth_token = '2376c15004fc4343939511b4e798ac08'

	client = TwilioRestClient(account_sid,auth_token)

	message = client.messages.create(body="Electromecanica Ruben le informa que su vehiculo "+ vehiculo +" esta listo para ser retirado.",to=phone_number,from_="+18027274523")

	print message.sid