node {
    stage('Build & Test') {
        checkout scm
        sh "docker build . -t aaronmwilliams/python-selenium-testing"
        sh "docker-compose up --exit-code-from tests"
    }
}