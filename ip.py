import pymysql

#+++++++++++++++++++++++++++MAIN PROGRAM+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
def main():
   ip = input('give an ip number to calculate your net_ID\n')
   ipclass = input ('give the class of the IP(A B OR C)\n') 
   ipconv(ip,ipclass)
   ask = input('Do tou want to write this info to the database yes or no?!\n')
   if ask =='yes':
        try:
            
            conn = pymysql.connect(host="localhost", port=3306, user="chrigeta", passwd="vegeta1988", db="test")
            cur = conn.cursor()
            cur.execute('INSERT INTO test.ips  VALUES (%s,%s,%s)',(ip,net_id,submask))
            conn.commit()
            print('Succesful Database Entry')
        except pymysql.err.IntegrityError:
            print('duplicate entry for the primary key')
            exit
        ask2 = input('Do you want to see all the other entries in the table yes or no?!\n')
        if ask2 =='yes':
            cur.execute("SELECT * FROM test.ips")
            for r in cur.fetchall():
                print(r)
            asking()
        else:
           asking() 
           
   else:
        asking()
   
   
#+++++++++++++++++++++++++++MAIN PROGRAM+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++  
   

#a funtion that takes the ip and class 
def ipconv(ip,ipclass):
    global submask
    global net_id
    iplen = len(ip)   
    while   ip.isalpha():
        print ('No letters allowed in the ip form')
        exit()
        
    if (iplen<10 or iplen>15):
        print('too small for an ip or too big')
        exit()
    
#findind the position of every dot of the ip given     
    p1 = ip.find('.')
    print('in the position',p1,'the first .')
    p2 = ip[p1+1:iplen].find('.')
    p2 = p2+p1+1
    print('in the position',p2,'the second .')    
    p3 = ip[p2+1:iplen].find('.')
    p3=p2+p3+1
    print('in the position',p3,'the third .')

#converting every part of the ip to integer to do the bitwise end 
    i1 = int(ip[0:p1])
    print('the conversion to integer gives:',i1)
    i2 = int(ip[p1+1:p2])
    print('the conversion to integer gives:',i2)
    i3 = int(ip[p2+1:p3])
    print('the conversion to integer gives:',i3)
    i4 = int(ip[p3+1:iplen])
    print('the conversion to integer gives:',i4)

    if (i1>255 or i2>255 or i3>255 or i4>255) :
        print('not valid ip')
        asking()
        exit()
        
    if ipclass=='A':
        
        submask='255.255.255.0'
        cp1 = (i1 & 255)
        cp2 = (i2 & 255)
        cp3 = (i3 & 255)
        cp4 = (i4 & 0)
        #converting the subnet mask to string inorder to write it to the database
        sp1 = str(cp1)
        sp2 = str(cp2)
        sp3 = str(cp3)
        sp4 = str(cp4)
        net_id =sp1+'.'+sp2+'.'+sp3+'.'+sp4
        print('the net_id produced from the given ip is:',net_id)
        
    elif ipclass=='B':
        submask='255.255.0.0'
        cp1 = (i1 & 255)
        cp2 = (i2 & 255)
        cp3 = (i3 & 0)
        cp4 = (i4 & 0)
        
        sp1 = str(cp1)
        sp2 = str(cp2)
        sp3 = str(cp3)
        sp4 = str(cp4)
        net_id =sp1+'.'+sp2+'.'+sp3+'.'+sp4
        print('the net_id produced from the given ip is:',net_id)
        
    elif ipclass=='C':
        submask='255.0.0.0'
        cp1 = (i1 & 255)
        cp2 = (i2 & 0)
        cp3 = (i3 & 0)
        cp4 = (i4 & 0)
        
        sp1 = str(cp1)
        sp2 = str(cp2)
        sp3 = str(cp3)
        sp4 = str(cp4)
        net_id =sp1+'.'+sp2+'.'+sp3+'.'+sp4
        print('the net_id produced from the given ip is:',net_id)
        
    else:
        print('not valid class for an ip')
        restart = input('do you want to try again yes or no\n')
        if restart=='yes':
            main()
        else:
            exit()    
        
    return

#a function to avoid all this stupid and continuous asking!! 
def asking():
   ask3 = input('Do you want to continue the ip conversions yes or no?!\n')   
   if ask3=='yes':
      main()
   elif ask3=='no':
       print('have a nice day mate')       
       exit
   else:
       print('not valid answer , try again')
       asking()
   return
#i dont want to write every time the main() in the shell, so thats the reason for the last line!
 
main()
#for not closing the cmd after the end of main!     
stop=input('press enter to finish')
#for not closing the cmd after the end of main!





        
        
    

    
          
            
      
      
    
