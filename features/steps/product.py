from behave import *
import json

@given('product with id "{product_id}" exist')
def product_with_id_exist(context, product_id):
	"""
	make sure data for the test is correct
	"""
	pass

@given('product with id "{product_id}" does not exist')
def product_with_id_does_not_exist(context, product_id):
	"""
	make sure data for the test is correct
	"""
	pass

@given('the following create product payload')
def save_create_product_payload(context):
	context.product_data = json.loads(context.text)

@when('create product')
def create_product(context):
	print(context.product_data)
	context.response = context.api_client.create_product(context.product_data)

@when('get product with id "{product_id}"')
def get_product_with_id(context, product_id):
	context.response = context.api_client.get_product(product_id)

@then('response should contain key "{key}" with value "{value}"')
def response_should_contain_key_value(context, key, value):
	response = json.loads(context.response[1])
	assert key in response.keys()
	assert str(response[key]) == str(value)

@then('response should contain key "{key}"')
def response_should_contain_key_value(context, key):
	response = json.loads(context.response[1])
	assert key in response.keys()

@then('response status code should be "{status_code}"')
def response_status_code_should_be(context, status_code):
	assert str(status_code) == str(context.response[0])





