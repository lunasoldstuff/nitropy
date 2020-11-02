import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="stampylongr", # Replace with your own username
    version="0.0.1",
    author="Robert Wilcox",
    author_email="contact@rororobby.ml",
    description="Proof-of-concept Discord Nitro code generator.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/stampylongr/nitropy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)