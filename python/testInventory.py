import Inventory
import AppConfig

inventory = Inventory.Inventory(AppConfig.AppConfig.INVENTORY_FILE_PATH);

# check get_categories_for_store(1) expect [10,1,2]
categories = inventory.get_categories_for_store(1)
print('\ncategories list for store 1: (should be [10, 1, 2])\n')
print(categories)

# check for get_item_inventory('bisli') 
sumOfItems = inventory.get_item_inventory('bisli')
print('\nget sum of items for bisli : (should be 35)\n')
print(sumOfItems)
# check for get_item_inventory('pc') 
sumOfItems = inventory.get_item_inventory('pc')
print('\nget sum of items for pc : (should be 4)\n')
print(sumOfItems)
# check for get_item_inventory('king') 
sumOfItems = inventory.get_item_inventory('king')
print('\nget sum of items for king : (should be 0)\n')
print(sumOfItems)

# check for get_median_for_category(1) 
medianPerCategory = inventory.get_median_for_category(1)
print('\nget median for category 1 : (should be 3)\n')
print(medianPerCategory)

# check for get_median_for_category(120) 
medianPerCategory = inventory.get_median_for_category(120)
print('\nget median for category 120 : (should be 200)\n')
print(medianPerCategory)

# check for get_median_for_category(120) 
medianPerCategory = inventory.get_median_for_category(10)
print('\nget median for category 10 : (should be 50)\n')
print(medianPerCategory)