# Example code to run a flask application with gunicorn and docker

 * This code contains 2 example application written using flask
 * One application connectes with other application and return the reverse string
 * Nginx will be running in port 80 and pointing to 2nd app reverse_app
 * Now reverse_app will communicate with main_app and then reverse the string and send it back to requestor

# Requirements to be installed
  
  Docker
  Docker-compose


# Run all 3 containers using the following command

  sudo ./run_docker.sh   (This will use docker compose file and run all togather)

# Test the request
  
  curl http://localhost/v1/api/reverse

  or

  curl http://$IP/v1/api/reverse
  
  Output:
  {"id":"1","message":"dlroW olleH"}



# Steps to Host it in Kubernities / Minikube

  kubectl create -f .
