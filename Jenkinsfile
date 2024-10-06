pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                // Install dependencies
                sh '/Library/Frameworks/Python.framework/Versions/3.12/bin/pip install -r requirements.txt'
                // Train the model and save the pickle file
                sh '/opt/anaconda3/bin/python train_model.py'
            }
        }
        stage('Test') {
            steps {
                // Run the tests after training
                sh '/opt/anaconda3/bin/python test_model.py'
            }
        }
        stage('Deploy') {
            steps {
                // Optionally, deploy or perform other actions here
                echo "Model training and testing complete."
            }
        }
    }
}
