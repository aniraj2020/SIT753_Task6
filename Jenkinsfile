pipeline {
    agent any
    environment {
        AWS_ACCESS_KEY_ID = credentials('aws-credentials')
        AWS_SECRET_ACCESS_KEY = credentials('aws-credentials')
        PATH = "/opt/anaconda3/bin:$PATH"
    }
    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
                sh 'git checkout main'  // Ensure you are on the main branch
            }
        }

        stage('Build') {
            steps {
                // Use Anaconda Python to install dependencies
                sh '/opt/anaconda3/bin/python -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                // Use Anaconda Python to run tests
                sh '/opt/anaconda3/bin/python test_model.py'
            }
        }

        stage('Code Quality Analysis') {
            steps {
                withSonarQubeEnv('SonarCloud') {
                    withCredentials([string(credentialsId: 'b6392e5a-dde5-4913-9f63-3ba988f1601b', variable: 'SONAR_TOKEN')]) {
                        sh '/opt/homebrew/bin/sonar-scanner -Dsonar.projectKey=aniraj2020_SIT753_Task6 -Dsonar.organization=aniraj2020 -Dsonar.login=$SONAR_TOKEN'
                    }
                }
            }
        }

        stage('Deploy to AWS Elastic Beanstalk') {
            steps {
                script {
                    sh '''
                    # Install EB CLI using Anaconda Python
                    /opt/anaconda3/bin/python -m pip install awsebcli --upgrade --user
                    export PATH=/Users/ani/Library/Python/3.12/bin:$PATH
                    
                    # Deploy the application to the existing environment
                    eb deploy sit753-hd-app-env --region us-east-1
                    '''
                }
            }
        }

        stage('Monitor & Alert') {
            when {
                expression {
                    currentBuild.result == null || currentBuild.result == 'SUCCESS'
                }
            }
            steps {
                script {
                    sh 'aws cloudwatch describe-alarms --region us-east-1'
                }
            }
        }

        stage('Final Stage') {
            when {
                expression {
                    currentBuild.result == null || currentBuild.result == 'SUCCESS'
                }
            }
            steps {
                echo 'Model training, testing, and deployment complete.'
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check logs for more details.'
        }
    }
}
