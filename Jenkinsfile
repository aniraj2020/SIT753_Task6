pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh '/Library/Frameworks/Python.framework/Versions/3.12/bin/pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh '/opt/anaconda3/bin/python test_model.py'
            }
        }
        stage('Deploy') {
            steps {
                sh '/opt/anaconda3/bin/python train_model.py'
            }
        }
    }
}
