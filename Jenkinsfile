pipeline {
  agent { docker { image 'python:3.8' } }
  stages {
    stage('Building') {
      steps {
        sh 'python -m py_compile Blackjack.py'
        sh 'python -m py_compile Dealer.py'
        sh 'python -m py_compile Deck.py'
        sh 'python -m py_compile Player.py'
        sh 'python -m py_compile Table.py'
      }
    }
    stage('Unit Testing') {
      steps {
        sh 'python BlackJack_UnitTests.py'
      }
      post {
        always {
          junit 'UnitTestReports/*.xml'
        }
      }
    }
    stage('Integration Testing') {
      steps {
        sh 'python BlackJack_IntegrationTest.py'
      }
    }
  }
}