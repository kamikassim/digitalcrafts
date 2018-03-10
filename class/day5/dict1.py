phonebook_dict = {
    'Alice': '703-878-9898',
    'Bob': '878-898-9898',
    'Elizabeth': '878-475-4545'
}

#step1 Print Elizabeth's phone number
print phonebook_dict['Elizabeth']


#step2 Add Kareem
phonebook_dict["Kareem"] = '404-989-3535'
print phonebook_dict['Kareem']

#step3 Delete Alice
del phonebook_dict['Alice']

#step4 change Bob's phone number
phonebook_dict['Bob'] = '404-888-7777'
print phonebook_dict

#step5 print everything
print phonebook_dict