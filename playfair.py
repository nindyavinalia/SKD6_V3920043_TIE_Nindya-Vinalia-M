#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


key=input("Enter key")
key=key.replace(" ", "")
key=key.upper()
def matrix(x,y,initial):
   return [[initial for i in range(x)] for j in range(y)]
   
result=list()
for c in key: # kode ini merupakan kode untuk menyimpan kunci
   if c not in result:
       if c=='J':
           result.append('I')
       else:
           result.append(c)
flag=0
for i in range(65,91): # untuk menyimpan karakter lain
   if chr(i) not in result:
       if i==73 and chr(74) not in result:
           result.append("I")
           flag=1
       elif flag==0 and i==73 or i==74:
           pass    
       else:
           result.append(chr(i))
k=0
my_matrix=matrix(5,5,0) # inisialisasi matriks
for i in range(0,5): # membuat matriks
   for j in range(0,5):
       my_matrix[i][j]=result[k]
       k+=1

def locindex(c): # dapatkan lokasi setiap karakter
   loc=list()
   if c=='J':
       c='I'
   for i ,j in enumerate(my_matrix):
       for k,l in enumerate(j):
           if c==l:
               loc.append(i)
               loc.append(k)
               return loc
           
def encrypt():  # Kode Program Enkripsi
   msg=str(input("ENTER MSG:")) #menampilkan teks "ENTER MSG:" untuk menginputkan plaintext
   msg=msg.upper()
   msg=msg.replace(" ", "")             
   i=0
   for s in range(0,len(msg)+1,2):
       if s<len(msg)-1:
           if msg[s]==msg[s+1]:
               msg=msg[:s+1]+'X'+msg[s+1:]
   if len(msg)%2!=0:
       msg=msg[:]+'X'
   print("CIPHER TEXT:",end=' ') #menampilkan hasil enkripsi plaintext
   while i<len(msg):
       loc=list()
       loc=locindex(msg[i])
       loc1=list()
       loc1=locindex(msg[i+1])
       if loc[1]==loc1[1]:
           print("{}{}".format(my_matrix[(loc[0]+1)%5][loc[1]],my_matrix[(loc1[0]+1)%5][loc1[1]]),end=' ')
       elif loc[0]==loc1[0]:
           print("{}{}".format(my_matrix[loc[0]][(loc[1]+1)%5],my_matrix[loc1[0]][(loc1[1]+1)%5]),end=' ')  
       else:
           print("{}{}".format(my_matrix[loc[0]][loc1[1]],my_matrix[loc1[0]][loc[1]]),end=' ')    
       i=i+2        
                
def decrypt():  # Deskripsi
   msg=str(input("ENTER CIPHER TEXT:")) #menampilkan teks "ENTER CIPHER TEXT:" untuk menginputkan cipher text
   msg=msg.upper()
   msg=msg.replace(" ", "")
   print("PLAIN TEXT:",end=' ') #menampilkan hasil dekripsi dekripsi
   i=0
   while i<len(msg):
       loc=list()
       loc=locindex(msg[i])
       loc1=list()
       loc1=locindex(msg[i+1])
       if loc[1]==loc1[1]:
           print("{}{}".format(my_matrix[(loc[0]-1)%5][loc[1]],my_matrix[(loc1[0]-1)%5][loc1[1]]),end=' ')
       elif loc[0]==loc1[0]:
           print("{}{}".format(my_matrix[loc[0]][(loc[1]-1)%5],my_matrix[loc1[0]][(loc1[1]-1)%5]),end=' ')  
       else:
           print("{}{}".format(my_matrix[loc[0]][loc1[1]],my_matrix[loc1[0]][loc[1]]),end=' ')    
       i=i+2        

while(1):
   choice=int(input("\n 1.Encryption \n 2.Decryption: \n 3.EXIT")) #menginputkan menu yang ada
   if choice==1: #menjalankan menu 1
       encrypt()
   elif choice==2: #menjalankan menu 2
       decrypt()
   elif choice==3: #menjalankan menu 3
       exit()
   else:
       print("Choose correct choice")


# In[ ]:




