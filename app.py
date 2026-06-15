from flask import Flask, request, render_template
from math import sqrt
from datetime import datetime

app = Flask('my_distance')

distances = list()


@app.route('/', methods=['GET', 'POST'])
def distance_form():
    if request.method == 'GET':
        return render_template('index.html', result=None)
    if request.method == 'POST':
        start_point = tuple(map(lambda x: int(x), request.form['apoint'].split(',')[0:2]))
        end_point = tuple(map(lambda y: int(y), request.form['bpoint'].split(',')[0:2]))
        result_tmp = sqrt((end_point[1] - start_point[1])**2 + (end_point[0] - start_point[0])**2)
        result = {
            'requested_at': datetime.now(),
            'result_distance': result_tmp,
            'start_point': start_point,
            'end_point': end_point
        }
        distances.append(result)
        return render_template('index.html', result=result)


@app.route('/api')
def index():
    return {}


@app.route('/api/distances')
def get_distances():
    result = list(map(lambda x: {
        'requested_at': x['requested_at'],
        'result_distance': x['result_distance'],
        'start_point': x['start_point'],
        'end_point': x['end_point']
    }, distances))
    return result


@app.route('/api/distance', methods=['POST'])
def calculate():
    start_point = tuple(map(lambda y: int(y), request.json['start_point'].split(',')[0:2]))
    end_point = tuple(map(lambda x: int(x), request.json['end_point'].split(',')[0:2]))
    result_tmp = sqrt((end_point[1] - start_point[1])**2 + (end_point[0] - start_point[0])**2)
    result = {
        'requested_at': datetime.now(),
        'result_distance': result_tmp,
        'start_point': start_point,
        'end_point': end_point
    }
    return result


if __name__ == '__main__':
    app.run(debug=True)