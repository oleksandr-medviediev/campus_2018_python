import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dungeon_game_afokin",
    version="0.10.1",
    author="Fokin Andrii",
    author_email="andrikred@gmail.com",
    description="My first python project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fox998/campus_2018_python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)