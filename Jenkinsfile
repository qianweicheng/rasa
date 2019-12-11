pipeline {
   agent {
       docker 'hub.edisonpark.net/edisonchat/rasa:latest' 
   }

   stages {
      stage('Prepare Env') {
         steps {
           sh '''
                python -m edo_pro.rasasc_jeff -h
           '''
         }
      }
      stage('Training') {
        steps {
            sh """
                ls -al
                pwd
                python --version
                which python
                which pip
                # python -m edo_pro.rasasc_jeff -t
            """
        }
      }  
   }
}