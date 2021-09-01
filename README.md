# Load Testing with Locust

For installation follow https://docs.locust.io/en/stable/installation.html

- If Operating System is MacOs install before
```sh
$ brew install libev
``` 

## Running
### Running without the web UI
> No graphics results.

Go to folder where is your tests and execute: 
```sh
$ locust -f locustfile.py --host=https://reqres.in/api --headless -u 2 -r 1
``` 

### Running with the web UI
> Graphics results.
 1. Go to folder where is your tests and execute: 
```sh
$ locust -f locustfile.py --host=https://reqres.in/api
``` 
 2. Then open your browser and type:
```sh
http://localhost:${PORT}
``` 
 > **NOTE:** ${PORT} is shown at terminal after executes step 1
