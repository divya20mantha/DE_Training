customer_tbl = {
    "cust_id": [1,2,3,4],
    "cust_name": ["John", "Jane", "Doe", "Smith"],
    "cust_email": ["abc@abc.com","abc@abc.com"]

}

# print ('whole tbls ',customer_tbl)
# print ('cust id are ',customer_tbl["cust_id"])

print ('get method', customer_tbl.get('cust_name')[0])
