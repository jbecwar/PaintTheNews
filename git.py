from datetime import datetime
import subprocess


def push():
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    result = subprocess.run(["git",  "add", "*"], capture_output=True, text=True)
    print(result.stdout)
    result = subprocess.run(["git", "commit", "-m", "Update " + timestamp], capture_output=True, text=True)
    print(result.stdout)
    result = subprocess.run(["git", "push"], capture_output=True, text=True) 
    print(result.stdout)
    print("Pushed to GitHub")
    return
