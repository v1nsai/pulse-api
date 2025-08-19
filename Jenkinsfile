pipeline {
  agent {
    kubernetes {
      yaml '''
      apiVersion: v1
      kind: Pod
      metadata:
        labels:
          app: jenkins-kaniko
      spec:
        serviceAccountName: jenkins
        securityContext:
          fsGroup: 1000
          fsGroupChangePolicy: OnRootMismatch
        containers:
        - name: kaniko
          image: gcr.io/kaniko-project/executor:v1.23.2-debug
          command: ["/busybox/sh","-c","while true; do sleep 3600; done"]
          tty: true
          env:
            - name: DJANGO_SECRET_KEY
              valueFrom:
                secretKeyRef:
                  name: django-secret
                  key: DJANGO_SECRET_KEY
          securityContext:
            runAsUser: 0
            allowPrivilegeEscalation: true
          volumeMounts:
          - name: docker-config
            mountPath: /kaniko/.docker/
        - name: kubectl
          image: bitnami/kubectl:1.29
          command: ["/bin/sh","-c","while true; do sleep 3600; done"]
          tty: true
          securityContext:
            runAsUser: 0
            runAsGroup: 1000
            allowPrivilegeEscalation: true
        - name: git
          image: alpine/git:2.45.2
          command: ["/bin/sh","-c","while true; do sleep 3600; done"]
          tty: true
          securityContext:
            runAsUser: 1000
            runAsGroup: 1000
            allowPrivilegeEscalation: false
        volumes:
        - name: docker-config
          secret:
            secretName: harbor-docker-config
          '''
    }
  }

  options {
    timestamps()
    ansiColor('xterm')
  }

  environment {
    REGISTRY   = 'harbor.internal'
    PROJECT    = 'library'
    IMAGE_NAME = 'pulse-api'
    NAMESPACE  = 'pulse'
    KANIKO_TLS = '--insecure --skip-tls-verify --skip-tls-verify-registry=harbor.internal'
  }

  stages {
    stage('Checkout') {
      steps {
        container('git') {
          checkout scm
          sh 'git --version && echo WORKSPACE=$WORKSPACE && test -f Dockerfile && ls -la'
        }
      }
    }

    stage('Build & Push Image') {
      environment {
        SHORT_SHA = "${env.GIT_COMMIT.take(7)}"
        TAG       = "${env.BRANCH_NAME}-${SHORT_SHA}"
      }
      steps {
        container('kaniko') {
          sh """
            /kaniko/executor \
              --context ${WORKSPACE} \
              --dockerfile ${WORKSPACE}/Dockerfile \
              --destination ${REGISTRY}/${PROJECT}/${IMAGE_NAME}:${TAG} \
              --destination ${REGISTRY}/${PROJECT}/${IMAGE_NAME}:latest-${BRANCH_NAME} \
              ${KANIKO_TLS}
          """
        }
      }
    }

    stage('Deploy to K8s') {
      environment {
        SHORT_SHA = "${env.GIT_COMMIT.take(7)}"
        TAG       = "${env.BRANCH_NAME}-${SHORT_SHA}"
        FULL_IMG  = "${REGISTRY}/${PROJECT}/${IMAGE_NAME}:${TAG}"
        DEPLOY    = "${IMAGE_NAME}"
      }
      steps {
        container('kubectl') {
          sh '''
            set -eu pipefail
            sed "s|REPLACE_IMAGE|${FULL_IMG}|g" jenkins/deploy/deployment.template.yaml > jenkins/deploy/deployment.yaml
            kubectl apply -k ./jenkins/deploy
            kubectl -n ${NAMESPACE} rollout status deploy/${DEPLOY} --timeout=5m
            kubectl -n ${NAMESPACE} get deploy ${DEPLOY} -o wide
          '''
        }
      }
    }
  }

  post {
    always {
      echo "BRANCH=${env.BRANCH_NAME} SHA=${env.GIT_COMMIT}"
    }
    failure {
      echo "Build failed on ${env.BRANCH_NAME}@${env.GIT_COMMIT}"
    }
  }
}
