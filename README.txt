Notes:
- when you process text, map names to objects for context matching
- build full pipeline first then worry about consistency and timing

Virtual Environment Directions:
First make sure you have python3.6 or above installed on your device.
Then, run python"your-python-version" -m venv "your-venv-name"
For example: python3.9 -m venv fablesvenv
Then, run $source "your-venv-name"/bin/activate
This will activate the virtual Environment
then, run $pip"your-python-version" install -r requirements.txt
This will install all the necessary packages and libraries
Following this, you should be able to run everything with the python command as normal

Also, run "flask run" to start up the flask app!
This will spin up a server on your local address at port 5000:
http://127.0.0.1:5000
