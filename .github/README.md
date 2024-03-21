[![PyTest](https://github.com/oliv10/ShortURL/actions/workflows/pytest.yml/badge.svg?branch=main)](https://github.com/oliv10/ShortURL/actions/workflows/pytest.yml)

# ShortURL

A simple webpage using FastAPI and Redis to create a short URL to forward to another site.

Inspired by [this](https://realpython.com/build-a-python-url-shortener-with-fastapi/). But not followed in the slightest.

## Environment Variables

To run this project outside of Docker, you will need to add the following environment variables to your .env file. These are the defaults when running in Docker and the developemnt environment (assuming you are using vscode devcontainers).

```
DBHOST: str = "redis"
DBPORT: int = 6379
DBUSER: str | None = None
DBPASS: str | None = None
KEYLEN: int = 8
```
**_Note_**: This is not proper formatting for a .env file, this is just to show the datatypes the program is expecting, what the default values are, and which ones are optional (marked as _None_).

## Deployment

To deploy ShortURL using Docker run

```bash
curl -O https://raw.githubusercontent.com/oliv10/ShortURL/main/compose.yml
docker compose up -d
```


## Run Locally

Clone the project

```bash
  git clone https://github.com/oliv10/ShortURL.git
```

Go to the project directory

```bash
  cd ShortURL
```

Install dependencies

```bash
  python3 install .
```

Start the server

```bash
  shorturl
```


## Running Tests

To run tests, run the following commands in the shorturl directory

```bash
  python3 install .[development]
  pytest
```

