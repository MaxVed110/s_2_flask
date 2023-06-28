from flask import Flask, render_template, make_response, request

app = Flask(__name__, static_folder='homework_s_10')


@app.route('/')
def index():
    return render_template('index.html')


# Создать страницу, на которой будет форма для ввода числа и кнопка "Отправить".
# При нажатии на кнопку будет произведено перенаправление на страницу с результатом,
# где будет выведено введенное число и его квадрат.
@app.route('/multiply/', methods=['GET', 'POST'])
def multiply():
    if request.method == 'POST':
        number = int(request.form.get('number'))
        content = {
            'number': number,
            'number_mul': number ** 2
        }
        return render_template('result.html', **content)
    return render_template('multiply.html')


# Создать страницу, на которой будет форма для ввода имени и электронной почты, при отправке которой будет
# создан cookie-файл с данными пользователя, а также будет произведено перенаправление на страницу приветствия,
# где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка «Выйти», при нажатии на которую будет удалён cookie-файл с данными
# пользователя и произведено перенаправление на страницу ввода имени и электронной почты.
@app.route('/registration/', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        content = {
            'name': name
        }
        response = make_response(render_template('main_list.html',
                                                 **content))
        response.headers['new_head'] = 'New value'
        response.set_cookie('username', content['name'])
        response.set_cookie('email', email)
        return response
    return render_template('registration.html')


@app.route('/registration_out/')
def reg_out():
    response = make_response(render_template('registration.html'))
    response.delete_cookie('username')
    response.delete_cookie('email')
    return response


if __name__ == '__main__':
    app.run(debug=True)
