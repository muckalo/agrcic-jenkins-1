pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/muckalo/agrcic-jenkins-1.git'
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
                pytest --maxfail=1 --disable-warnings
                '''
            }
        }
    }
}
