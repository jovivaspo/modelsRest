from flask_restx import Api
from flask import Blueprint
from src.routes.analyse import api as nanalyse

route_analyse = Blueprint('auth',__name__, url_prefix='/api')

authorizations = {
    "Bearer":{
        "type":"apiKey",
        "in":"headers",
        "name":"authorization",
        "description": "Example: bearer {token}"
    }
}

api = Api(
    route_analyse,
    title="Rest Api Sentiment Analysis",
    version="1.0",
    description="REST Api to sentiment Analysis: positive, neutral or negative rating.",
    prefix="/api/v1",
    doc="/api/v1/doc",
    authorizations=authorizations,
    security="Bearer"
)

api.add_namespace(nanalyse)



