# PyAddressBook 

Simple module to present Flask-based DB connecting app

## Installation
Run `pip install -r requirements.txt`

## Run in debug mode
<aside class="warning">
Warning: Running in debug mode is insecure and should never be used in production
</aside>

### Linux  
```bash
export FLASK_APP=web-app.py  
flask run --host 0.0.0.0
```
### Windows
```bash
set FLASK_APP=web-app.py
flask run -- host 0.0.0.0
```