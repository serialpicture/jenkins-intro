# 🧪 Exercise 8: Generate and Archive CSV Output

**Goal:** Use Jenkins to run a script that creates a CSV file and archives it.

**Instructions:**
1. Add `scripts/generate_csv.py` to your workspace.
2. Create a new Pipeline job.
3. Use this pipeline:
   ```groovy
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
   ```
4. Run and check for `output.csv` in artifacts.
