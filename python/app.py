import Inventory
import AppConfig
import sys

from flask import Flask, json, make_response

app = Flask(__name__)
  
@app.route('/ping')
def say_pong():
  return 'pong'

# get inventory bt item name
@app.route('/item/<itemName>')
def get_item_inventory(itemName):
	inventory = Inventory.Inventory(AppConfig.AppConfig.INVENTORY_FILE_PATH)
	msg = "all {item_name} inventory ".format(item_name=itemName)
	retval = inventory.get_item_inventory(itemName)

	return make_response({'message': msg, 'response': json.dumps(retval)}, 200)

# get categories list per store id 
@app.route('/category/store/<int:storeId>')
def get_categories_for_store(storeId):
	inventory = Inventory.Inventory(AppConfig.AppConfig.INVENTORY_FILE_PATH)
	msg = "all categories for store {store_id}".format(store_id=storeId)
	retval = inventory.get_categories_for_store(storeId)
	return make_response({'message': msg, 'response': json.dumps(retval)}, 200)

# get price median per category id 
@app.route('/category/median/<int:categoryId>')
def get_median_for_category(categoryId):
	retval = None
	msg = None
	status = 200
	try:
		inventory = Inventory.Inventory(AppConfig.AppConfig.INVENTORY_FILE_PATH)
		msg = "Median for category {category_id}".format(category_id=categoryId)
		retval = inventory.get_efficient_median_for_category(categoryId)	
	except:
		msg = "Unexpected error: internal server error" 
		retval = str(sys.exc_info()[1])
		status = 500 # internal server error
		pass

	return make_response({'message': msg, 'response': json.dumps(retval)}, status)

