import os,sys,re
from pprint import pprint


def getFiles(codeDir, ext):
	codeFiles = []

	for r, d, f in os.walk(codeDir):
		for file in f:
			if file.endswith(".{}".format(ext)):
				if 'numpy'.lower() not in r.lower():
					codeFiles.append(os.path.join(r, file))

	return codeFiles


def countLines(files):
	lines = 0

	for file in files:
		with open(file, 'r') as codeFile:
			data = codeFile.readlines()

		lines += len(data)

	return lines



if __name__ == '__main__':
	codePaths = [
		'C:/Users/Chris/Documents/ProtoPipe_1.1/applications',
		'C:/Users/Chris/Documents/ProtoPipe_1.1/ProtoPipe',
		'C:/Users/Chris/Documents/ProtoPipe_1.1/tools'
	]

	lines = 0
	for path in codePaths:
		files = getFiles(path, 'py')
		lines += countLines(files)

	print(lines)
