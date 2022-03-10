from flask import Flask, request, make_response, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandex_lyceum_secret_key'


def main():
    app.run(port=8080, host='127.0.0.1')


@app.route('/cookie_test')
def cookie_test():
    visit_count = int(request.cookies.get("visit_count", 0))
    if visit_count:
        res = make_response(f"Вы пришли на эту страницу "
                            f"{visit_count + 1} "
                            f"раз")
        res.set_cookie("visit_count", str(visit_count + 1),
                       max_age=60 * 60 * 24 * 365 * 2)
    else:
        res = make_response(f"Вы пришли на эту страницу "
                            f"первый "
                            f"раз за последние 2 года")
        res.set_cookie("visit_count", "1",
                       max_age=60 * 60 * 24 * 365 * 2)

    return res


@app.route('/session_test')
def session_test():
    visit_count = session.get("visit_count", 1)
    session['visit_count'] = visit_count + 1
    session.permanent = True
    if session["visit_count"] > 9:
        session.pop("visit_count", None)
    return f'Вы пришли на эту страницу {visit_count} раз'


if __name__ == "__main__":
    main()