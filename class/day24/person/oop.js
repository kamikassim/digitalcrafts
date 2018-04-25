/* 1. Instantiate an instance object of Person with name of 'Sonny', 
email of 'sonny@hotmail.com', and phone of '483-485-4948', store it in the variable sonny. */

function Person (name, email, phone) {
    // this.name = 'Sonny';
    // this.email = 'sonny@hotmail.com'
    // this.phone = '483-485-4948';
    this.name = name;
    this.email = email;
    this.phone = phone;
}

var sonny = new Person('Sonny', 'sonny@hotmail.com', '483-485-4948');
console.log(sonny);

var jordan = new Person('Jordan', 'jordan@aol.com','495-586-3456');
console.log(jordan);

Person.prototype.greet = function(other) {
    console.log('Hello ' + other.name + ', I am ' + this.name + '!');
  };

sonny.greet(jordan);
jordan.greet(sonny);

console.log(sonny.name, sonny.email); 
console.log(jordan.name, jordan.email, jordan.phone);

