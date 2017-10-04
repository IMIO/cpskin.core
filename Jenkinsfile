pipeline {
    agent {
        docker {
            image 'docker-staging.imio.be/mutual-website:latest'
            args '-u imio'
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
                sh 'python bootstrap.py'
                sh 'bin/buildout -c jenkins.cfg buildout:download-cache="/home/imio/imio-website/buildout-cache/downloads" buildout:eggs-directory="/home/imio/imio-website/buildout-cache/eggs" -t 15'
            }
        }
        stage('Test') {
            steps {
                sh 'bin/test --all'
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
