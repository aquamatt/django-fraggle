from setuptools import setup, find_packages
import os

TEMPLATE_ROOT = 'src/fraggle/templates'
template_files = [os.path.join(TEMPLATE_ROOT, f) for f in os.listdir(TEMPLATE_ROOT)] 

setup(
    name = "fraggle",
    version = "0.3",
    
    packages = find_packages('src'),
    package_dir = {'':'src'},
    package_data = {'': ["templates/*.html",] },
)
