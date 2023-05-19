import os

def dirModulesImportStatement(
	moduleDirPath: str, 
	except_modules: set = {"base.py", "__init__.py", "__pycache__"}
	):

	modules = set(os.listdir(moduleDirPath)) - except_modules

	importStatement = ""

	for mod in sorted(modules):
		mod = "".join(mod.split(".")[:-1])

		importStatement += f"from .{mod} import *\n"

	return importStatement

def generateModuleImportInit(moduleDirPath):
	importStatement = dirModulesImportStatement(moduleDirPath)

	initFilePath = os.path.join(moduleDirPath, "__init__.py")
	initFilePathContent = ""

	with open(initFilePath, "r") as file:
		initFilePathContent = file.read()
	
	# print(initFilePathContent)
	# print(importStatement)
	
	if initFilePathContent != importStatement:
		print(initFilePath)
		# exit()
		with open(initFilePath, "w") as file:
			file.write(importStatement)
		
		print(f"update {initFilePath}")
		
