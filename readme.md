A - Danielle Zenking
B - Yuval Dar

**Notes**  
Port used by Flask: 5000  
Current interface used by Flask: Localhost (127.0.0.1)  
Templates directory (for index.html): Current directory (".")  
Chats location: Temporary dictionar
extra line to test that git is connected


to install use:
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python backend.py


to use Dockerfile:
$ docker build -t dan_dar -f Dockerfile-slim .
    or use:
    $ docker build -t dan_dar -f Dockerfile-multi .

$ docker run -it --rm -p 5000:5000 dan_dar