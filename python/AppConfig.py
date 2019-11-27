from os import environ

class AppConfig(object):
	# selecting the appropriate inventory file,
	# according to the environment variable FLASK_ENV.
	INVENTORY_FILE_PATH = './inventory.txt' if environ.get('FLASK_ENV') == 'test' else './inventory.txt'