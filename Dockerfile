FROM python:3

WORKDIR /python-selenium-testing

COPY . ./

RUN pip install --upgrade pip
RUN pip install selenium
RUN pip install behave