from pathlib import Path

def get_cats_info(path):   # Create function
    cats_file = Path(path)   #Convert input path (string) to Path object
    cats = []   # Create list to store all cat info
    
    try:
        with open (cats_file, encoding="utf-8") as file:   # Try to open file
            for line in file:
                line = line.strip()   # Remove leading and trailing whitespace
                if not line:   # Skip empty lines
                    continue
                line = line.split(",")   # Split the line by comma
                if len(line) != 3:   # Skip wrong lines
                    continue
                cat = {   # Create dict with cat info
                        "id": line[0].strip(),
                        "name": line[1].strip(),
                        "age": line[2].strip()
                        }
                cats.append(cat)   # Add cat dict to the list
    except(FileNotFoundError):   # Manage FileNotFoundError exception, print message
        print("File not found")
        
    return cats

cats_info = get_cats_info("cats.txt")
print(cats_info)
