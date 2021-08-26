from setuptools import setup, find_packages
import io
import os

VERSION = "1.1"

def get_long_description():
    with io.open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()

setup(
    name="doomsday",
    description="A command line Doomsday rule utility and trainer",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Bradley P. Allen",
    version=VERSION,
    license="MIT License",
    packages=find_packages(),
    install_requires=["click>=8.0.1"],
    setup_requires=["pytest-runner"],
    extras_require={"test": ["pytest"]},
    entry_points="""
        [console_scripts]
        doomsday=doomsday.cli:cli
    """,
    tests_require=["doomsday[test]"],
    url="https://github.com/bradleypallen/doomsday",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
