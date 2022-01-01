from atm_app import views as v, models as m  
from atm_app.models import Account as A   

class Application():
    
    def __init__(self):
        self.name = input('Please enter name: ')
        self.amnt = int(input('Enter amount: '))
    
    def get_details(self):
        return[self.name, self.amnt]
        
        
x = Application()
details = x.get_details()
if details:
    v.ATM(details[0], details[1]).action()
    




    
        
        
