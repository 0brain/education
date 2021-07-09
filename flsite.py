'''1) З бібліотеки flask імпортуємо клас Flask
   8) З бібліотеки flask імпортуємо функцію render_template, яка приймає ім’я шаблону
   і список змінних аргументів шаблону, а повертає готовий шаблон з заміненими аргументами
'''
from flask import Flask, render_template, url_for, request, flash, session, redirect, abort

app = Flask(__name__) # 2) У випадку імпорту __name__ - буде ім’ям поточного файлу
app.config['SECRET_KEY'] = "kihihngfcj6751jg"

menu = [{"name": "Встановлення", "url": "install-flask"},
        {"name": "Перша програма", "url": "first-app"},
        {"name": "Зворотній зв’язок", "url": "contact"}]  # 13) Створюємо список menu

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


@app.route("/contact", methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash("Повідомлення відправлено", category="success")
        else:
            flash("Виникла помилка відправлення", category="error")
    return render_template("contact.html", title="Зворотній зв’язок", menu=menu)


@app.route("/profile/<username>")
def profile(username):
    if "userLogged" not in session or session["userLogged"] != username:  #щоб користувач або незалогінений користувач випадково не зміг зайти в чужий профіль
        abort(401)  #доступ до сторінки заборонено
    return f"Профіль користувача: {username}"


@app.route("/login", methods=['POST', 'GET'])  #декоратор прив’язаний до адресу /login по якому можна приймати пост і ґет запити
def login():
    if "userLogged" in session: #якщо userLogged існує в нашій сесії
        return redirect(url_for("profile", username=session["userLogged"]))  #то ми робимо переадресацію на відповідний профайл з тим username, який знаходиться в сесії
    elif request.method == "POST" and request.form["username"] == "Admin" and request.form["psw"] == "admin":  #інакше ми беремо дані з форми, і якщо вони співпадають з таким "Admin" юзернеймом і таким "admin" паролем
        session["userLogged"] = request.form["username"]  # то ми зберігаємо дані в сесії
        return redirect(url_for("profile", username=session["userLogged"]))   # і знову робимо переадресацію на відповідний профайл з тим username, який знаходиться в сесії
    return render_template("login.html", title="Авторизація", menu=menu)  # а інакше просто буде відображена форма Авторизація



@app.errorhandler(404)
def pageNotFound(error):
    return render_template("page404.html", title="Сторінку не знайдено", menu=menu)  # 10) в функцію render_template крім назви шаблону передаємо параметр title


'''3) У випадку самостійного запуску __name__ - буде мати значення __main__;
      if __name__ == '__main__' - є умовою, що локальний сервер запуститься тільки
      при безпосередньому запуску з Python,  а не при імпортуванні як модуль 
'''
if __name__ == "__main__":
    '''4) Для запуску локального сервера використовуємо функцію run()'''
    '''5) debug=True - щоб ми в браузері бачили всі помилки, які виникатимуть під час розробки сайту'''
    app.run(debug=True)
