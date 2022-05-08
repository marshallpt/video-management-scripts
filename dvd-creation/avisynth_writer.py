import os

desired_extension = '.mpg'
working_directory = os.getcwd()
split_path = working_directory.split('\\')

project_name = split_path[len(split_path) - 1]
avs_name = project_name + '.avs'
batch_name = project_name + '.bat'

avs_file = open(avs_name, "w+")
file_list = os.scandir(os.curdir)

print(f"Operating path: {working_directory}\nFiles found: ")

count = 0
fileVal = ''

for entry in file_list:
	fileVal = entry.name
	if fileVal.find(desired_extension) != -1 and fileVal.find('.ffindex') == -1:
		print(entry.name)
		if count != 0:
			avs_file.write('  ++ \\\n')
		entry = f'FFmpegSource2("{working_directory}\\{fileVal}", atrack = -1)'
		avs_file.write(entry)
		count += 1


# Writing the batch file too because I'm lazy
batchFile = open(batch_name, "w+")
entry = f'ffmpeg -i {avs_name} -target ntsc-dvd -r 29.97 -s 720x480 -aspect 16:9 -b:v 8000k ' \
		f'{project_name}.mpeg \npause'
batchFile.write(entry)


# Closing all files
file_list.close
avs_file.close
batchFile.close
