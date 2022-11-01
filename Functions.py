import csv
def display(state):
    fobj=open('tourism.csv','r')
    treader=csv.reader(fobj)
    for i in treader:
        if i[0]==state:
            print('The best tourist spot of',state,'is',i[1])
            print(i[2])
            print('The best places in this spot are:',i[3])
            print('GOOGLE MAP RATINGS:',i[4])
            print(i[5])

          
