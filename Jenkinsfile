pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                // Use full pip path
                sh '/Library/Frameworks/Python.framework/Versions/3.12/bin/pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                // Use full python path
                sh '/opt/anaconda3/bin/python test_model.py'
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
