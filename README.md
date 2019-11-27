# inventory
Run this application on docker  
  docker run -it -p 8888:8888 -v 'C:/work/cympire/python/:/root/python' floydhub/dl-docker:cpu bash
  in adision i install flaks and set 
  $ export FLASK_ENV=development
  $ export FLASK_APP=app.py 
  for more info visit https://medium.com/@onejohi/building-a-simple-rest-api-with-python-and-flask-b404371dc699
  
  $>flask run --host=0.0.0.0 --port=8888
  
  then you can perform calls like:
  get category list by store id
  http://localhost:8888/category/store/30
  http://localhost:8888/category/store/1
  
  getting items median price per category id
  http://localhost:8888/category/median/33
  http://localhost:8888/category/median/1
  
  get item total inventory by item name:
  http://localhost:8888/item/bisli
  
  
  for web test , install request 
  pip install requests 
  for more info visit https://www.geeksforgeeks.org/get-post-requests-using-python/
  
  for running web test:
  from comand line 
  cd python
  python testWeb.py
  
  for regular testing:
  cd python 
  python testInventory.py
  
