<h1>Flask ML Приложение</h1>

  <h2>Описание</h2>
    <p>Это Flask приложение, которое предоставляет доступ к двум моделям машинного обучения через Docker контейнеры.</p>

  <h2>Установка и запуск</h2>
    <ol>
        <li>Клонировать репозиторий:
            <pre><code>git clone https://github.com/7aaassss/flask-ml.git</code></pre>
            <pre><code>cd flask-ml</code></pre>
        </li>
        <li>Собрать Docker контейнер:
            <pre><code>docker build -t flask-ml .</code></pre>
        </li>
        <li>Запустить Docker контейнер:
            <pre><code>docker run -p 5000:5000 flask-ml</code></pre>
            <p>Приложение Flask будет доступно по адресу <a href="http://localhost:5000">http://localhost:5000</a>.</p>
        </li>
    </ol>
    <h2>Использование</h2>
    <p>После запуска приложения вы можете взаимодействовать с ним с помощью веб интерфейса</p>
    <h2>Docker Конфигурация</h2>
    <p>Docker контейнер собирается из <code>Dockerfile</code>, который определяет конфигурацию приложения и включает в себя установку Flask и других необходимых зависимостей.</p>
    <h2>Зависимости</h2>
    <ul>
        <li>Python 3.x</li>
        <li>Flask</li>
        <li>Docker</li>
    </ul>
</body>
