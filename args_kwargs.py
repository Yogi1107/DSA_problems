def create_profile(name, age, *hobbies, **details):
    return f'''
    Name: {name},
    Age: {age},
    Hobbies: {[i for i in hobbies]}
    Details: {details}
'''

result = create_profile('D',25)
result_2 = create_profile('Diana',28,city='London',occupation='Teacher',hobbies_count = 0)
print(result)
print(result_2)
