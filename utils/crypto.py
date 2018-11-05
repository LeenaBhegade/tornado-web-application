import base64
import os.path

from Crypto import Random
from Crypto.PublicKey import RSA

def get_keys(key_type):
	# Check if private key and public key exists
	file_exists = os.path.isfile('public_key.pem') and os.path.isfile('private_key.pem')

	if file_exists:
		if (key_type == "private_key"):
			private_key_file = open('private_key.pem', 'rb')
			private_key = RSA.importKey(private_key_file.read())

		if (key_type == "public_key"):
			public_key_file = open('public_key.pem', 'rb')
			public_key = RSA.importKey(public_key_file.read())
	else:
		private_key = RSA.generate(1024, Random.new().read)
		public_key = private_key.publickey()
		
		file = open('public_key.pem', 'wb')
		file.write(public_key.exportKey('PEM'))
		file.close()

		file = open('private_key.pem', 'wb')
		file.write(private_key.exportKey('PEM'))
		file.close()

	if key_type == "private_key":
		return private_key
	else:
		return public_key

def encrypt_data(word, publickey):
	word_bytes = bytes(word, 'utf-8')
	encrypted_data = publickey.encrypt(word_bytes, 32)[0]
	encoded_encrypted_data = base64.b64encode(encrypted_data)
	return encoded_encrypted_data

def decrypt_data(encoded_encrypted_data, privatekey):
	decoded_encrypted_data = base64.b64decode(encoded_encrypted_data)
	word = privatekey.decrypt(decoded_encrypted_data)
	return word.decode('utf-8')
