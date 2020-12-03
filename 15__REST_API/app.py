from flask import Flask,jsonify,request,abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# initialize app
app = Flask(__name__)
# setting the database URI (where the database is located)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)   # initialize sqlalchemy orm 
ma = Marshmallow(app)  # initialize the serializer 

# database Model
class Movie(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50),nullable=False)
	likes = db.Column(db.Integer,default=0)

# This schema will convert the movie object into a JSON (serialize)
class MovieSchema(ma.Schema):
	class Meta:
		fields = ['id','name','likes']

movie_schema = MovieSchema()			# for single movie objects
movies_schema = MovieSchema(many=True)  # for list of movie objects


@app.route('/movie',methods=['GET'])
def allMoviesRoute():
	movies = Movie.query.all()
	data =  movies_schema.dumps(movies)
	return jsonify(message='movies returned',data=data)


@app.route('/movie/<int:id>',methods=['GET'])
def oneMovieRoute(id):
	movie = Movie.query.get(id);
	print(id, movie)
	if movie:
		data =  movie_schema.dumps(movie)
		return jsonify(message='movie returned',data=data),200
	return jsonify(message = f'movie with id {id} does not exists!'),404


@app.route('/movie/add',methods=['POST'])
def addMovieRoute():
	movie_name = request.get_json()
	if movie_name['name']:
		name = movie_name['name']
		movie = Movie.query.filter_by(name=name).first()
		if movie:
			return jsonify(message = f"movie with name '{name}' already exists!"),409		
		else:
			new_movie = Movie(name=name)
			db.session.add(new_movie)
			db.session.commit()
			data = movie_schema.dumps(new_movie)
			return jsonify(message="movie added!",data=data) ,201
	return jsonify(message = f"invalid data"),400


@app.route('/movie/like',methods=['POST'])
def likeMovieRoute():
	movie_id = request.get_json()
	if movie_id['id']:
		movie = Movie.query.get(movie_id['id'])
		if movie:
			movie.likes += 1
			db.session.commit()
			data = movie_schema.dumps(movie)
			return jsonify(message = 'movie liked',data=data)
		return jsonify(message = f"movie with id {movie_id['id']} does not exists!"),404
	return jsonify(message = f"invalid data"),400


if __name__ == '__main__':
	app.run(debug=True)