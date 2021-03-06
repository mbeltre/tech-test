Feature: Product API

	Scenario: Get product with id 1
		 Given product with id "1" exist
	     When get product with id "1"
	     Then response status code should be "200"
	      And response should contain key "id" with value "1"
	      And response should contain key "name" with value "Nike Shoes"
	      And response should contain key "description" with value "The Nike LunarEpic Low Flyknit Running Shoe is lightweight and breathable with targeted cushioning for a soft, effortless sensation underfoot."
	      And response should contain key "price" with value "23.89"

	Scenario: Get product with id that does not exist
	    Given product with id "2" does not exist
	     When get product with id "2"
	     Then response status code should be "404"

	Scenario: Create new product
		Given the following create product payload
	   			"""
	   				{"name": "testing product", "description": "new product", "price": 100}
	   			"""
	     When create product
	     Then response status code should be "200"
	     Then response should contain key "id" 
	      And response should contain key "name" with value "testing product"
	      And response should contain key "description" with value "new product"
	      And response should contain key "price" with value "100"

	Scenario: Create new product with negative price
		Given the following create product payload
	   			"""
	   				{"name": "testing product", "description": "new product", "price": -1}
	   			"""
	     When create product
	     Then response status code should be "400"
	     
	Scenario: Update product data with valid values
		Given product with id "1" exist
	   	  And the following update product payload
	   	 		"""
	   				{"name": "testing product updated", "description": "new description", "price":100}
	   			"""
	     When update product with id "1"
	     Then response status code should be "200"
	      And response should contain key "id" with value "1"
	      And response should contain key "name" with value "testing product updated"
	      And response should contain key "description" with value "new description"
	      And response should contain key "price" with value "100"

	Scenario: Update product id
	   Given product with id "1" exist
	   	 And the following update product payload
	   	 		"""
	   				{"id": 100}
	   			"""
	    When update product with id "1"
	    Then response status code should be "404"

	Scenario: Update product with id that does not exist
		Given product with id "2" does not exist
	   	  And the following update product payload
	   	 		"""
	   				{name": "testing product updated"}
	   			"""
	     When update product with id "2"
	     Then response status code should be "404"

	Scenario: Update product price to negative value
	   Given product with id "1" exist
	   	 And the following update product payload
	   	 		"""
	   				{"price": -1}
	   			"""
	    When update product with id "1"
	    Then response status code should be "400"

	Scenario: Delete product
		Given product with id "1" exist
	   	 When delete product with id "1"
	     Then response status code should be "404"
	















