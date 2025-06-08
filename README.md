# 🐍 Copycat

**Copycat** is a harmless educational Python script that mimics the behavior of a self-replicating worm.  
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

## 📄 Example

Suppose your folder looks like this:
project/
├── copycat.py
├── demo/
│ └── test/
└── notes/
After running `copycat.py`, each subfolder (`demo/`, `demo/test/`, `notes/`) will contain a new copy of the script, and each will launch its own process.

## 🔧 Requirements

- Python 3.x (no external libraries needed)

## 📜 License

MIT License – do whatever you want with this code, but leave attribution.

## 📘 Disclaimer

This script is intended for **educational purposes only**. It does not damage data, but can cause system slowdowns or clutter. Use responsibly and only in controlled environments.
