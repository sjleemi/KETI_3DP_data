from flask import Flask, render_template, request, abort
from utils.data_parsing import load_layer_data, load_detail_data  

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            layer_num = int(request.form.get('layer'))
        except (ValueError, TypeError):
            return " 올바른 숫자를 입력해주세요.", 400

        try:
            result = load_layer_data(layer_num)
        except Exception as e:
            return f" 데이터 처리 중 에러: {e}", 500

        return render_template("index.html", **result)

    return render_template("index.html")


@app.route('/details/<path:layer_key>')
def detail(layer_key):
    try:
        detail_data = load_detail_data(layer_key)
    except Exception as e:
        abort(500, description=str(e))

    return render_template("details.html", **detail_data)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
