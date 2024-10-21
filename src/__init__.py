from flask import Flask 

app = Flask(__name__)


@app.route('/hotels')
@app.route('/')
def get_hotels():
    hotel_ratings = [
        {'id': 1, 'name': 'Maple Tree', 'rating': 4},
        {'id': 2, 'name': 'Regents', 'rating': 5},
        {'id': 3, 'name': 'DropInn', 'rating': 3}
    ]
    rows = ''
    for hotel in hotel_ratings:
        rows += '<tr><td>' + hotel.get('name') + '</td></tr>'
        #rows += f'<tr><td>{hotel.get('id')}</td><td>{hotel.get('name')}</td><td>{hotel.get('rating')}</td></tr>'
        
    #return f'<html><body><table><tr><th>Name</th></tr>{rows}</table></body></html>'
    return '<html><body><table border = 1>' + rows + '</table></body></html>'



if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=8080, debug=True)
    app.run(debug=True)