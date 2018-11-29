import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dungeon_game_pkg",
    version="0.0.1",
    author="Volodymyr Kuksa",
    description="A small study package",
    long_description=long_description,
    long_description_content_type="markdown",
    url="https://github.com/VolodymyrKuksa/campus_2018_python",
    packages=setuptools.find_packages()
)
