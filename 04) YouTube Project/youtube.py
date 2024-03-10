import json

# Take data from json file
def data():
    try:
     with open("youtube.txt",'r') as file : #load : read the content of txt file and store it in a variable 'data'
         return json.load(file)
    except FileNotFoundError:
        return []
    
# Saving the data
def save(video):
    with open("youtube.txt",'w') as file : #dump : write
        json.dump(video,file)    
         
# enumerate : Data collection as a parameter and returns an object & its returned in a key-value pair format
def list(video):
    print("*"*70)
    for index , video in enumerate(video,start=1):
        print(f"{index}. Video : {video['name']} , Duration: {video['time']}")
    print("\n","*"*70)
  
# Video Add Function
def add(video):
    name = input("Enter video name : ")
    time = input("Enter video time : ")
    video.append({'name':name,'time':time})
    save(video)
    
    
# Video Update Function
def update(video):
    list(video)
    index = int(input("Enter the video Number to Update : "))
    
    if 1<= index<=len(video):
        name = input("Enter the new video Name : ")
        time = input("Enter the new video Time : ")
        video[index-1] = {'name':name,'time':time}
        save(video)
    else : 
        print('Invalid Video Index Selected')    
        
# Video Delete Function
def delete(video):
    list(video)
    index = int(input("Enter the video Number to Delete : "))
    
    if 1<= index<=len(video):
        del video[index-1]
        save(video)
    else : 
        print('Invalid Video Index Selected')    
        

def main():
        video=data()
        while True :
            print("\n Youtube Manager | Choose an Option : \n")
            print(" 1. List all Youtube videos  ")
            print(" 2. Add a Youtube videos  ")
            print(" 3. Update a Youtube videos Details  ")
            print(" 4. Delete Youtube videos  ")
            print(" 5. Exit the App  ")
            print("\n")
            a= input("Enter your choice : ")
            
            match a :
                case '1':
                    print("\n")
                    list(video)
                    
                case '2':
                    print("\n")
                    add(video)
                    
                case '3':
                    print("\n")
                    update(video)
                    
                case '4':
                    print("\n")
                    delete(video)
                    
                case '5':
                    break
                
                case _:
                    print("Invalid Choice ...!!")    
                    

# Call the main function 
if __name__ == "__main__":
    main()                    