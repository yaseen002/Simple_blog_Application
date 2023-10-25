from flask import Flask, render_template
import requests

app = Flask(__name__)
response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
all_blogs = response.json()


@app.route('/')
def home():
    return render_template('index.html', blogs=all_blogs)


@app.route('/post/<blog_id>')
def get_post(blog_id):
    blog = int(blog_id)
    return render_template('post.html', get_blog=blog, blogs=all_blogs)


if __name__ == "__main__":
    app.run(debug=True)
