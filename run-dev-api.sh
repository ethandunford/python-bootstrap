clear

sudo rm -rf app/__pycache__/

docker stop python-network || true
docker stop python-network || true
docker network create -d bridge python-network || true

docker stop python-api
docker rm python-api

set -e

DOCKER_BUILDKIT=1 docker build -t python-api-dev-image -f Dockerfile.api .

docker run --name=python-api \
    -v "$(pwd)/app":/root \
    --network=python-network \
    -e FLASK_ENV=development \
    -e CONTEXT="dev" \
    -e DB="dbname='pythondb' user='pythondb' password='password' host='db'" \
    -e DEBUG=1 \
    -p 5000:5000 \
    -it python-api-dev-image /bin/bash