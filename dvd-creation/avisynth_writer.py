import os

vid_extension = '.mpg'
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
	if entry.name.find(vid_extension) != -1 and entry.name.find('.ffindex') == -1:
		print(entry, end='')
		print(os.path.getmtime(entry))
		if count != 0:
			avs_file.write('  ++ \\\n')
		avs_line = f'FFmpegSource2("{entry.path}", atrack = -1)'
		avs_file.write(avs_line)
		count += 1


# Writing the batch file too because I'm lazy
batch_file = open(batch_name, "w+")
batch_line = f'ffmpeg -i {avs_name} -target ntsc-dvd -r 29.97 -s 720x480 -aspect 16:9 -b:v 8000k ' \
		f'{project_name}.mpeg \npause'
batch_file.write(batch_line)


# Closing all files
file_list.close
avs_file.close
batch_file.close
