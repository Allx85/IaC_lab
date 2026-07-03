import os

path = os.path.expanduser("~/Downloads")

files = (os.listdir(path))

if os.path.exists(path):
    files = (os.listdir(path))
    print(f"You have {len(files)} files in Downloads folder")
else:
    print("The directory does not exist")

total_bytes = sum(
        os.path.getsize(os.path.join(path,f))
        for f in files
        if os.path.isfile(os.path.join(path,f))
)

total_gb = total_bytes / (1024 * 1024 * 1024)
rounded_value = (round(total_gb, 2))
print(f"You have {rounded_value} GB in your Downloads folder")