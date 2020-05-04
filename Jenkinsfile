pipeline {
  agent { docker { image 'python:3.8' } }
  stages {
    stage('build') {
      steps {
        echo 'Building'
      }
    }
    stage('test') {
      steps {
        sh 'python BlackJack_UnitTests.py'
      }
      post {
        always {
          junit 'test-reports/*.xml'
        }
      }
    }
  }
}