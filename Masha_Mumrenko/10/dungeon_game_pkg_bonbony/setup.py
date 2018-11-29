import setuptools

with open("README.md", "r") as file:
    long_description = file.read()

setuptools.setup(
    name="dungeon_game_pkg_bonbony",
    version="0.0.1",
    author="Mumrenko Masha",
    author_email="mr.mashaishere@gmail.com",
    description="A dungeon game package bu bonbony",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bonbony/campus_2018_python/tree/master/Masha_Mumrenko",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
