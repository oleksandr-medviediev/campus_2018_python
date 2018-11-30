import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="dungeon_game_kliukina",
    version="0.0.1",
    author="Kateryna Liukina",
    author_email="katel199614@gmail.com",
    description="Dungeon game",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/les0714/campus_2018_python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
