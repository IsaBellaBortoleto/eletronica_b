import subprocess
import sys
from pathlib import Path

# Roda cada script a partir desta pasta (cada um salva seu PNG ao lado)
pasta = Path(__file__).parent
for arquivo in ["3_1.py", "3_2.py", "3_3.py", "4_1.py", "4_2.py"]:
    print(f"\n--- {arquivo} ---")
    subprocess.run([sys.executable, arquivo], cwd=pasta, check=True)
