from setuptools import setup, find_packages


setup(
	name = "reservoir-sampling-cli",
	version = "0.1",
	description = "A command line tool to randomly sample k items from an input S containing n items.",
	long_description=open('README.md').read(),
	url = "https://github.com/RyanBalfanz/reservoir-sampling-cli",
	license = 'MIT',
	author = "Ryan Balfanz",
	author_email = "ryan@ryanbalfanz.net",
	packages = find_packages(),
	entry_points = {
		'console_scripts': [
			'resamp = sampler.command_line:main',
		],
	},
	include_package_data = True,
	exclude_package_data = { '': ['README.md'] },
	test_suite = "tests"
)
