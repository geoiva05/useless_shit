from flask import Flask
from flask import request, url_for, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "Привет, Яндекс!"


@app.route('/carousel', methods=['POST', 'GET'])
def i_dont_now_why_i_do_this():
    return f'''<!doctype html>
<html lang="ru">
<head>
<title>Название потом придумаю</title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css"
integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
<link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
</head>
<body>

<div class="container text-center">
<h1>Пейзажи марса</h1>
<br>
<div id="carous1" class="carousel slide" data-ride="carousel">
<div class="carousel-inner">
<div class="carousel-item active">
<img class="d-block w-100" src="{url_for('static', filename='img/first_image.jpg')}" alt="Первое изображение">
</div>
<div class="carousel-item">
<img class="d-block w-100" src="{url_for('static', filename='img/second_image.jpg')}" alt="Второе изображение">
</div>
<div class="carousel-item">
<img class="d-block w-100" src="{url_for('static', filename='img/third_image.jpg')}" alt="Третье изображение">
</div>
</div>
<a class="carousel-control-prev" href="#carous1" role="button" data-slide="prev">
<span class="carousel-control-prev-icon" aria-hidden="true"></span>
<span class="sr-only">Предыдущий</span>
</a>
<a class="carousel-control-next" href="#carous1" role="button" data-slide="next">
<span class="carousel-control-next-icon" aria-hidden="true"></span>
<span class="sr-only">Следующий</span>
</a>
</div>

</div>



<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>

</body>
</html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
