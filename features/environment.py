from steps.api_client import Client

SERVER_URL = "https://python-qa-tech-test.herokuapp.com"
PRODUCT_API_PATH = SERVER_URL + "/product"

def before_all(context):
	context.api_client = Client(PRODUCT_API_PATH)