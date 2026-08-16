import os 

#listing the files
files = os.listdir()
print(files)

#creating the 3 folders
os.makedirs("Images", exist_ok=True)

#checking the files last name : 
