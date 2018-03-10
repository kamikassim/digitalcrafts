class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def greet(self, other_person):
        print 'Hello %s, I am %s!' % (other_person.name, self.name)

#step1 Sonny/Kami
kamilah = Person('kami', 'kam@gmail.com', '576-878-9898')
print kamilah.name

sonny = Person('sonny', 'sonny@aol.com', '989-999-9999')
print sonny.name

#step2 Jordan
jordan = Person('jordan', 'jordan@aol.com', '495-586-3456')
print jordan.name

#step3 Sonny greet Jordan
sonny.greet(jordan)

#step4 Jordan greet Sonny
jordan.greet(sonny)

#step5 print contact info for both
print jordan.email
print jordan.phone

print sonny.email
print sonny.phone