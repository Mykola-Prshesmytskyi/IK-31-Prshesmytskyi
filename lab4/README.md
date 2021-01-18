
##1. Ознайомився з Docker,Створюю Dockerfile
##2. Створив репозиторій Docker Hub - mykolaprshesmytskyi/lab4/
##3. Виконав команду "sudo docker run -it --name=django --rm -p 8000:8000 mykolaprshesmytskyi/lab4:django"
##4. Створив Dockerfile.site та виконав команди імеджа:
sudo docker build -t mykolaprshesmytskyi/lab4:monitoring . --file Dockerfile.site
sudo docker push mykolaprshesmytskyi/lab4:monitoring
sudo docker images
##6. Щоб отримати логи виконав команди:
sudo docker run -it --name=django --rm -p 8000:8000 mykolaprshesmytskyi/lab4:django
sudo docker run -it --rm --net=host -v $(pwd)/server.log:/app/server.log mykolaprshesmytskyi/lab4:monitoring
