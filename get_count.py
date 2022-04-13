import glob
total_files = glob.glob('Chennai/*')
total_folders = glob.glob('Chennai/Chennai*')
print(total_folders)
print(len(total_files))

