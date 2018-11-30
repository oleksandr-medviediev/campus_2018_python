import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TKDungeonGamePkg",
    version="0.0.1",
    author="Tihran Katolikian",
    author_email="moreggmoreskill@icloud.com",
    description="Dungeon game",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SleepingSoul/campus_2018_python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
