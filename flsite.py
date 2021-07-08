'''1) З бібліотеки flask імпортуємо клас Flask
   8) З бібліотеки flask імпортуємо функцію render_template, яка приймає ім’я шаблону
   і список змінних аргументів шаблону, а повертає готовий шаблон з заміненими аргументами
'''
from flask import Flask, render_template

app = Flask(__name__) # 2) У випадку імпорту __name__ - буде ім’ям поточного файлу

menu = ["Встановлення", "Перша програма", "Зворотній зв’язок"]  # 13) Створюємо список menu

'''6) Використовуємо декоратор route(), щоб сказати Flask, який URL запустить функцію
   7) def index() - повертає повідомлення, яке буде відображено в браузері за URL адресою "/" та "index"
'''


@app.route("/index")  # коли ми будемо переходити по адресу /index, буде загружатися шаблон index.html
@app.route("/")
def index():
    '''9) підключаємо render_template в момент переходу /index, /, /about'''
    return render_template("index.html", menu=menu)  # 14) Передаємо список menu в якості параметра в функцію render_template


@app.route("/about")
def about():
    return render_template("about.html", title="Про сайт", menu=menu)  # 10) в функцію render_template крім назви шаблону передаємо параметр title




'''3) У випадку самостійного запуску __name__ - буде мати значення __main__;
      if __name__ == '__main__' - є умовою, що локальний сервер запуститься тільки
      при безпосередньому запуску з Python,  а не при імпортуванні як модуль 
'''
if __name__ == "__main__":
    '''4) Для запуску локального сервера використовуємо функцію run()'''
    '''5) debug=True - щоб ми в браузері бачили всі помилки, які виникатимуть під час розробки сайту'''
    app.run(debug=True)
