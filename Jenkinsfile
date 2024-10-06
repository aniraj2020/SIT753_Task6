pipeline {
    agent any
    environment {
        // Access AWS credentials from Jenkins credentials store
        AWS_ACCESS_KEY_ID = credentials('aws-credentials')
        AWS_SECRET_ACCESS_KEY = credentials('aws-credentials')
        // Add the path to the EB CLI
        PATH = "/Users/ani/Library/Python/3.12/bin:$PATH"
    }
    stages {
        // Step 1: Build Stage
        stage('Build') {
            steps {
                // Use the correct path for pip
                sh '/Library/Frameworks/Python.framework/Versions/3.12/bin/pip install -r requirements.txt'
            }
        }

        // Step 2: Test Stage
        stage('Test') {
            steps {
                sh '/opt/anaconda3/bin/python test_model.py'
            }
        }

        // Step 3: Code Quality Analysis Stage
        stage('Code Quality Analysis') {
            steps {
                withSonarQubeEnv('SonarCloud') {
                    withCredentials([string(credentialsId: 'b6392e5a-dde5-4913-9f63-3ba988f1601b', variable: 'SONAR_TOKEN')]) {
                        sh '/opt/homebrew/bin/sonar-scanner -Dsonar.projectKey=aniraj2020_SIT753_Task6 -Dsonar.organization=aniraj2020 -Dsonar.login=$SONAR_TOKEN'
                    }
                }
            }
        }

        // Step 4: Deploy to AWS Elastic Beanstalk
        stage('Deploy to AWS Elastic Beanstalk') {
            steps {
                script {
                    // AWS EB CLI commands to deploy the model
                    sh '''
                    /Library/Frameworks/Python.framework/Versions/3.12/bin/pip install awsebcli --upgrade --user
                    export PATH=/Users/ani/Library/Python/3.12/bin:$PATH
                    
                    # Initialize Elastic Beanstalk for deployment (only needed once)
                    eb init -p python-3.8 sit753-hd-app --region us-east-1
                    
                    # Create a new environment (only needed for first-time deployment)
                    eb create sit753-hd-app-env --region us-east-1

                    # Deploy the application
                    eb deploy
                    '''
                }
            }
        }

        // Step 5: Monitor AWS Elastic Beanstalk
        stage('Monitor & Alert') {
            steps {
                script {
                    // Monitor the health of the application using CloudWatch
                    sh '''
                    aws cloudwatch describe-alarms --region us-east-1
                    '''
                }
            }
        }

        // Final Stage: Echo Message
        stage('Final Stage') {
            steps {
                echo 'Model training, testing, and deployment complete.'
            }
        }
    }

    // Post-build actions
    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check logs for more details.'
        }
    }
}
