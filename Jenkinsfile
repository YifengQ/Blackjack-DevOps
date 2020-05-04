pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Unit Testing') {
            steps {
                sh 'python BlackJack_UnitTests.py'
            }
        }

    }
}