from flask import Flask
from views import views

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")


if __name__ == '__main__':
    app.run(debug=True) 

#one dayyyyyy ill know what thissss meannnnssssssss
#you will rel ill make sure of it