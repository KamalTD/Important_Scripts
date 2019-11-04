"""
Script to Install modules in python 3

Using script:

        import sys

        sys.path.append("path/install_module.py") # replace 'path' by the directory of install_module.py 

        import install_module

        install_module.install("module_name") # replace "module_name" by the module you need to install as String

        

"""
def install(module_name):
	try:
	    from pip import main as pipmain
	except:
	    from pip._internal import main as pipmain
	pipmain(['install','%s'%module_name])
