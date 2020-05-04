pipeline {
  agent { docker { image 'python:3.8' } }
  stages {
    stage('Building') {
      steps {
        sh 'python Dealer.py'
        sh 'python Deck.py'
        sh 'python Player.py'
        sh 'python Table.py'
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