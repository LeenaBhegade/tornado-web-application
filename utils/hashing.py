import hashlib, binascii
import os

def get_salted_hash(word):
	salt = os.environ['SALT']
	salt_bytes = bytes(salt, 'utf-8')
	word_bytes = bytes(word, 'utf-8')
	dk = hashlib.pbkdf2_hmac('sha256', word_bytes, salt_bytes, 100000)
	salted_bytes = binascii.hexlify(dk)
	return salted_bytes.decode('utf-8')