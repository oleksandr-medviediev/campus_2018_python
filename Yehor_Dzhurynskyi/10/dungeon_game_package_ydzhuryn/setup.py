import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dungeon_game_package_ydzhuryn",
    version="0.0.5",
    author="Yehor Dzhurynskyi",
    author_email="yehor.dzhurynskyi@ubisoft.com",
    description="dungeon game package ydzhuryn",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yehordzhurynskyi/campus_2018_python/tree/Yehor-Dzhurynskyi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)