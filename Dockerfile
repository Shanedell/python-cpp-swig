FROM python:3.7-slim

WORKDIR /app

COPY . ./

RUN pip install pipenv && \
  apt-get update && \
  apt-get install -y --no-install-recommends \
    g++ \
    python3-dev \
    git \
    libssl-dev \
    swig && \
  pipenv install --dev

CMD [ "./gen_lib" ]
