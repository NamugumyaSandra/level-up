import re

class Rider(object): 

    def __init__ (self, first_name, last_name, email_address, phone_number, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.phone_number = phone_number
        self.password = password


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
        x = True
        while x:
            if (len(self.password)>8):
                return 'Should be more than 8 characters'

            elif not re.search('[a-z-_]', self.password):
                return 'Invalid Password'

            elif not re.search('[A-Z-_]', self.password):    
                return 'Invalid Password'

            elif not re.search('[0-9-_]', self.password):
                return 'Invalid Password'

            elif not re.search('[!@#$%^&*_?]?', self.password):
                return 'Invalid Password'

            elif re.search('\s', self.password):
                return 'Invalid Password'

            else:
                return 'Congrats,Valid password'
                x = False
                break

