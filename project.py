from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Большие буковки</h1> <h6>Маленькие буковки</h6>' \
           '<table><table border=#><tr><td>ячейка 1</td><td>ячейка 2</td></tr></table>'
#комментарий 2
@app.route('/privet')
def greeting():
    return '<h2>Здравствуй, друг</h2>'

@app.route('/button')
def click():
    return '<button name="button">Тык!</button>'

@app.route('/form')
def survey():
    return '<label for="city">Введите город:</label>' \
           '<input list="city-list" id="city" name="city"> <datalist id="city-list">' \
           '<option value="Москва"><option value="Рига"></datalist>'

@app.route('/picture')
def show_pic():
    return '<figure>' \
           '<img src="https://htmlbase.ru/storage/app/media/travel.jpg" alt=""></img>' \
           '<figcaption>Путешествие по миру</figcaption></figure>'

if __name__ == "__main__":
    app.run(debug=True)