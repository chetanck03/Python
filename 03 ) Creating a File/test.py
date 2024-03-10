# Create a File : 
file=open('test.txt','w')

# Method 1 :

try:
    file.write("chetan ck")
finally:
    file.close()    
    
# Method 2 : 

with open("chetan.txt","w") as file :
    file.write("gautam")    