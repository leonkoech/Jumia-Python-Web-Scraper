import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="jumiascraper-pkg-leonkoech",
    version="0.0.1",
    author="Leon Koech",
    author_email="leonkoechh@gmail.com",
    description="A jumia webscraping package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/leonkoech/Jumia-Python-Web-Scraper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)