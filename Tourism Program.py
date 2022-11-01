#Python program which suggests the best places in to visit in different states
print('BEST TOURIST PLACE IN EACH STATE OF INDIA')

import csv
import Functions
L=['Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chattisgarh','Goa','Gujarat','Haryana','Himachal','Pradesh','Jharkhand','Karnataka','Kerala','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal'] 
while True:
    state=input('Please select the state in which you would like to visit: ')
    if state in L:
        Functions.display(state)
        break
    else:
        print('Enter the correct state')





                            
