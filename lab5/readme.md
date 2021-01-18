
##  1. Прочитав все, про "docker-compose" та "Flask".
##  2. Створив папку "my_app" і папку "tests".
##  3. Перевірив працездатність за допомогою команд 
"pipenv --python 3.7", "pipenv install -r requirements.txt", "pipenv run python app.py".
##  4. Виникли помилки.Усунув їх за допомогою установки та запуску redis-server та створенням папки logs
##  5. Провів тести за допомогою команди "pipenv run pytest test_app.py --url http://localhost:5000" всі вони пройшли успішно.
##  6. Перевірив роботу сайту та перейшов на всі його сторінки.
##  7. Очистив середовище, створив файли "Dockerfile.app" та "Dockerfile.tests", а також "Makefile" для автоматизації процесу.

    REPO - змінна для зберігання назви Docker репозиторію
    PHONY - дозволяє оголошувати фальшиві цілі
    STATES - змінна для зберігання директив
    run - директива для створення мережі
    test-app - директива для запуску контейнера з моніторингом
    docker-prune - видалення контейнерів, волюмів, мереж i імеджів
    $(STATES) - директива для білда самого контейнера
    docker-delete - директива для видалення імелжів
##  9. Завантажив імеджі до Docker Hub репозиторію
##  10. Переходжу до Docker-compose, перевірив чи встановлений "Docker-compose" та запустив його за допомогою команди "docker-compose -p lab5 up"
##  11. Веб-сайт працює, адреса для переходу на сайт - http:/0.0.0.0/ Скрішоти сторінок сайту:
![image alt](https://github.com/Mykola-Prshesmytskyi/IK-31-Prshesmytskyi/blob/main/lab5/screenshot_1.jpg?raw=true)
![image alt](https://github.com/Mykola-Prshesmytskyi/IK-31-Prshesmytskyi/blob/main/lab5/screenshot_2.jpg?raw=true)
![image alt](https://github.com/Mykola-Prshesmytskyi/IK-31-Prshesmytskyi/blob/main/lab5/screenshot_3.jpg?raw=true)
##  12. Компоуз створив докер імеджі, тег для цих імеджів "compose".
##  13. Запушив імеджі до Docker Hub.
##  14. На мою думку "docker-compose" кращий по декільком причинам: він легший у використанні, технологія є новішою, а також він розроблявся саме для docker-а.
##  15. Запушив імеджі.
