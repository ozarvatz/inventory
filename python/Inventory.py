import json
import os
from numpy import median
import numpy as np

class Inventory(object):
    """
    Inventory Management system 
    """
    def __init__(self, pathToInventoryJsonFile): 
        self.inventoryData = None
        with open(pathToInventoryJsonFile) as json_file:
            self.inventoryData = ([doc for doc in json.load(json_file)])

        if self.inventoryData == None:
            raise Exception('pathToInventoryJsonFile is empty')
        print(self.inventoryData)
        pass    
    def get_categories_for_store(self, store):
        """
        Given a store id you should return all the categories ids in the inventory.
        :param store: store id
        :return: all the categories ids in the inventory
        """
        return [doc['category'] for doc in self.inventoryData if doc['store'] == store]
    def get_item_inventory(self, item):
        """
        Given items name return all the items across all stores.
        :param item: item name
        :return: all the items across all stores
        """
        return sum([doc['items'] for doc in self.inventoryData if doc['item_name'] == item])
    def get_median_for_category(self, category):
        """
        Given category id return the median of the prices for all items in the category.
        :param category: category name
        :return: the median of the prices for all items in the category
        """
        # i choose the numpy median,  
        # cos I want a average of the two middle elements
        # in case of even array length.
        # it is a very inefficient way to find the median,
        # I wanted to show that I learn a little bit python ;) 
        prices = [np.full(doc['items'], doc['price']) for doc in self.inventoryData if doc['category'] == category ]
        
        if prices:
            prices = np.concatenate(prices)
        else: 
            # prices is empty cos category not exists
            raise Exception("no median, empty prices list cos category {id} not exists!!!".format(id=category))
        # print('test------------')
        return median(prices)

    #calculate median more efficiently 
    def get_efficient_median_for_category(self, category):
        categoryData = [doc for doc in self.inventoryData if doc['category'] == category]
        categoryData.sort(key=lambda i:i['price'])
        print(categoryData)
        totalItems = sum([doc['items'] for doc in categoryData])
        if totalItems == 0:
            raise Exception("no median, empty prices list cos category {id} not exists!!!".format(id=category))
        
        medianItemIndex = int(totalItems / 2)
        medianPrice = -1
        i = 0
        itemCounter = 0

        while True:
            data = categoryData[i]
            i = i + 1
            itemCounter += data['items']
            print(itemCounter) 
            print(data)
            if itemCounter >= medianItemIndex:
                medianPrice = data['price']
                print(medianPrice) 
                break    
        if medianPrice == -1:
            raise Exception("could not find a median for category ({category_id})".format(category_id = category))

        return medianPrice