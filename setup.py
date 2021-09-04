import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path("F:\VSCode Projects\Miscellaneous\logic-python\setup.py").parent

# The text of the README file
README = (HERE / "F:\VSCode Projects\Miscellaneous\logic-python\README.md").read_text()

# This call to setup() does all the work
setup(
    name="logic-python",
    version="1.0.0",
    description="This package makes mathematics very easy to use in python",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/realpython/reader",
    author="Animesh Biswas",
    author_email="animeshb2004@gmail.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["logic-python"],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "realpython=logic-python.__main__:main",
        ]
    },
)
