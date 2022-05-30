from flask import (Flask, render_template,
                   url_for, request)
from flask_qrcode import QRcode

application = Flask(__name__)
qrcode = QRcode(application)


@application.route('/')
def index():
    return render_template('index.html')


@application.route('/qr', methods=["GET", 'POST'])
def qr():
    if request.form:
        return render_template('qr.html')
    return render_template('index.html')


if __name__ == '__main__':
    application.run()
