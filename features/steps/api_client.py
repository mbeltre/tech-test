import requests
import json

class Client(object):

	def __init__(self, url):
		self.url = url

	def get_product(self, product_id):
		path =  self.url + "/" + str(product_id)
		r = requests.get(path)
		return (r.status_code, r.text)

	def create_product(self, data):
		headers={"Content-Type":"application/x-www-form-urlencoded"}
		r = requests.post(self.url, data={"json_data":data}, headers=headers)
		return (r.status_code, r.text)

	def update_product(self, product_id, data):
		path =  self.url + "/" + str(product_id)
		headers={"Content-Type":"application/x-www-form-urlencoded"}
		r = requests.patch(path, data={"json_data":data}, headers=headers)
		return (r.status_code, r.text)

	def delete_product(self, product_id):
		path =  self.url + "/" + str(product_id)
		r = requests.delete(path)
		return (r.status_code, r.text)