# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 14:33:57 2020

@author: jedaix
"""

class info:
    def __init__(self,name,phone,email):
        pass
    def set_name(self,name):
       self.name=name
    def set_phone(self,phone):
       self.phone=phone
    def set_email(self,email):
        self.email=email
    def get_name(self,name):
        return self.name
    def get_phone(self,phone):
        return self.phone
    def get_email(self,email):
        return self.email
    def __str__(self):
        return self.name+" "+self.email+" "+self.phone

c=info('name','phone','email')
c.set_name('bhavesh')
c.set_phone('9039908997')
c.set_email('bhavesh16somnani@gmail.com')
print(c.__str__())
    