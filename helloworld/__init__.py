import pkgutil
def __read_version_txt():
return pkgutil.get_data('helloworld', 'VERSION.txt').decode('utf-8').strip()
__version__ = __read_version_txt()
