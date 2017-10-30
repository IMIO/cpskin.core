pipeline {
    agent {
        docker {
            image 'docker-staging.imio.be/cpskin.test:latest'
        }
    }
    triggers {
        pollSCM('*/3 * * * *')
    }
    stages {
        stage('INIT') {
            steps {
                deleteDir()
                sh 'echo `whoami`'
                sh 'echo `pwd`'
                sh 'echo ls -lah'
                sh 'sleep 1000'
            }
        }
        stage('Build') {
            steps {
                sh 'python bootstrap.py'
                sh 'bin/buildout buildout:download-cache=/.buildout/buildout-cache/downloads buildout:eggs-directory=/.buildout/buildout-cache/eggs'
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
