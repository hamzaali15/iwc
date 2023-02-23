from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in iwc/__init__.py
from iwc import __version__ as version

setup(
	name="iwc",
	version=version,
	description="Integrated Waves Contracting",
	author="Hamza Ali",
	author_email="malikhamzaali48@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
