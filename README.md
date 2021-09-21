# this is to test the effect of 

* main app configs:
    * simply python app/app.py
    * gunicorn with sync worker
    * gunicorn with async worker (gevent not patched)
    * gunicorn with async worker (gevent not patched)
* main app endpoints to test:
    * slow (main app makes a request to resource app, resource app has a time.sleep(1) before response)
    * fast (main app makes a request to resource app, resource app responses instantly)
    * stuck (main app will run something cpu-heavy before response)
* then there will be 12 results
