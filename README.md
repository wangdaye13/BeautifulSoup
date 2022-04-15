## Clone the Repo

Clone the repo by whater means you like. After cloning `cd` into the downloaded BeautifulSoup directery.

```
git clone https://github.com/crispycret/BeautifulSoup.git
# or
git clone git@github.com:crispycret/BeautifulSoup.git

cd BeautifulSoup
```

## Setup

### Start by creating a virtual environment.

```
python3 -m venv venv
```

### Activate the virtual environment

#### WSL / WSL2 / Linux
```
source venv/bin/activate
```

#### Windows

To get activate the virtualenv on windows 10 you must do the following
* Run `powershell` as `admin`
* Run the command `set-executionpolicy remotesigned` and answer `Y` to the response to allow untrusted scripts to be run. This is required for activating the virtualenv.
* Lastly navigate inside the `BeaitufulSoup` folder and run `.\venv\bin\Activate.ps1`


##### Allow unsigned scripts to be executed
```
set-executionpolicy remotesigned
```
##### Output
```
Execution Policy Change
The execution policy helps protect you from scripts that you do not trust. Changing the execution policy might expose
you to the security risks described in the about_Execution_Policies help topic at
https:/go.microsoft.com/fwlink/?LinkID=135170. Do you want to change the execution policy?
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "N"): Y
```

#### Navigate to the BeautifulSoup folder and activate the virtual environment
'''
cd /your/path/to/BeautifulSoup

.\venv\bin\Activate.ps1
```



#### WSL / WSL2 / Linux / Windows virtualenv conclusion

After activating the virtual environment you should see that your terminal prompt is prefixed by `(venv)`


### Install the required moudles.

Install the modules required for this project.

```
pip install -r requirements.txt
``` 


This includes an extra module: `python-dotenv==0.20.0` which will read a `.env` and set environment variables found in there. The provided `.env` file includes `FLASK_APP=task6.py` so that the only thing left to do is to run flask. If for some reason running flask provides you with the following error then you will need to set the `FLASK_APP` variable manually.

```
Error: Could not locate a Flask application. You did not provide the "FLASK_APP" environment variable, and a "wsgi.py" or "app.py" module was not found in the current directory.
```

### Manually Set Environment Variables If Needed
```
# If on windows use 
set FLASK_APP=task6.py

#If on linux/WSL use 
export FLASK_APP=task6.py
```

## Running

To start the flask application run:

```
flask run
```

Once the application is running you can go to `http://127.0.0.1:5000/` in a browser to view the application.






