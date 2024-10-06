pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'python test_model.py'
            }
        }
        stage('Deploy') {
            steps {
                sh 'python train_model.py'
            }
        }
    }
}
