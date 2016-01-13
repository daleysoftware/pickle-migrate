#!/usr/bin/env python
import setuptools


with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()
    requirements = filter(lambda x: not x.startswith('#'), requirements)


setuptools.setup(
    name='picklemigrate',
    version='0.1',
    description='picklemigrate',
    long_description='A lightweight and simple migration tool for the pickleDB key-value store',
    author='Matt Pillar',
    author_email='matt@pillarcomputing.com',
    url='https://github.com/mpillar/pickle-migrate',
    packages=setuptools.find_packages(exclude=['tests']),
    install_requires=requirements,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
)
