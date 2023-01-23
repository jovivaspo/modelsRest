from flask_restx import Api
from src.routes.analyse import api as nanalyse
from src.routes.auth import api as nauth
from flask import Blueprint

blueprint = Blueprint("api", __name__, url_prefix="/api/v1")

authorizations = {
    "Bearer":{
        "type":"apiKey",
        "in":"headers",
        "name":"authorization",
        "description": "Example: bearer {token}"
    }
}

api = Api(
    blueprint,
    title="REST API Sentiment Analysis",
    version="1.0",
    description="REST Api to Sentiment Analysis. Analyses the sentiment (positive, neutral or negative) of a given text by giving a score between 0 and 1. ",
    authorizations=authorizations,
    security="Bearer"
)

api.add_namespace(nanalyse)
api.add_namespace(nauth)



