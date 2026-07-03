import os
import glob

def replace_in_file(filepath, replacements):
    with open(filepath, 'r') as f:
        content = f.read()
    
    modified = False
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
            modified = True
            
    if modified:
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Reverted {filepath}")

icon_replacements = [
    ("Icons.AutoMirrored.Filled.VolumeUp", "Icons.Filled.VolumeUp"),
    ("Icons.AutoMirrored.Filled.Send", "Icons.Filled.Send"),
    ("Icons.AutoMirrored.Filled.TrendingUp", "Icons.Filled.TrendingUp"),
    ("Icons.AutoMirrored.Filled.ReceiptLong", "Icons.Filled.ReceiptLong"),
    ("Icons.AutoMirrored.Filled.TrendingDown", "Icons.Filled.TrendingDown"),
    ("Icons.AutoMirrored.Filled.ArrowBack", "Icons.Filled.ArrowBack"),
    ("Icons.AutoMirrored.Filled.ArrowForward", "Icons.Filled.ArrowForward"),
    ("Icons.AutoMirrored.Filled.ListAlt", "Icons.Filled.ListAlt"),
    ("Icons.AutoMirrored.Filled.List", "Icons.Filled.List"),
    ("Icons.AutoMirrored.Filled.Logout", "Icons.Filled.Logout"),
    ("Icons.AutoMirrored.Filled.KeyboardArrowRight", "Icons.Filled.KeyboardArrowRight"),
]

for filepath in glob.glob('app/src/main/java/**/*.kt', recursive=True):
    replace_in_file(filepath, icon_replacements)
