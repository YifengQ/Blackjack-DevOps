node {
    def app

    stage('Checkout') {
        checkout scm
    }

    stage('Build') {

        app = docker.build("yifengqin/devops")
    }

    stage('Unit Testing') {
      app.inside {
        sh 'python BlackJack_UnitTests.py'
      }
    }

    stage('Integration Testing') {
      app.inside {
        sh 'python BlackJack_IntegrationTest.py'
      }
    }
}