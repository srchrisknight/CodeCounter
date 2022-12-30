import os,sys,re
from pprint import pprint


def getFiles(codeDir, ext):
	codeFiles = []

	for r, d, f in os.walk(codeDir):
		for file in f:
			if file.endswith(".{}".format(ext)):
				codeFiles.append(os.path.join(r, file))

	return codeFiles


def countLines(files):
	lines = 0

	for file in files:
		with open(file, 'r') as codeFile:
			data = codeFile.readlines()

		for line in data:
			if re.search('\w', line) is not None:
				lines += 1

	return lines



if __name__ == '__main__':
	codePath = 'C:/Users/srchr/Documents/DownloadManager/'
	files = getFiles(codePath, 'py')
	lines = countLines(files)
	print(lines)
