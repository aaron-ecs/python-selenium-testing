# python-selenium-testing
An example Selenium framework written in Python using Behave for BDD.

## Setup
It's recommended you run a Python Virtual Environment in Python 3.7.2 or higher.

If you want to run the tests locally in your environment please run `pip install behave` & `pip install selenium`

Please have your Selenium Grid running. You may find the easyest way to do this by running Zalenium (https://opensource.zalando.com/zalenium/) and amend the remote driver URL in `google.step.py`.

## Testing
To save you from having to install Python and the dependencies you can run the tests by building the docker image
run `docker build . -t aaronmwilliams/python-selenium-testing` in the project root then `docker-compose up` this will also spin up a Zalenium docker container.

## Project
**environment.py**: the driver is built and added to the context. Setup and teardown of the driver is done for each test.

If you want to run the tests locally please amend the remote webdriver URL. Execute all tests by running the following command: `behave`

## Reporting
The default Behave test result gets generated in `plain.output` file.

If you run the tests with argument `--junit` an jUnit XML report will be generated in `./reports/`

## Linting
Please ensure you have the `pylint` plugin installed and running on your IDE.

## Jenkins
If the Jenkins file is used it will build the docker image and then run `docker-compose up --exit-code-from tests` which kicks off the tests.

## To-Do
- Add more tests and abstract general selenium logic and waits
- Add to TravisCI