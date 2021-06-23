# Flask API
This is a basic demo of how to create API using FLASK

## Steps to follow:
* create a virtual env(optional) and activate the same

* in cmd run : pip install -r requirements.txt (make sure you are in same location where your requirements.txt file is present)
* run python run.py file

### Some example of requests using python to your local server:

* GET request
```python
import requests
url='http://127.0.0.1:5000/books'
r = requests.get(url)
print(r.text)
```

* POST request (add a new record)
```python
import requests
payload = {'name':'Lord of Rings 4','desc':'This is related to ring and magic witchery saga of log of rings'}
url='http://127.0.0.1:5000/books'
r = requests.post(url, json=payload)
print(r.text)
```

* POST request (update a record)
```python
import requests
payload = {'id':4,'name':'Lord of Rings 4','desc':'This is related to ring and magic witchery saga of log of rings'}
url='http://127.0.0.1:5000/books/update'
r = requests.post(url, json=payload)
print(r.text)
```
