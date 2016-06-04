from flask import Flask, render_template
app = Flask(__name__)

#import từ thư viện Mongo DB
import mongoengine
from mongoengine import Document, StringField
host = "ds011893.mlab.com"
port = 11893
db_name = "c4e_rss"
user_name = "c4e"
password = "codethechange"
mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

class Movie(Document): #để báo cho Python là mình lấy dữ liệu từ Document của Mongo DB
    title = StringField() #Mongo sẽ tự tìm những field có trùng tên ở trên DB và mục này của Python
    img = StringField()

# #Để update dữ liệu lên Mongo DB:
# m = Movie(
#     title = "Tom & Jerry",
#     img = "https://upload.wikimedia.org/wikipedia/en/5/5f/TomandJerryTitleCardc.jpg"
# )
# m.save()

# #Lập ra movie_list
# class Movie:
#     def __init__(self, title, img):
#         self.title = title
#         self.img = img
#
# movie1 = Movie("Tom & Jerry", "https://upload.wikimedia.org/wikipedia/en/5/5f/TomandJerryTitleCardc.jpg")
# movie2 = Movie("Harry Potter", "http://static.independent.co.uk/s3fs-public/styles/article_large/public/thumbnails/image/2013/09/12/17/potter.jpg")
# movie_list = [
#     movie1,
#     movie2,
#     Movie("50 Shades of Grey", "http://cdn04.cdn.justjared.com/wp-content/uploads/headlines/2015/04/fifty-shades-of-grey-writer.jpg")
#     ]

@app.route('/')
def index():
    return render_template("index.html", m_list = Movie.objects)

@app.route('/<name>')
def hello(name):
    return 'Hello ' + name

#Dữ liệu nằm tại file HTML:
@app.route('/movie_1')
def get_movie():
    return render_template('movie_1.html')

#Dữ liệu nằm tại file Lập trình Web Session:
@app.route('/movie_2')
def get_movie_2():
    return render_template(
        'movie_2.html',
        title = 'CIVIL WAR',
        img="http://lovelace-media.imgix.net/uploads/1143/9a4331d0-041a-0134-e757-0a315da82319.jpg?")

#Cách bật với dữ liệu list, nằm tại file lập trình Web Session:
@app.route('/movies')
def movies():
    return render_template('movies.html', movies = movie_list)







if __name__ == '__main__':
    app.run()
