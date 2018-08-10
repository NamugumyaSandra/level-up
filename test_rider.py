
import unittest
from rider import Rider

class TestRider(unittest.TestCase):

    def test_rider_creation(self):
        rider = Rider('Sandra', 'Namugumya', 'salyn123@gfhj.dfg', '+256 790 456789', 'W3!c0me@')
    
    # def test_full_name(self):
    #     rider = Rider('Sandra', 'Namugumya', 'salyn123@gfhj.dfg', '+256 790 456789', 'W3!c0me@')
    #     self.assertNotRegex(rider.full_name(), ('[A-Za-z-_]+'), 'Sandra Namugumya')
        
    # def test_not_correct_name_format(self):
    #     rider = Rider('Sandra', 'Namug789a', 'salyn123@gfhj.dfg', '+256 790 456789', 'W3!c0me@')
    #     self.assertRegex(rider.full_name(), ('[A-Za-z-_]+'), 'Name should have only letters')

    def test_validate_email(self):
        rider = Rider('Sandra', 'Namugumya', 'salyn123@gfhj.dfg', '+256 790 456789', 'W3!c0me@')
        self.assertRegex(rider.validate_email(), ('[A-Za-z0-9-_]+(.[A-Za-z0-9-_]+)*@[A-Za-z0-9-_]+(.[A-Za-z-_]+)*(.[A-Za-z]{2,})'),'salyn123@gfhj.dfg')
    
    def test_not_validate_email(self):
        rider = Rider('Sandra', 'Namugumya', 'salyn123@gfhjdfg.8j.99', '+256 790 456789', 'W3!c0me@')
        self.assertNotRegex(rider.validate_email(), ('[A-Za-z0-9-_]+(.[A-Za-z0-9-_]+)*@[A-Za-z0-9-_]+(.[A-Za-z-_]+)*(.[A-Za-z]{2,})'),'Invalid email address')

    def test_validate_phone_number(self):
        rider = Rider('Sandra', 'Namugumya', 'salyn123@gfhj.dfg', '+256 790 456789', 'W3!c0me@')
        self.assertRegex(rider.validate_phone_number(), ('\+?[\d]{3}[ ]?[\d]{3}-[\d]{6}|\+?[\d]{3}[ ]?[\d]{3}[ ]?[\d]{6}'),'256 790 456789')

    def test_not_validate_phone_number(self):
        rider = Rider('Sandra', 'Namugumya', 'salyn123@gfhj.dfg', '+256-790 46789', 'W3!c0me@')
        self.assertNotEqual(rider.validate_phone_number(), 'Incorrect number format')

    def test_validate_password(self):
        rider = Rider('Sandra', 'Namugumya', 'salyn123@gfhj.dfg', '+256 790 456789', 'W3!c0me@1')
        self.assertRegex(rider.validate_password(), ('([A-Za-z0-9-_]+[!@#$%^&*_?]?){8,}'), 'Congrats,Valid password')

    def test_not_validate_password(self):
        rider = Rider('Sandra', 'Namugumya', 'salyn123@gfhj.dfg', '+256 790 456789', 'W3!e@')
        self.assertNotEqual(rider.validate_password(), 'Invalid password')