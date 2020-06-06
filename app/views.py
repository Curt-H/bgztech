from flask import render_template, redirect, url_for
from flask import Blueprint as bp

main = bp('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/happy')
def happy():
    return "Happy!"

@main.route('/articles')
def articles():
    return redirect(url_for('.index'))

@main.route('/activities')
def activities():
    return redirect(url_for('.index'))

@main.route('/lab')
def lab():
    return redirect(url_for('.index'))


