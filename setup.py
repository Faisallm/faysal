import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "faisal",
    version = "0.0.1",
    author = "Faisal Lawan Muhammad",
    author_email = "Faisallawan1997@gmail.com",
    description = "Faisal",
    long_description = "Faisal",
    long_description_content_type = "text/markdown",
    url = "https://github.com/Faisallm/faysal",
    project_urls = {
        "Bug Tracker": "package issues URL",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.6"
)