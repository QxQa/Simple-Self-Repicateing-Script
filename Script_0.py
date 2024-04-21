import os

# Extract the number from the filename
Script_Name = os.path.basename(__file__)
Script_Num = int(Script_Name.split("_")[1].split(".")[0])

# Get path to the New file
File_Path = os.path.join(os.path.dirname(__file__), f"Script_{Script_Num + 1}.py")

# Read the content of the current script
with open(__file__, "r") as f:
    content = f.read()

# Write the contents to the New File
with open(File_Path, "w") as f:
    f.write(content)
    f.close()

# Execute the next script
os.system(File_Path)


