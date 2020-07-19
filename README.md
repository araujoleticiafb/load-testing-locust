# Load Testing with Locust

For installation follow [https://docs.locust.io/en/stable/installation.html]

- If Operating System is MacOs install **brew install libev** before install locust
## Running 


### Running without the web UI
No graphics results.

1. Go to folder where is your tests and execute: 
 - locust -f locustfile.py --host=https://reqres.in/api --headless -u 2 -r 1

### Running with the web UI
Graphics results.
 1.  Then go to folder where is your tests and execute: 
		- locust -f locustfile.py --host=https://reqres.in/api 
 2. Open browser and type (PORT is shown at terminal after execute step 1):
		 - http://localhost:PORT	