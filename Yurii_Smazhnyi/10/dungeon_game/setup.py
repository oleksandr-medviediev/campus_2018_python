import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dungeon_game_smazhnyi",
    version="0.0.1",
    author="Yurii Smazhnyi",
    author_email="yura.smazhny@gmail.com",
    description="Dunegon Game made during education",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/McMuzil/campus_2018_python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)