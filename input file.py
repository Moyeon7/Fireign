#input file
import csv
f1=open('tourism.csv','a')
twriter=csv.writer(f1)
count=0
while True:
   A=input('Enter a state to be filled')
   while True:
        B=input('Enter a tourist spot for this state:')
        while True:
                C=list()
                while True:
                   ans=input('do you want to enter more para:')
                   if ans=='y':
                      S=input('enter more para:')
                      C.append(S)
                   else:break
                E=list()
                while True:
                   ans=input('do you want to enter more places:')
                   if ans=='y':
                      X=input('enter more places:')
                      E.append(X)
                   else:break
                F=eval(input('Enter the google map ratings:'))
                D=list()
                while True:
                   ans=input('do you want to enter more conditions:')
                   if ans=='y':
                      Y=input('enter more conditions:')
                      D.append(Y)
                   else:break
                info=[A,B,C,E,F,D]
                f1=open('tourism.csv','a+')
                twriter=csv.writer(f1)
                twriter.writerow(info)
                f1.close()
                break
        break
                
                

        
        

        


