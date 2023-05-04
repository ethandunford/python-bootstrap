clear

ip=$(ip -o route get to 8.8.8.8 | sed -n 's/.*src \([0-9.]\+\).*/\1/p')


docker stop python-network || true
docker stop python-network || true
docker network create -d bridge python-network || true

docker stop python-pytest
docker rm python-pytest

set -e

DOCKER_BUILDKIT=1 docker build -t python-pytest-pytest -f Dockerfile.pytest .

docker run --name=python-pytest \
    -v "$(pwd)/app":/root \
    --network=python-network \
    -e CONTEXT="dev" \
    -e API_URL="http://$ip:5000" \
    -it python-pytest-pytest /bin/bash