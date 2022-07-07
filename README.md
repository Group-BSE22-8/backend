# Administrative & Auditing Module
This repo contains the backend code for the administrative and auditing module.


## Installation
#### 1. Create a virtual environment
Navigate to the root of the project and run the following command:
```python3 -m venv venv ```

Activate the viitual environment by running the following command:
```  . venv/bin/activate ```

Navigate to the virtual environment and run
``` pip install Flask```


#### 2. Create a Flask application
``` 
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1>'
 ```

#### 3. Run the application
```
export FLASK_APP=hello
export FLASK_ENV=development
flask run
```