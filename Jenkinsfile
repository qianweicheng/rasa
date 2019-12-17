pipeline {
    agent none
    options {
        timeout(time: 1, unit: 'HOURS') 
    }
    stages {
        stage('Prepare Env') {
            agent {
                docker 'hub.edisonpark.net/edisonchat/rasa:tools' 
            }
            steps {
                sh '''
                    pwd
                    python --version
                    which python
                    which pip
                '''
            }
        }
        stage('Training') {
            agent {
                docker 'hub.edisonpark.net/edisonchat/rasa:tools' 
            }
            steps {
                sh """
                    python -m edo_pro.rasasc_jeff -t


                """
            }
        }
        stage('Build The Image') {
            agent { 
                docker {
                    image 'docker' 
                    args '-v /var/run/docker.sock:/var/run/docker.sock'
                }
            }
            environment {
                EDISON_DOCKER_HUB = credentials('hub.edisonpark.net')
            }
            steps {
                withDockerRegistry(credentialsId: 'hub.edisonpark.net', url: 'https://hub.edisonpark.net/') {
                    sh '''
                        docker ps
                        docker build -t hub.edisonpark.net/edisonchat/rasa -f ./deploy/Dockerfile .
                        docker push hub.edisonpark.net/edisonchat/rasa
                    '''
                }
            }
        }
        stage('Deploy to K8S') {
            agent { 
                docker 'hub.edisonpark.net/edisonchat/deploy-helper:latest' 
            }
            steps {
                sh '''
                    # workingspack is rasa1
                    kubectl --kubeconfig /root/kube_config_stag get pod
                '''
            }
        } 
   }
   post { 
        always {
            echo 'I will always say Hello again!'
        }
        success {
            echo 'Weicheng!'
        }
    }
}