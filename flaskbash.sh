sudo service postgresql start
export FLASK_DEBUG=1
export FLASK_APP=/home/ubuntu/workspace/networkmanager/venv/src/app.py
flask run --host=0.0.0.0 --port=8080

