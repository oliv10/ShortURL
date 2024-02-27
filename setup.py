from setuptools import setup, find_packages

setup(
    name='Package Name',
    version='0.1.0',
    url='',
    author='Author',
    author_email='',
    description='',
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=[

    ],
    extras_require={
        "development": [
            "pytest",
            "pipreqs"
        ],
    },
    entry_points={
        "console_scripts": [
            "package = src.__main__:run",
        ],
    },
)
