pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/muckalo/agrcic-jenkins-1'
            }
        }
        stage('Set Python Path') {
            steps {
                sh 'export PATH=$PATH:/usr/local/bin'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }
    }
}
