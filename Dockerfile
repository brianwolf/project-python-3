# ---------------------------------------------
# COMPILER
# ---------------------------------------------
FROM python:3.10-slim as compiler

WORKDIR /home
COPY app.py .
COPY logic ./logic

RUN pip install compile --upgrade pip

RUN	python -m compile -b -f -o dist/ .
RUN	rm -fr dist/env/


# ---------------------------------------------
# RUNNER
# ---------------------------------------------
FROM python:3.10-slim

WORKDIR /home/dist

ARG ARG_VERSION=local

ENV VERSION=${ARG_VERSION}
ENV PYTHON_HOST=0.0.0.0
ENV PYTHON_PORT=5000
ENV WORKERS=1
ENV TZ America/Argentina/Buenos_Aires

COPY requirements.txt ./
RUN pip install -r requirements.txt --upgrade pip
RUN rm -fr requirements.txt

COPY --from=compiler /home/dist/ .
COPY logic/resources logic/resources

CMD uvicorn \
    --host ${PYTHON_HOST} \
    --port ${PYTHON_PORT} \
    --workers=${WORKERS} \
    app:app