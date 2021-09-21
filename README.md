# this is to test the effect of 

* main app configs:
    * type 1: simply python app/app.py
    * type 2: gunicorn with sync worker
    * type 3: gunicorn with async worker (gevent not patched)
    * type 4: gunicorn with async worker (gevent patched)
* main app endpoints to test:
    * slow (main app makes a request to resource app, resource app has a time.sleep(1) before response)
    * fast (main app makes a request to resource app, resource app responses instantly)
    * stuck (main app will run something cpu-heavy before response)
* then there will be 12 results
