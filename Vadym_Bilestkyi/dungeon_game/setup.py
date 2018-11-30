import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dungeon_game_from_vadym_biletskyi",
    version="0.0.1",
    author="Vadym Biletskyi",
    author_email="umpire333@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/umpire-3/campus_2018_python/tree/vadym-biletskyi/Vadym_Bilestkyi/dungeon_game",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
