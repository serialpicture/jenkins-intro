# 🧪 Exercise 2: Simple Pipeline

**Goal:** Create a basic Jenkins Pipeline job to learn about stages and steps.

## Steps:
1. Create a new item named `simple-pipeline` and select **Pipeline**.
2. In the pipeline script section, enter:
   ```groovy
   pipeline {
       agent any
       stages {
           stage('Build') {
               steps {
                   echo 'Building the app...'
               }
           }
           stage('Test') {
               steps {
                   echo 'Running tests...'
               }
           }
       }
   }
   ```
3. Run the job and review each stage.

## Reflection:
- What are stages used for?
- What would happen if you removed a bracket or keyword?
