#modules
import os 
import shutil

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

#creating the 4 folders
os.makedirs("Images", exist_ok=True)
os.makedirs("Documents", exist_ok=True)
os.makedirs("Music", exist_ok=True)
os.makedirs("Coding files", exist_ok=True)

#checking the files last name : 

for i in files : 
    if i.lower().endswith(image_extensions) :
        # print("Yes there is a file that ends with py")
        shutil.move(i,"Images/" + i)
    if i.lower().endswith(music_extensions):
        shutil.move(i,"Music/" + i)
    if i.lower().endswith(document_extensions):
        shutil.move(i,"Documents/"+i)
    