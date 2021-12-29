import setuptools
import os


def package_files(directory):
    # https://stackoverflow.com/questions/27664504/how-to-add-package-data-recursively-in-python-setup-py/27664856
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths


original_files = package_files('transparent_star/original')
output_files = package_files('transparent_star/output')


with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="transparent_star",
    version="0.1.0.0",
    author="Selewirre Iskvary",
    author_email="selewirre@gmail.com",
    description="A tool for adding transparent background to a stellar image of your choice.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/selewirre/transparent_star",
    packages=setuptools.find_packages(),
    package_dir={'transparent_star': 'transparent_star'},
    package_data={'transparent_star': original_files + output_files},
    install_requires=['pillow',
                      'numpy',
                      'pyqt5'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GNU GPL v3 license",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)

