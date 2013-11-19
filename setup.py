from setuptools import setup, find_packages


setup(
	name = "reservoir-sampling-cli",
	version = "0.1",
	packages = find_packages(),
	entry_points = {
		'console_scripts': [
			'resamp = sampler.command_line:main',
		],
	},
	test_suite = "tests"
)
