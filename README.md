Это Flask приложение, которое предоставляет доступ к двум моделям машинного обучения через Docker контейнеры.

Описание
Данное приложение предоставляет доступ к двум моделям машинного обучения:
### YOLO (You Only Look Once)
### DETR (DEtection TRansformer)
Модели упакованы в Docker контейнеры для удобного развёртывания и масштабирования.

Установка и запуск
Для запуска приложения локально выполните следующие шаги:
1.Клонировать репозиторий:
<br>`git clone https://github.com/your-username/flask-ml.git`</br>
`cd flask-ml`
2.Собрать Docker контейнер:
<br>`docker build -t flask-ml .`</br>
3.Запустить Docker контейнер:
<br>`docker run -d -p 5000:5000 flask-ml`</br>
Приложение Flask будет доступно по адресу http://localhost:5000
Использование
После запуска приложения вы можете взаимодействовать с ним с помощью веб интерфейса.
Docker Конфигурация
Docker контейнер собирается из Dockerfile, который определяет конфигурацию приложения и включает в себя установку Flask и других необходимых зависимостей.

Вклад в проект
Вы можете вносить свой вклад в проект! Просто создайте форк репозитория и отправьте pull request с вашими изменениями.
