from setuptools import setup, find_packages


with open('README.md') as file:
    long_description = file.read()

setup(
    name="webmail-domains",
    version="0.12",
    py_modules="webmail_domains",
    url='https://github.com/zevaverbach/Webmail-Domains',
    include_package_data=True,
    packages=find_packages(),
    description=('A pretty thorough list of webmail domains!'),
    long_description_content_type='text/markdown',
    long_description=long_description,
        )
