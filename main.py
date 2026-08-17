#modules
import os 
import shutil

#protected files : 
protected_files = {
    "main.py",
    "README.md",
    ".gitattributes"

}
protected_folders = (
    ".git",
    "Images",
    "Music",
    "Documents"
)

#entensions for coading files

coding_extensions = (
    ".py",
    ".js",
    ".ts",
    ".jsx",
    ".tsx",
    ".html",
    ".css",
    ".java",
    ".c",
    ".cpp",
    ".h",
    ".hpp",
    ".cs",
    ".php",
    ".rb",
    ".go",
    ".rs",
    ".swift",
    ".kt",
    ".kts",
    ".dart",
    ".lua",
    ".r",
    ".sql",
    ".sh",
    ".bat",
    ".ps1",
    ".json",
    ".xml",
    ".yaml",
    ".yml",
    ".md"
)


#image extensions
image_extensions = (
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".bmp",
    ".webp",
    ".tiff",
    ".tif",
    ".svg",
    ".ico",
    ".heic",
    ".heif",
    ".avif"
)
#music extension : 
music_extensions = (
    ".mp3",
    ".wav",
    ".flac",
    ".aac",
    ".ogg",
    ".m4a",
    ".wma",
    ".opus",
    ".aiff",
    ".alac"
)
#document extensions : 
document_extensions = (
    ".pdf",
    ".doc",
    ".docx",
    ".txt",
    ".rtf",
    ".odt",
    ".xls",
    ".xlsx",
    ".csv",
    ".ppt",
    ".pptx",
    ".odp",
    ".ods"
)
#listing the files
files = os.listdir()
print(type(files))


#asking the user to enter the folders name and how many he wants to create
folder_num = int(input("Enter how many folders you want to add : "))
folder_list = []
for i in range(folder_num):
    folder_name = input("Enter the folder's name : ")
    folder_list.append(folder_name)
print(folder_list)

#the folder rules : 
folder_rules = {}
#creating the 4 folders
for i in folder_list : 
    os.makedirs(i, exist_ok=True)

#asking the user what folder will contain which type of files
for i in folder_list: 
    folder_contains = input(f"What type of files will {i} contain? ")
    folder_rules[i] = folder_contains
print(folder_rules)
#checking the files last name : 

for i in files : 
    if i in protected_files :
        continue
    if i in protected_folders : 
        continue
    if i.lower().endswith(image_extensions) :
        # print("Yes there is a file that ends with py")
        shutil.move(i,"Images/" + i)
    if i.lower().endswith(music_extensions):
        shutil.move(i,"Music/" + i)
    if i.lower().endswith(document_extensions):
        shutil.move(i,"Documents/"+i)
    if i.lower().endswith(coding_extensions):
        shutil.move(i,"Coding/"+i)