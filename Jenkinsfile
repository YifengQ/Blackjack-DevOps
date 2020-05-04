pipeline {
  agent { docker { image 'python:3.8' } }
  stages {
    stage('Building') {
      steps {
        sh 'python Blackjack.py'
      }
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
}