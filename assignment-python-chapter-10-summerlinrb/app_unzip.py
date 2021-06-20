from pathlib import Path
from zipfile import ZipFile

path = Path("worldbank_zipfiles")
print("List of Directories")
path_of_directories = [p for p in path.iterdir() if p.is_dir()]
print(path_of_directories)

print("List of .zip files:")
path_of_zipfiles = [p for p in path.rglob("*.zip")]
print(path_of_zipfiles)

list_of_files = ["worldbank_zipfiles/Data_0.zip", "worldbank_zipfiles/Data_1.zip", "worldbank_zipfiles/Data_2.zip", "worldbank_zipfiles/Data_3.zip",
                 "worldbank_zipfiles/Data_4.zip", "worldbank_zipfiles/Data_5.zip", "worldbank_zipfiles/Data_6.zip", "worldbank_zipfiles/Data_7.zip", "worldbank_zipfiles/Data_8.zip"]
target_directory = "worldbank_zipfiles"
for file in list_of_files:
    with ZipFile(file) as zip:
        zip.extractall(target_directory)
print("Done Extracting from Multiple Files.")
