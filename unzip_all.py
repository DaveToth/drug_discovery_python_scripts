import subprocess

files = subprocess.run(['find', '.', '-name', '*.gz'], capture_output=True, text=True)

file_list = files.stdout.split('\n')

for file in file_list:
    if file.strip() != '':
         subprocess.run(['gunzip','-rk', file])
         #print(file)
