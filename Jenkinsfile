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
        stage('Code Quality Analysis') {
            steps {
                withSonarQubeEnv('SonarCloud') {
                    sh 'sonar-scanner -Dsonar.projectKey=aniraj2020_SIT753_Task6 -Dsonar.organization=aniraj2020 -Dsonar.login=71e7f4891be40e7df01e1a514eff68a75525dcb3'
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Model training and testing complete.'
            }
        }
    }
}
