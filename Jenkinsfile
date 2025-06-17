pipeline {
       agent any
       stages {
           stage('Generate CSV') {
               steps {
                   sh 'python3 scripts/generate_csv.py'
               }
           }
           stage('Archive') {
               steps {
                   archiveArtifacts artifacts: 'output.csv'
               }
           }
       }
   }