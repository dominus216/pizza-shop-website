from flask import *

app = Flask(__name__)

@app.route("/")
def main_page():
    """
    тестовая функция для обработки корневого маршрута
    :return:
    """
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)