import json
import datetime 
import requests
import os


# Change to custom address if not using local node
node = 'http://127.0.0.1'

# Mainnet = :8000
# Testnet = :7000
# Betanet = :5000
network_port = ':8000'

# Password used while creating encrypted passphrase
password = ''

# Publickey of your address
publickey = ''


def main():
	url = node + network_port + '/api/node/status/forging'
	response = requests.get(url)
	json_data = response.json()


	if json_data['data'][0]['forging'] == True:
		message = "Forging was already enabled. No actions taken."
		
	else:
		headers = {
			'Content-Type': 'application/json',
		}

		data = '{"password":"%s", "forging": true, "publicKey":"%s"}' % (password, publickey)

		response = requests.put(url, headers=headers, data=data, verify=False)
		
		message = "Forging was disabled. Toggled status to 'true'."


	with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "lisk-autotoggler.log"), "a") as text_file:
		text_file.write("%s - %s\n" % (datetime.datetime.now(), message))
	
	
if __name__ == "__main__":
	main()
