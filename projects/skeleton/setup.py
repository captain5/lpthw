try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'My Project',
	'author': 'Captain',
	'url': 'https://github.com/captain5/lpthw/projects/sketon',
	'download_url': 'Where to download it.',
	'author_email': 'captain5abc@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': '',
	'scripts': '[]',
	'name': 'sketon'
}

setup(**config)
