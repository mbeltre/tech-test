import requests

class Client(object):

	def __init__(self, url):
		self.url = url

	def get_product(self, product_id):
		path =  self.url + "/" + str(product_id)
		r = requests.get(path)
		return (r.status_code, r.text)

	def create_product(self, data):
		r = requests.post(self.url, data=data)
		return (r.status_code, r.text)

	def update_product(self, product_id, data):
		path =  self.url + "/" + str(product_id)
		r = requests.patch(path, data=data)
		return (r.status_code, r.text)