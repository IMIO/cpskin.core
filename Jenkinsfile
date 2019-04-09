pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                cache(maxCacheSize: 850,
                      caches: [[$class: 'ArbitraryFileCache', excludes: '', path: '${WORKSPACE}/eggs']]){
                    sh 'virtualenv-2.7 .'
                    sh 'bin/pip install -r requirements.txt'
                    sh 'bin/buildout code-analysis:jenkins=True'
                }
                stash 'workspace'
            }
        }
        stage('Test') {
            steps {
                unstash 'workspace'
                sh '/etc/init.d/xvfb start 2> /dev/null &'
                sh 'bin/test --all'
            }
        }
        stage('Coverage') {
            steps {
                unstash 'workspace'
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
    post{
        cleanup{
            deleteDir()
        }
    }
}
