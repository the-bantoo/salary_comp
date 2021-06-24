from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in salary_comp/__init__.py
from salary_comp import __version__ as version

setup(
	name='salary_comp',
	version=version,
	description='Salary Components',
	author='Bantoo Accounting Innovations',
	author_email='technical@thebanto.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
