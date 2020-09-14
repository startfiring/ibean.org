# create newest build
docker image build -t www.ibean.org:test -f ~/github/www.ibean.org/docker/Dockerfile ~/github/www.ibean.org/

# start the web site in WSL2 docker
docker run -it --rm -p 2000:80  www.ibean.org:test bash

# access from WSL2 Host server to test the web site. 
http://localhost:2000

# push the tested version to ACR 

docker tag www.ibean.org:test kangzian/www.ibean.org:latest
docker push kangzian/www.ibean.org:latest
