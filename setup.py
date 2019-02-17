from setuptools import setup, find_packages


with open('README.md') as file:
    long_description = file.read()

setup(
    name="webmail-domains",
    version="0.22",
    packages=find_packages(),
    url='https://github.com/zevaverbach/Webmail-Domains',
    description=('A pretty thorough list of webmail domains!'),
    long_description_content_type='text/markdown',
    long_description=long_description,
        )
