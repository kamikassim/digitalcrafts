ramit = {
    'name': 'Ramit',
    'email': 'ramit@gmail.com',
    'interests': ['movies', 'tennis'],
    'friends': [
        {
            'name': 'Jasmine',
            'email': 'jasmine@yahoo.com',
            'interests': ['photography', 'tennis']
        }, {
            'name': 'Jan',
            'email': 'jan@hotmail.com',
            'interests': ['movies', 'tv']
        }
    ]
}

#step 1 Get Ramit's Email 
print ramit['email']

#step2 get first of ramit's interests
print ramit['interests'][0]

#step3 get Jasmine's email address
print ramit['friends'][0]['email']

#step4 get second of Jan's two interests
print ramit['friends'][1]['interests'][1]