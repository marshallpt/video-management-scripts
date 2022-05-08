import os


fullPath = os.getcwd()
pathSplit = fullPath.split('\\')

directoryName = pathSplit[len(pathSplit)-1]
avsFileName = directoryName + '.avs'
batchFileName = directoryName + '.bat'

avsFile = open(avsFileName, "w+")
fileList = os.scandir(os.curdir)

# Debugging Outputs
print(fullPath)
print(pathSplit)
print(len(pathSplit))

count = 0
fileVal = ''
lineToWrite = ''

for entry in fileList:
	fileVal = entry.name
	if fileVal.find('.MOD') != -1 and fileVal.find('.ffindex') == -1:
		print(entry.name)
		if count != 0:
			avsFile.write('  ++ \\\n')
		lineToWrite = 'FFmpegSource2("' + fullPath + '\\' + fileVal + '", atrack = -1)'
		avsFile.write(lineToWrite)
		count += 1

# Closing things that need to be closed
fileList.close
avsFile.close

# Writing the batch file too because I'm lazy
batchFile = open(batchFileName, "w+")
batchLine = 'ffmpeg -i ' + avsFileName + ' -target ntsc-dvd -r 29.97 -s 720x480 -aspect 16:9 -b:v 8000k ' + directoryName + '.mpeg \npause' 
batchFile.write(batchLine)

batchFile.close
