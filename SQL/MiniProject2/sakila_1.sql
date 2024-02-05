UPDATE customer
SET address_id = (SELECT address_id FROM address WHERE address = '123 New Address, New City')
WHERE customer_id = 5;