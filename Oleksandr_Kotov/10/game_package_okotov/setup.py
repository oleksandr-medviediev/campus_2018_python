import setuptools

with open("README.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name="game_package_okotov",
    version="10.1",
    author="Oleksandr Kotov",
    author_email="alxkot@gamil.com",
    description="My little Dungeon Game",
    long_description=long_description,
    url="https://github.com/okotov/campus_2018_python/tree/master/Oleksandr_Kotov/10",
    packages=setuptools.find_packages(),
)