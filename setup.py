from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setup(
    name="iccsh",
    version="1.0.0",
    entry_points='''
        [console_scripts]
        iccsh=src.run:main
    ''',
    description=("A shell for executing algorithms related "
                 "to MATH3411 Information, Codes and Ciphers"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Hillary Chan",
    license="MIT",
    packages=find_packages(),
    install_requires=["colorama"],
    python_requires=">=3.6"
)
