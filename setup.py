from setuptools import setup
import os
import sys

if sys.version_info[0] < 3:
    with open('README.rst') as f:
        long_description = f.read()
else:
    with open('README.rst', encoding='utf-8') as f:
        long_description = f.read()


setup(
    name='SNgramExtractor',
    version='0.0.4',
    description='Implementation of syntactic n-grams (sn-gram) extraction',
    long_description=long_description,
    long_description_content_type='text/markdown',  # This is important!
    author='StatguyUser',
    url='https://github.com/StatguyUser/SNgramExtractor',
    install_requires=['spacy','spacy[en_core_news_md]'],
    download_url='https://github.com/StatguyUser/SNgramExtractor.git',
    py_modules=["SNgramExtractor"],
    package_dir={'':'src'},
)
