# deployment-skeleton-fastapi
В этом репозитории я собираю хорошие практики развертывания и создания веб приложения написанного на python с фреймворком fastapi. Это пример одного микросервиса.

Его можно развертывать с помощью docker-compose. Для этого создайте в корне проекта файл .env с системными переменными которые хотите доставить в контейнер. Есть несколько обязательных для работы этого приложения, например:

DEBAG=true

POSTGRES_USER=postgres

POSTGRES_PASSWORD=postgres

POSTGRES_DB=postgres

POSTGRES_HOST=db

POSTGRES_PORT=5432

Можете указать другие значения для всех кроме POSTGRES_HOST

Затем запустите команду: docker-compose up --build
