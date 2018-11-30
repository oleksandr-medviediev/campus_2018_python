#https://test.pypi.org/project/map-test-package/

import setuptools


setuptools.setup(
    name="map_test_package",
    version="0.0.2",
    author="Serhii Oliinyk",
    description="Package contsains file for creating map for dungeon game.",
    url="https://github.com/Serhiyko/Python_project_packaging",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)
