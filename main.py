from pathlib import Path
import hashlib
import json



folder = Path("files")



def create_baseline():
    file_hashes={}
    for file in folder.iterdir():
        if file.is_file():
            file_hash = hashlib.sha256(file.read_text().encode()).hexdigest()
        
            file_hashes[file.name] = file_hash


        
    with open("baseline.json","w") as file:
            json.dump(file_hashes, file)
    
    print("Baseline created successfully") 
def monitor_files():
    
    with open("baseline.json","r")as file:
        old_hashes= json.load(file)

    new_hashes= {}

    for file in folder.iterdir():
        if file.is_file():
            file_hash = hashlib.sha256(file.read_text().encode()).hexdigest()
            new_hashes[file.name]= file_hash

    print(new_hashes)

    for filename in old_hashes:
        if filename not in new_hashes:
            print(filename,"DELETED")
            
        elif old_hashes[filename] == new_hashes[filename]:
            print(filename, "Unchanged")
        else:
            print(filename, "Modified")
            
    for filename in new_hashes:
        if filename not in old_hashes:
            print(filename, "NEW FILE DETECTED")   

choice = input("1. Create baseline\n2. Monitor files\n")

if choice == "1":
    create_baseline()

elif choice == "2":
    monitor_files()  
