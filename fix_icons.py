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
        print(f"Fixed {filepath}")

icon_replacements = [
    ("Icons.Filled.VolumeUp", "Icons.AutoMirrored.Filled.VolumeUp"),
    ("Icons.Filled.Send", "Icons.AutoMirrored.Filled.Send"),
    ("Icons.Filled.TrendingUp", "Icons.AutoMirrored.Filled.TrendingUp"),
    ("Icons.Filled.ReceiptLong", "Icons.AutoMirrored.Filled.ReceiptLong"),
    ("Icons.Filled.TrendingDown", "Icons.AutoMirrored.Filled.TrendingDown"),
    ("Icons.Filled.ArrowBack", "Icons.AutoMirrored.Filled.ArrowBack"),
    ("Icons.Filled.ArrowForward", "Icons.AutoMirrored.Filled.ArrowForward"),
    ("Icons.Filled.ListAlt", "Icons.AutoMirrored.Filled.ListAlt"),
    ("Icons.Filled.List", "Icons.AutoMirrored.Filled.List"),
    ("Icons.Filled.Logout", "Icons.AutoMirrored.Filled.Logout"),
    ("Icons.Filled.KeyboardArrowRight", "Icons.AutoMirrored.Filled.KeyboardArrowRight"),
    ("Icons.Default.VolumeUp", "Icons.AutoMirrored.Filled.VolumeUp"),
    ("Icons.Default.Send", "Icons.AutoMirrored.Filled.Send"),
    ("Icons.Default.TrendingUp", "Icons.AutoMirrored.Filled.TrendingUp"),
    ("Icons.Default.ReceiptLong", "Icons.AutoMirrored.Filled.ReceiptLong"),
    ("Icons.Default.TrendingDown", "Icons.AutoMirrored.Filled.TrendingDown"),
    ("Icons.Default.ArrowBack", "Icons.AutoMirrored.Filled.ArrowBack"),
    ("Icons.Default.ArrowForward", "Icons.AutoMirrored.Filled.ArrowForward"),
    ("Icons.Default.ListAlt", "Icons.AutoMirrored.Filled.ListAlt"),
    ("Icons.Default.List", "Icons.AutoMirrored.Filled.List"),
    ("Icons.Default.Logout", "Icons.AutoMirrored.Filled.Logout"),
    ("Icons.Default.KeyboardArrowRight", "Icons.AutoMirrored.Filled.KeyboardArrowRight"),
]

for filepath in glob.glob('app/src/main/java/**/*.kt', recursive=True):
    replace_in_file(filepath, icon_replacements)
