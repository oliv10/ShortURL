FROM python:3.13-bullseye



COPY ./shorturl /shorturl

COPY ./setup.py /

RUN python3 -m pip install .

ENTRYPOINT shorturl --host 0.0.0.0 --port 80