[![PyTest](https://github.com/oliv10/ShortURL/actions/workflows/pytest.yml/badge.svg?branch=main)](https://github.com/oliv10/ShortURL/actions/workflows/pytest.yml)

# ShortURL

A simple webpage using FastAPI and Redis to create a short URL to forward to another site.

Inspired by [this](https://realpython.com/build-a-python-url-shortener-with-fastapi/). But not followed in the slightest.

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
  python3 -m pip install .
```

Start the server

```bash
  shorturl
```


## Running Tests

To run tests, run the following command in the shorturl directory

```bash
  python3 install .[development]
  pytest
```

