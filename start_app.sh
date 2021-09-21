#!/bin/bash


echo "Mode: $1";

mode=$1

echo $mode


case $mode in 

    1)
        echo "This is mode 1, running app with python app.py"
        python app/app.py
        ;;
    2)
        echo "this is mode 2, running app with gunicorn 3 sync worker"
        gunicorn app.app:app -w 3 -b 0.0.0.0:8000
        ;;

    3)
        echo "this is mode 3, running app with gunicorn 3 async worker"
        gunicorn app.not_patched:app --worker-class gevent -w 3 -b 0.0.0.0:8000
        ;;

    4)
        echo "this is mode 4, running app with gunicorn 3 async worker, patched"
        gunicorn app.patched:app --worker-class gevent -w 3 -b 0.0.0.0:8000
        ;;

esac
