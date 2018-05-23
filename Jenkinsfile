pipeline {
    agent {
        docker {
            image 'docker-staging.imio.be/iasmartweb/test:110'
            args '-v /etc/group:/etc/group:ro -v /etc/passwd:/etc/passwd:ro -v /var/lib/jenkins:/var/lib/jenkins'
        }
    }
    triggers {
        pollSCM('*/3 * * * *')
    }
    stages {
        stage('Build') {
            steps {
                sh 'virtualenv -p python2.7 .'
                sh 'bin/pip install -r requirements.txt'
                sh 'bin/buildout code-analysis:jenkins=True'
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
                warnings canComputeNew: false, canResolveRelativePaths: false, parserConfigurations: [[parserName: 'Pep8', pattern: '**/parts/code-analysis/flake8.log']]
                sh 'bin/createcoverage'
                sh 'bin/coverage xml'
                cobertura coberturaReportFile: '**/coverage.xml', conditionalCoverageTargets: '70, 0, 0', lineCoverageTargets: '80, 0, 0', maxNumberOfBuilds: 0, methodCoverageTargets: '80, 0, 0', onlyStable: false, sourceEncoding: 'ASCII'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
