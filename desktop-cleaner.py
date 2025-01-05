import os
import shutil



def createSubFolder(subFolderName, folderPath):
    subFolder_path = os.path.join(folderPath ,subFolderName)
    if not os.path.exists(subFolder_path):
        os.makedirs(subFolder_path)
    return subFolder_path


def cleaner(folderPath):
    for fileName in os.listdir(folderPath):
        filePath = os.path.join(folderPath, fileName)
        if os.path.exists(filePath):
            type = fileName.split('.')[-1].lower()
            if type:
                subfolderName = f"{type.upper()} Files"
                subfolderPath = createSubFolder(subfolderName, folderPath)
                shutil.move(filePath, subfolderPath)
                print(f"Moved: {fileName} to {subfolderName}")



if __name__ == "__main__":
    print("Dekstop Cleaner")
    downloadsPath = "/Users/mohd.muhtasimbashar/Downloads"
    if os.path.isdir(downloadsPath):
        cleaner(downloadsPath)
        print("Cleaning Complete")
    else:
        print("Invalid path!, There is no such directory. Try again with a correct folder path.")