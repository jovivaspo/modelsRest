from flask import Flask
from routes.auth import routes_auth
from routes.analyse import route_analyse
from dotenv import load_dotenv
from waitress import serve


app = Flask(__name__)

# Using a production configuration
app.config.from_object('config.ProdConfig')

# Using a development configuration
#app.config.from_object('config.DevConfig')


#Routes:
app.register_blueprint(routes_auth, url_prefix='/api')
app.register_blueprint(route_analyse, url_prefix='/api')


if __name__ == "__main__":
    load_dotenv()
    #app.run(debug=True, c)
    print("Server running")
    serve(app, host='0.0.0.0', port=5000) 


