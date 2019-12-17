pipeline {
   agent none
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
            steps {
                sh '''
                    docker ps
                    docker build -t hub.edisonpark.net/edisonchat/rasa:latest ./deploy/Dockerfile
                    docker push hub.edisonpark.net/edisonchat/rasa:latest
                '''
            }
        }
        stage('Deploy to K8S') {
            agent { 
                docker 'hub.edisonpark.net/edisonchat/deploy-helper:latest' 
            }
            steps {
                sh 'kubectl --kubeconfig ./kube_config_stag get pod'
            }
        } 
   }
   post { 
        always {
            agent any
            echo 'I will always say Hello again!'
        }
        success {
            steps {
                agent any
                echo 'Weicheng!'
            }
        }
    }
}