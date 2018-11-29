from setuptools import setup, find_packages

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name="dungeon_game_stereotype_pkg",
    version="0.0.5",
    author="Dmytro Skorobohatskyi",
    author_email="skorobogatskiidima@gmail.com",
    description="The dungeon game package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Stereotype97/campus_2018_python/tree/Dmytro_Skorobohatskyi",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
