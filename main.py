import os

path = os.path.expanduser("~/Downloads")

try:
        files = (os.listdir(path))
except FileNotFoundError:
        print("Downloads folder cannot be found.")
        exit(1)
       
print(f"You have {len(files)} files in Downloads folder")

total_bytes = sum(
        os.path.getsize(os.path.join(path,f))
        for f in files
        if os.path.isfile(os.path.join(path,f))
)

total_gb = total_bytes / (1024 * 1024 * 1024)
rounded_value = (round(total_gb, 2))
print(f"You have {rounded_value} GB in your Downloads folder")