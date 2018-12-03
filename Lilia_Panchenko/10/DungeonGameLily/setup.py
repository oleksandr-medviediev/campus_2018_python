# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(

    name='dungeongamelily2', 

    version='4.0.1',

    description='Dungeon game project',

    long_description=long_description,

    url='https://github.com/LiliaPanda/DungeonGameLily',

    classifiers=[ 
        'Development Status :: 2 - Pre-Alpha',

        'Intended Audience :: Education',
        'Topic :: Software Development',

        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.7',
    ],

    keywords='educational development',  # Optional

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target
    # platform.
    #
    # For example, the following would provide a command called `sample` which
    # executes the function `main` from this package when invoked:
    entry_points={  # Optional
        'console_scripts': [
            'startgame=dungeongame:start',
        ],
    },

)
