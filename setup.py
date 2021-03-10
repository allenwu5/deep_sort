"""
Based on https://packaging.python.org/tutorials/packaging-projects/
"""
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="deep-sort", 
    version="0.0.1",
    author="",
    author_email="",
    description="Deep Sort Tracker",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/allenwu5/deep_sort",
    project_urls={
        "Bug Tracker": "https://github.com/allenwu5/deep_sort",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL-3.0 License",
        "Operating System :: OS Independent",
    ],
    packages=['deep_sort'],
    python_requires=">=3.6",
)
