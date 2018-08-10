import re

class Rider(object): 

    def __init__ (self, first_name, last_name, email_address, phone_number, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.phone_number = phone_number
        self.password = password

    # def __str__(self):
    #     return self.first_name + ', ' + self.last_name + ', ' + self.email_address  + ', ' + self.phone_number + ', ' + self.password

    def full_name(self):
        fullname = self.first_name + ', ' +  self.last_name
        if re.match('^([A-Za-z-_]+)$)', fullname, re.I):
            return fullname
        else:
            return 'Name should have only letters'

    def validate_email(self):
        if re.match('^[A-Za-z0-9-_]+(.[A-Za-z0-9-_]+)*@[A-Za-z0-9-_]+(.[A-Za-z-_]+)*(.[A-Za-z]{2,})$', self.email_address, re.I):
            return self.email_address

        else:
            return 'Invalid email address'


    def validate_phone_number(self):
        if re.match('^\+?[\d]{3}[ ]?[\d]{3}-[\d]{6}|\+?[\d]{3}[ ]?[\d]{3}[ ]?[\d]{6}$', self.phone_number, re.I):
            return self.phone_number

        else:
            print('Incorrect number format')

    def validate_password(self):
        # if re.match('^(?=.*[!@#$%&?^])(?=.*[a-z])(?=.*[A-Z].{8,}$', self.password):
        #     return self.password

        # else:
        #     return 'Invalid password'
        x = True
        while x:
            pwd = input('Enter Password:')
            if (len(pwd)<8 0r len(pwd)>15):
                return 'Invalid Password'

            elif not re.search('[a-z]', pwd):
                return 'Invalid Password'

            elif not re.search('[A-Z]', pwd):    
                return 'Invalid Password'

            elif not re.search('[0-9]', pwd):
                return 'Invalid Password'

            elif not re.search('[!@#$%^&*_?', pwd):
                return 'Invalid Password'

            elif re.search('\s', pwd):
                return 'Invalid Password'

            else:
                return 'Congrats,Valid password set'
                x = False
                break

