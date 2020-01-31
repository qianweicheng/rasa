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
                // git credentialsId: 'rsa_github', url: 'git@github.com:qianweicheng/rasa.git'
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
                    python -m edo_pro.rasasc_jeff -h
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
                        docker build -t hub.edisonpark.net/edisonchat/rasa -f ./deploy/Dockerfile .
                        docker push hub.edisonpark.net/edisonchat/rasa
                    '''
                }
            }
        }
        stage('Deploy to K8S') {
            agent { 
                docker {
                    image 'hub.edisonpark.net/edisonchat/deploy-helper:latest'
                    args '-v /var/jenkins_home/workspace/rack:/rack'
                }
            }
            steps {
                sh '''
                    # workingspack is rasa1
                    # make stag as default
                    # kubectl --kubeconfig /root/kube_config_stag get pod
                    mkdir /root/.kube
                    cp /root/kube_config_stag /root/.kube/config
                    cd ../rack/deploy2
                    ./deploy-tool.py -f -h
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