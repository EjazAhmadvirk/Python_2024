# ====================================
# 📘 Python File Handling Capsule
# Covers:
# 1. Open File (r, w, a, r+, x)
# 2. Read Entire File
# 3. Read Line by Line
# 4. Write File
# 5. Append File
# 6. Read/Write
# 7. With Statement
# 8. Check if File Exists
# 9. Delete File
# ====================================

import os

filename = "data.txt"  # Sample file name

# -------------------------------------
# 1. Creating/Opening File in Write Mode (Overwrite)
# -------------------------------------
file = open(filename, "w")  # Creates file or overwrites if exists
file.write("Hello Ejaz!\n")
file.write("This is the first line written using 'w' mode.\n")
file.close()

# -------------------------------------
# 2. Appending to File
# -------------------------------------
file = open(filename, "a")  # Appends to existing file
file.write("This line is added using 'a' (append) mode.\n")
file.close()

# -------------------------------------
# 3. Reading Entire File
# -------------------------------------
file = open(filename, "r")  # Opens file for reading
content = file.read()       # Reads whole file
print("=== Reading Entire File ===")
print(content)
file.close()

# -------------------------------------
# 4. Reading Line by Line
# -------------------------------------
file = open(filename, "r")
print("=== Reading Line by Line ===")
for line in file:
    print(line.strip())  # strip() removes newline characters
file.close()

# -------------------------------------
# 5. Read + Write Mode ('r+')
# -------------------------------------
with open(filename, "r+") as file:
    print("=== Using 'r+' (read + write) ===")
    print(file.read())
    file.write("Extra line added using r+ mode.\n")

# -------------------------------------
# 6. Using 'with' Statement (Auto-close)
# -------------------------------------
with open(filename, "a") as file:
    file.write("Line added using 'with' statement.\n")

with open(filename, "r") as file:
    print("=== File Content (with statement) ===")
    print(file.read())

# -------------------------------------
# 7. Check if File Exists
# -------------------------------------
if os.path.exists(filename):
    print(f"✅ The file '{filename}' exists.")
else:
    print(f"❌ The file '{filename}' does not exist.")

# -------------------------------------
# 8. Delete File (Optional)
# Uncomment below if you want to delete the file

# if os.path.exists(filename):
#     os.remove(filename)
#     print(f"🗑️ The file '{filename}' was deleted.")
# else:
#     print("The file does not exist, can't delete.")
