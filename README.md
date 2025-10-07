# 🐍 CopyCat

**CopyCat** is a harmless educational Python script that mimics the behavior of a self-replicating worm.  
When executed, it scans the current working directory and recursively copies itself into each subfolder, then launches a copy from each newly infected folder.

## 🚀 How It Works

- The script locates itself using `os.getcwd()` and `__file__`.
- It uses `os.walk()` to iterate through subdirectories.
- It copies itself with `shutil.copy()` into each folder (if not already present).
- Each copy is then launched via `subprocess.Popen()` using the Python interpreter that ran the original script.

This way, the script "spreads" recursively through subfolders — each copy creates more copies, like a digital copycat.

## ⚠️ Warning

**DO NOT** run this script in:
- the root of your drive (e.g., `C:\`, `/`, or `C:/Users/YourName`)
- folders with important files
- directories with system or sensitive data

The script will flood every subdirectory with copies of itself and start them, which may:
- clutter your filesystem
- slow down your computer
- make cleanup annoying

Use it in a safe, disposable testing folder **only**.

## 🚫 Ignored Folders

The script ignores folders named .git and stop to avoid replicating into version control directories or intentionally excluded locations.

## 🔧 Requirements

- Python 3.x (no external libraries needed)

## 📜 License

This project is licensed under **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0)**.

 - If you fork this project, you must clearly state that it is a fork of the original.
 - Forks must be licensed under the same license
 - Commercial use is not allowed - you can't make money from this project

For more details, see the full license here: [https://creativecommons.org/licenses/by-nc-sa/4.0/](https://creativecommons.org/licenses/by-nc-sa/4.0/)

## 📘 Disclaimer

This script is intended for **educational purposes only**. It does not damage data, but can cause system slowdowns or clutter. Use responsibly and only in controlled environments.

## 📂 Versions

CopyCat versions:
- copycat.py - main file
- copycat-for-exe.py - copycat.py prepared to compile to exe file (pyinstaller)
- copycat.exe - compiled copycat-for-exe.py
- copycatcp.py - a copycat.py with choosing a path (Tkinter GUI or main(path) function on import) to force, needs a normal copycat.py file in the same directory