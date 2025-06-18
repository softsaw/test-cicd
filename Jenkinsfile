pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps { checkout scm }
    }
    stage('Build') {
      steps { sh "docker build -t softsaw/test-cicd:${GIT_COMMIT[0..6]} ." }
    }
    stage('Login & Push') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USR', passwordVariable: 'PSW')]) {
          sh '''
            echo $PSW | docker login -u $USR --password-stdin
            docker push softsaw/test-cicd:${GIT_COMMIT[0..6]}
            docker tag softsaw/test-cicd:${GIT_COMMIT[0..6]} softsaw/test-cicd:latest
            docker push softsaw/test-cicd:latest
          '''
        }
      }
    }
  }
}