pipeline {
    agent {
        docker {
            image 'docker-staging.imio.be/cpskin.test:latest'
            args '-v /etc/group:/etc/group:ro -v /etc/passwd:/etc/passwd:ro'
        }
    }
    triggers {
        pollSCM('*/3 * * * *')
    }
    stages {
        stage('INIT') {
            steps {
                sh 'echo `whoami`'
                sh 'echo `pwd`'
                sh 'echo ls -lah'
            }
        }
        stage('Build') {
            steps {
                sh 'python bootstrap.py buildout:download-cache=/.buildout/buildout-cache/downloads buildout:eggs-directory=/.buildout/buildout-cache/eggs'
                sh 'bin/buildout buildout:download-cache=/.buildout/buildout-cache/downloads buildout:eggs-directory=/.buildout/buildout-cache/eggs'
            }
        }
        stage('Test') {
            steps {
                sh 'Xvfb :10 -ac & export DISPLAY=:10; bin/test --all'
            }
        }
        stage('Coverage') {
            steps {
                sh 'bin/code-analysis'
                sh 'bin/createcoverage'
                sh 'bin/coverage xml'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
