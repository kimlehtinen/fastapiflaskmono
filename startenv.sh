
# source fastapitest/bin/activate

docker compose down
sudo chmod -R 777 /home/kle/projects/fastapitest/db
docker compose up -d --build
