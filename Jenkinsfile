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
        stage('Code Quality Analysis') {
            steps {
                withSonarQubeEnv('SonarCloud') {
                    withCredentials([string(credentialsId: 'sonarcloud_token', variable: 'SONAR_TOKEN')]) {
                        sh '/opt/homebrew/bin/sonar-scanner -Dsonar.projectKey=aniraj2020_SIT753_Task6 -Dsonar.organization=aniraj2020 -Dsonar.login=$SONAR_TOKEN'
                    }
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
