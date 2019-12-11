pipeline {
   agent {
       docker 'hub.edisonpark.net/edisonchat/rasa:latest' 
   }

   stages {
      stage('Prepare Env') {
         steps {
           sh """
                echo `pwd`
                python --version
                which python
                which pip
                ls
                python -m edo_pro.rasasc_jeff -h
           """
         }
      }
      stage('Training') {
        steps {
            sh """
                echo `pwd`
                python --version
                which python
                which pip
                ls
                python -m edo_pro.rasasc_jeff -t
            """
        }
      }  
   }
}