import os
import shutil
import subprocess
import tkinter
from tkinter import filedialog
from sys import executable



def gui():
	root = tkinter.Tk()
	root.withdraw()
	path_of_file = os.path.join(os.getcwd(), 'copycat.py')
	path = filedialog.askdirectory()


	for root, dirs, files in os.walk(path):
		for subfolder in dirs:
			try:
				if subfolder == "stop" or subfolder == ".git":
					continue
				new_path = os.path.join(root, subfolder, 'copycat.py')
				if os.path.exists(new_path):
					continue
				shutil.copy(path_of_file,new_path)
				print(f'Copied to {subfolder}')
				subprocess.Popen([executable, new_path])
				print(f'Successfully launched {new_path}')
			except Exception as e:
				print(f'Something went wrong: {e}')
				input("Press Enter to continue...")

def main(path:str):

	path_of_file = os.path.join(os.getcwd(), 'copycat.py')


	for root, dirs, files in os.walk(path):
		for subfolder in dirs:
			try:
				if subfolder == "stop" or subfolder == ".git":
					continue
				new_path = os.path.join(root, subfolder, 'copycat.py')
				if os.path.exists(new_path):
					continue
				shutil.copy(path_of_file,new_path)
				print(f'Copied to {subfolder}')
				subprocess.Popen([executable, new_path])
				print(f'Successfully launched {new_path}')
			except Exception as e:
				print(f'Something went wrong: {e}')
				input("Press Enter to continue...")
				
if __name__ == "__main__":
	gui()