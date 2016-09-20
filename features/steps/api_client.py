import requests

class Client(object):

	def __init__(self, url):
		self.url = url

	def get_product(self, product_id):
		path =  self.url + "/" + str(product_id)
		r = requests.get(path)
		return (r.status_code, r.text)

	def create_product(self, json):
		print("json")
		print(json)
		r = requests.post(self.url, data=json)
		return (r.status_code, r.text)

	def update_product(self, product_id, product_json):
		path =  self.url + "/" + str(product_id)
		r = requests.patch(path, data=product_json)
		return (r.status_code, r.text)