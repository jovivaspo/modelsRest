from flask_restx import Api
from flask import Blueprint
from src.routes.auth import api as nauth

route_auth = Blueprint('auth',__name__, url_prefix='/api')

authorizations = {
    "Bearer":{
        "type":"apiKey",
        "in":"headers",
        "name":"authorization",
        "description": "Example: bearer {token}"
    }
}

api = Api(
    route_auth,
    title="Rest Api Sentiment Analysis",
    version="1.0",
    description="REST Api to Sentiment Analysis: positive, neutral or negative rating.",
    prefix="/api/v1",
    doc="/api/v1/doc",
    authorizations=authorizations,
    security="Bearer"
)

api.add_namespace(nauth)



