pipeline {
    agent {
        docker {
            image 'docker-staging.imio.be/cpskin.test:latest'
            args '-v /etc/group:/etc/group:ro -v /etc/passwd:/etc/passwd:ro -v /var/lib/jenkins:/var/lib/jenkins'
        }
    }
    triggers {
        pollSCM('*/3 * * * *')
    }
    stages {
        stage('Build') {
            steps {
                sh 'python bootstrap.py buildout:download-cache=/.buildout/buildout-cache/downloads buildout:eggs-directory=/.buildout/buildout-cache/eggs --buildout-version=2.7.0'
                sh 'bin/buildout buildout:download-cache=/.buildout/buildout-cache/downloads buildout:eggs-directory=/.buildout/buildout-cache/eggs code-analysis:jenkins=True'
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
