pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'github.com/muckalo/agrcic-jenkins-1'
            }
        }
        stage('Set up Virtual Environment') {
            steps {
                sh '''
                python3 -m venv venv   # Create virtual environment
                . venv/bin/activate    # Activate virtual environment
                pip install -r requirements.txt  # Install dependencies
                '''
            }
        }
        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate    # Activate virtual environment
                pytest                 # Run tests
                '''
            }
        }
    }
}

