import json
import os
import random

from PIL import Image
from flask import Flask, render_template, request

app = Flask(__name__)

FORM_DATA = {'surname': 'Watny', 'name': 'Mark', 'edu': 'Выше среднего', 'prof': 'штурман марсохода',
             'gender': 'male', 'motiv': 'Всегда мечтал застрять на Марсе!', 'ready': 'True'}
PROFESSIONS = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач',
                   'инженер по терраформированию', 'климатолог',
                   'специалист по радиационной защите', 'астрогеолог', 'гляциолог',
                   'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода', 'киберинженер',
                   'штурман', 'пилот дронов']
NUM = 4
IMAGES = {'img': ['static/img/pez2.png', 'static/img/pez3.png']}


@app.route('/<title>')
@app.route('/index/<title>')
def base(title):
    params = {'title': title}
    return render_template('base.html', **params)


@app.route('/training/<prof>')
def training(prof):
    if 'инженер' in prof or 'строитель' in prof:
        prof = 'True'
    else:
        prof = 'False'
    params = {'prof': prof}
    return render_template('training.html', **params)


@app.route('/list_prof/<list>')
def list_prof(list):
    params = {'list': list, 'profs': PROFESSIONS}
    return render_template('list_prof.html', **params)


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def show_form():
    global FORM_DATA
    if request.method == 'GET':
        return render_template('form.html')
    elif request.method == 'POST':
        FORM_DATA["surname"] = request.form['surname']
        FORM_DATA["name"] = request.form['name']
        #FORM_DATA["email"] = request.form['email']
        FORM_DATA["edu"] = request.form['class']
        profs = []
        for i in range(1, 16):
            try:
                a = request.form[f'prof{i}']
                profs.append(a)
            except Exception:
                pass
        FORM_DATA["prof"] = profs
        FORM_DATA["gender"] = request.form['sex']
        FORM_DATA["motiv"] = request.form['about']
        FORM_DATA["ready"] = request.form['accept']
        print(FORM_DATA)
        return "Форма отправлена"


@app.route('/answer')
@app.route('/auto_answer')
def show_answer():
    params = FORM_DATA
    if isinstance(params['prof'], list):
        params['prof'] = ', '.join(params['prof'])
    return render_template('auto_answer.html', **params)


@app.route('/table_param/<gender>/<int:age>')
def show_rooms(gender, age):
    params = {'gender': gender, 'age': age}
    return render_template('rooms.html', **params)


@app.route('/member')
def show_member():
    a = random.choice(["1", "2", "3", "4", "5", "6"])
    with open('templates/json.json', 'r', encoding='utf-8') as file:
        file = json.load(file)
    params = file[a]
    print(params)
    return render_template('cards.html', **params)


@app.route('/galery', methods=['POST', 'GET'])
def show_gallery():
    global IMAGES, NUM
    if request.method == 'GET':
        params = IMAGES
        print(IMAGES)
        return render_template('gallery.html', **params)

    elif request.method == 'POST':
        filename = request.form['file']
        pth = 'C:\\'
        for root, dirnames, filenames in os.walk(pth):
            for file in filenames:
                if file == filename:
                    path = os.path.join(root, file)
        image = Image.open(path)
        image.save(f'static/img/pez{NUM}.jpg')
        IMAGES['img'].append(f'static/img/pez{NUM}.jpg')
        NUM += 1
        return "Картинка отправлена"


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")