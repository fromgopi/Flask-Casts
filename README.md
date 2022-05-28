# Flask-Casts
My experiments with Flask and Python

# To run the app in local env.
cd web
pip install -r requirements.txt
python3 app.py
 
# To run in Develop server

cd web
docker build -t project -f Dockerfile .
cd ../
docker-compose up -d

# To check if app is running
docker ps.
