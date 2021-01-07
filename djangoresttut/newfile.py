from pathlib import Path
import os
# directory of overall project or the directory which contains manaage.py file
Base_dir = Path(__file__).resolve().parent.parent
template_dir = os.path.join(Base_dir, 'templates')
print(Base_dir)
print(template_dir)
BASE_DIR = Path(__file__).resolve().parent.parent
print(os.path.join(BASE_DIR, 'templates'))
