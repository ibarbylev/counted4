# counted4
### The play for learning websockets in practice


ATTENTION!!!

First of all, you need to add the real ip address to app.py (row #171) and to main.js (row #79).
The default port for both cases is 8001.


HOW TO RUN SERVER AUTOMATICALLY AFTER EVERY CHANGE OF THE CODE:

```commandline
watchmedo auto-restart --pattern "*.py" --recursive --signal SIGTERM python app.py
```

More info: https://websockets.readthedocs.io/en/stable/howto/autoreload.html