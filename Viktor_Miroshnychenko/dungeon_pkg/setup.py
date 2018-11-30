import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "dungeon_game",
    version = '0.0.1',
    author = 'Viktor Mitoshnychenko',
    description = ' Study pakage',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/viktor-viktor/campus_2018_python',
    packages = setuptools.find_packages()
)