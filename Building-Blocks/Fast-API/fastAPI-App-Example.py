from fastapi import FastAPI



app = FastAPI()



@app.get("/")

def root():

  return {"message": "Hello World"}


# to start the server use the following command: uvicorn main:app --reload



# Points to remember#

    #If you create your app like this:

    #my_awesome_api = FastAPI()

    #And put it in a file main.py, then you would call uvicorn like this:

    #uvicorn main:my_awesome_api --reload

    #You can also use the other operations instead of GET:
        #@app.post() can be used if you want the client application to access the route in a POST manner.
        #@app.put() can be used if you want the client application to access the route in a PUT manner.
        #@app.delete() can be used if you want the client application to access the route in a DELETE manner.

        #There are four more operation types which could also be used. They are @app.options(), @app.head(), @app.patch(), and @app.trace().

