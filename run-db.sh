docker stop pythondb
docker rm pythondb

docker network create -d bridge python-network || true

DOCKER_BUILDKIT=1 docker build -t pythondb -f Dockerfile.pg .

docker stop pythondb && docker rm pythondb

docker run -d \
--rm \
--name db \
--network=python-network \
-e POSTGRES_PASSWORD=password \
-e POSTGRES_USER=pythondb \
-e POSTGRES_DATABASE=pythondb \
-p 5555:5432 python-db
