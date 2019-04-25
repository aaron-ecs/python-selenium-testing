# python-selenium-testing
An example Selenium framework written in Python using Behave for BDD.

## Setup
It's recommended you run a Python Virtual Environment in Python 3.7.2 or higher.

If you want to run the tests locally in your environment please run `pip install behave` & `pip install selenium`

Please have your Selenium Grid running. You may find the easyest way to do this by running Zalenium (https://opensource.zalando.com/zalenium/) and amend the remote driver URL in `google.step.py`.

## Testing
To save you from having to install Python and the dependencies you can run the tests by building the docker image
run `docker build . -t aaronmwilliams/python-selenium-testing` in the project root then `docker-compose up` this will also spin up a Zalenium docker container.

Or if you want to run the tests locally run the following command: `behave`


## Project
**environment.py**: the driver is built and added to the context. Setup and teardown of the driver is done for each test.

Please note the default URL is `http://localhost:4444/wd/hub`. You can override this by running behave command with the following option: `-D ENV_URL="your-new-url.com"`. Please note you may also need to change this aswell in the docker files.

## Reporting
The default Behave test result gets generated in `plain.output` file.

If you run the tests with argument `--junit` an jUnit XML report will be generated in `./reports/`

## Linting
Please ensure you have the `pylint` plugin installed and running on your IDE.

## Jenkins
If the Jenkins file is used it will build the docker image and then run `docker-compose up --exit-code-from tests` which kicks off the tests.

## Behave Hints and Trips
**Invoke Further Steps**
You can invoke steps from within steps. For example you can call the below code with: `context.execute_steps('''when I want to invoke another step''')`
```
@when('I want to invoke another step')
def do_magic_things(context):
    context.driver.get("http://www.google.co.uk")
```

**Tagging**
You can tag scenarios in the feature files and just run the scenarios tagged tests with this command: `behave --tags=regressions` or you can exclude them: `behave --tags=-slow`


## To-Do
- Add more tests and abstract general selenium logic and waits
- Add to TravisCI