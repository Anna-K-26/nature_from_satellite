from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os
from datetime import datetime
from werkzeug.utils import secure_filename
import random

app = Flask(__name__)
app.secret_key = '123'
app.config['UPLOAD_FOLDER'] = 'static/images'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

data_file = 'data.json'

def read_data():
    if not os.path.exists(data_file):
        test_data = {
            "images": [
                {
                    "id": 1,
                    "name": "Пустыня Сахара из космоса",
                    "date": "2023-06-15",
                    "lat": 23.42,
                    "lon": 13.13,
                    "image": "/static/images/desert.jpg",
                    "tags": "песок, пустыня",
                    "desc": "Засушливая природная зона"
                },
                {
                    "id": 2,
                    "name": "Бассейн Амазонки",
                    "date": "2008-09-28",
                    "lat": -3.47,
                    "lon": -58.38,
                    "image": "/static/images/basin.jpg",
                    "tags": "вода,река,тропики",
                    "desc": "Вид на водную поверхность с прилегающими тропическими лесами"
                },
                {
                    "id": 3,
                    "name": "Андский хребет",
                    "date": "2018-05-26",
                    "lat": -32.65,
                    "lon": -70.01,
                    "image": "/static/images/mountanins.jpg",
                    "tags": "снег,горный хребет",
                    "desc": "Заснеженные вершины горного хребта"
                }
            ],
            "analyses": []
        }
        save_data(test_data)
        return test_data

    with open(data_file, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_data(data):
    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def get_next_id(data):
    if not data['images']:
        return 1
    return max(img['id'] for img in data['images']) + 1


# Маршруты
@app.route('/')
def index():
    """Главная страница"""
    data = read_data()
    total_images = len(data['images'])
    total_analyses = len(data['analyses'])
    recent = data['images'][-3:]  # последние 3

    random_image = random.choice(data['images']) if data['images'] else None

    return render_template('index.html',
                           total_images=total_images,
                           total_analyses=total_analyses,
                           recent_images=recent,
                           random_image=random_image)


@app.route('/gallery')
def gallery():
    """Галерея снимков"""
    data = read_data()

    # Простая фильтрация
    satellite = request.args.get('satellite', '')
    tag = request.args.get('tag', '')

    images = data['images']
    if satellite:
        images = [img for img in images if img['satellite'] == satellite]
    if tag:
        images = [img for img in images if tag in img['tags']]

    # Уникальные значения для фильтров
    satellites = list(set(img['satellite'] for img in data['images']))

    return render_template('gallery.html',
                           images=images,
                           satellites=satellites,
                           current_filters={'satellite': satellite, 'tag': tag})


@app.route('/analyze/<int:image_id>', methods=['GET', 'POST'])
def analyze(image_id):
    """Анализ снимка"""
    data = read_data()
    image = next((img for img in data['images'] if img['id'] == image_id), None)

    if not image:
        flash('Снимок не найден!', 'danger')
        return redirect(url_for('gallery'))

    if request.method == 'POST':
        surface = request.form.get('surface_type')
        objects = request.form.getlist('detected_objects')

        # Валидация
        errors = []
        if not surface:
            errors.append("Выберите тип поверхности!")
        if not objects:
            errors.append("Выберите хотя бы один объект!")

        if errors:
            for error in errors:
                flash(error, 'danger')
        else:
            # Сохраняем анализ
            analysis = {
                'id': len(data['analyses']) + 1,
                'image_id': image_id,
                'surface': surface,
                'objects': objects,
                'date': datetime.now().strftime('%Y-%m-%d %H:%M')
            }
            data['analyses'].append(analysis)

            # Простая проверка правильности
            correct = False
            if surface == 'forest' and 'лес' in image['tags']:
                correct = True
            elif surface == 'water' and 'вода' in image['tags']:
                correct = True
            elif surface == 'fire' and 'пожар' in image['tags']:
                correct = True

            if correct:
                flash('✅ Правильно! Отличная работа!', 'success')
            else:
                flash('❌ Попробуйте еще раз!', 'warning')

            save_data(data)
            return redirect(url_for('gallery'))

    return render_template('analyze.html', image=image)


@app.route('/compare')
def compare():
    """Сравнение снимков"""
    data = read_data()
    if len(data['images']) < 2:
        flash('Нужно минимум 2 снимка для сравнения!', 'info')
        return redirect(url_for('gallery'))

    # Берем два случайных снимка
    img1, img2 = random.sample(data['images'], 2)

    return render_template('compare.html', image1=img1, image2=img2)


@app.route('/add', methods=['GET', 'POST'])
def add_image():
    """Добавление снимка"""
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.form.get('name', '').strip()
        satellite = request.form.get('satellite')
        date = request.form.get('date')
        lat = request.form.get('lat')
        lon = request.form.get('lon')
        clouds = request.form.get('clouds')
        image_type = request.form.get('image_type')
        tags = request.form.getlist('tags')
        desc = request.form.get('desc', '')

        # Валидация
        errors = []

        if not name:
            errors.append("Название обязательно!")
        elif len(name) < 3:
            errors.append("Название должно быть минимум 3 символа!")

        if not date:
            errors.append("Укажите дату съемки!")

        try:
            lat = float(lat)
            if lat < -90 or lat > 90:
                errors.append("Широта должна быть от -90 до 90!")
        except:
            errors.append("Широта должна быть числом!")

        try:
            lon = float(lon)
            if lon < -180 or lon > 180:
                errors.append("Долгота должна быть от -180 до 180!")
        except:
            errors.append("Долгота должна быть числом!")

        try:
            clouds = float(clouds)
            if clouds < 0 or clouds > 100:
                errors.append("Облачность от 0 до 100%!")
        except:
            errors.append("Облачность должна быть числом!")

        # Обработка файла
        file = request.files.get('image')
        if not file or file.filename == '':
            errors.append("Загрузите изображение!")
        else:
            if file.content_type not in ['image/jpeg', 'image/png', 'image/gif']:
                errors.append("Можно загружать только JPG, PNG или GIF!")

        if errors:
            for error in errors:
                flash(error, 'danger')
            return render_template('add_image.html')

        # Сохраняем файл
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Сохраняем в JSON
        data = read_data()
        new_image = {
            'id': get_next_id(data),
            'name': name,
            'satellite': satellite,
            'date': date,
            'lat': lat,
            'lon': lon,
            'image': f'/static/images/{filename}',
            'clouds': clouds,
            'type': image_type,
            'tags': ','.join(tags),
            'desc': desc
        }
        data['images'].append(new_image)
        save_data(data)

        flash('✅ Снимок успешно добавлен!', 'success')
        return redirect(url_for('gallery'))

    return render_template('add_image.html')

@app.route('/delete/<int:image_id>')
def delete_image(image_id):
    """Удаление снимка"""
    data = read_data()
    data['images'] = [img for img in data['images'] if img['id'] != image_id]
    data['analyses'] = [a for a in data['analyses'] if a['image_id'] != image_id]
    save_data(data)

    flash('Снимок удален', 'info')
    return redirect(url_for('gallery'))

if __name__ == '__main__':
    app.run(debug=True)

