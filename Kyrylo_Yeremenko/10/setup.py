import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dungeon_game_",
    version="1.0.0",
    author="Kirill Yeremenko",
    author_email="erem275@gmail.com",
    description="Dungeon game coursework package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/erem2k/dungeon_game",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)