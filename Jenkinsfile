node {
    def app

    stage('Checkout') {
        checkout scm
    }

    stage('Build') {

        app = docker.build("yifengqin/devops")
    }

    stage('Unit Testing') {
      steps {
        sh 'python BlackJack_UnitTests.py'
      }
    }

    stage('Integration Testing') {
      steps {
        sh 'python BlackJack_IntegrationTest.py'
      }
    }
}