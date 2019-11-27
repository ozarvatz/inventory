# inventory
Run this application on docker  
  docker run -it -p 8888:8888 -v 'C:/work/cympire/python/:/root/python' floydhub/dl-docker:cpu bash  <br>
  in adision i install flaks and set <br>
  $ export FLASK_ENV=development <br>
  $ export FLASK_APP=app.py <br>
  for more info visit https://medium.com/@onejohi/building-a-simple-rest-api-with-python-and-flask-b404371dc699  <br>
  <br>  
  $>flask run --host=0.0.0.0 --port=8888  <br>
  <br>
  then you can perform calls like: <br>
  get category list by store id <br>
  http://localhost:8888/category/store/30  <br>
  http://localhost:8888/category/store/1   <br>
  <br>
  getting items median price per category id <br>
  http://localhost:8888/category/median/33 <br>
  http://localhost:8888/category/median/1 <br>
  <br>
  get item total inventory by item name: <br>
  http://localhost:8888/item/bisli <br>
  <br>
  <br>
  for web test , install request <br>
  pip install requests <br>
  for more info visit https://www.geeksforgeeks.org/get-post-requests-using-python/ <br>
  <br>
  for running web test: <br>
  from comand line <br>
  cd python <br>
  python ./testWeb.py <br>
  
  for regular testing: <br>
  cd python <br>
  python ./testInventory.py <br>
  
