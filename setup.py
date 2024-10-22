from setuptools import setup, find_packages

setup(
    name='ShortURL',
    version='0.1.0',
    url='https://github.com/oliv10/ShortURL',
    author='Oliver Scotten',
    author_email='',
    description='Simple Webpage using FastAPI and Redis to create a short URL to forward to another site.',
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=[
        "uvicorn~=0.29.0",
        "fastapi~=0.115.3",
        "redis~=5.0.2",
        "pydantic_settings~=2.2.1"
    ],
    extras_require={
        "development": [
            "pytest",
            "pipreqs",
            "fakeredis",
            "httpx"
        ],
    },
    entry_points={
        "console_scripts": [
            "shurl = shorturl.__main__:run",
            "shorturl = shorturl.__main__:run",
        ],
    },
)
