pipeline {
    agent {
        docker {
            image 'docker-staging.imio.be/cpskin.test:latest'
            args '-v /etc/group:/etc/group:ro -v /etc/passwd:/etc/passwd:ro -v /var/lib/jenkins:/var/lib/jenkins -e PLONE_CSRF_DISABLED=True'
        }
    }
    triggers {
        pollSCM('*/3 * * * *')
    }
    stages {
        stage('Build') {
            steps {
                sh 'python bootstrap.py buildout:download-cache=/.buildout/buildout-cache/downloads buildout:eggs-directory=/.buildout/buildout-cache/eggs'
                sh 'bin/buildout buildout:download-cache=/.buildout/buildout-cache/downloads buildout:eggs-directory=/.buildout/buildout-cache/eggs'
            }
        }
        stage('Test') {
            steps {
                sh '/etc/init.d/xvfb start 2> /dev/null &'
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
