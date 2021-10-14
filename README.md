# OSA
```diff
! Oversea Shipping API
```

## Deployed at: https://osa-api.herokuapp.com/

## Guide to run the project locally: 
- install virtualenv: python -m venv venv
- active virtualenv: source venv/bin/activate
- (venv) pip install -r requirements.txt
- python manage.py makemigrations
- python manage.py migrate 
- python manage.py runserver 


## API REDIRECT: 
+ ORDER:
- detail: http://127.0.0.1:8000/api/order/<:id>/
- create: http://127.0.0.1:8000/api/order/create/
- update: http://127.0.0.1:8000/api/order/<:id>/edit/
- delete: http://127.0.0.1:8000/api/order/<:id>/delete/

+ PRODUCT:
- list:   http://127.0.0.1:8000/api/product/
- detail: http://127.0.0.1:8000/api/product/<:id>/
- create: http://127.0.0.1:8000/api/product/create/
- update: http://127.0.0.1:8000/api/product/<:id>/edit/
- delete: http://127.0.0.1:8000/api/product/<:id>/delete/

+ PACK:
- list:   http://127.0.0.1:8000/api/pack/
- detail: http://127.0.0.1:8000/api/pack/<:id>/
- create: http://127.0.0.1:8000/api/pack/create/
- update: http://127.0.0.1:8000/api/pack/<:id>/edit/
- delete: http://127.0.0.1:8000/api/pack/<:id>/delete/

## BACKEND SYSTEM REDIRECT: 
+ order management： http://127.0.0.1:8000/
+ product management： http://127.0.0.1:8000/product/
+ pack management： http://127.0.0.1:8000/pack/


## IAP for ios: ...
## React native frontend: ...
