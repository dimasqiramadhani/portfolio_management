from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Project

main = Blueprint('main', __name__)

@main.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)

@main.route('/add_project', methods=['GET', 'POST'])
def add_project():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        technology = request.form['technology']
        link = request.form['link']

        new_project = Project(title=title, description=description, technology=technology, link=link)
        db.session.add(new_project)
        db.session.commit()

        return redirect(url_for('main.index'))

    return render_template('add_project.html')

@main.route('/edit_project/<int:id>', methods=['GET', 'POST'])
def edit_project(id):
    project = Project.query.get_or_404(id)

    if request.method == 'POST':
        project.title = request.form['title']
        project.description = request.form['description']
        project.technology = request.form['technology']
        project.link = request.form['link']

        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('edit_project.html', project=project)

@main.route('/delete_project/<int:id>')
def delete_project(id):
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()

    return redirect(url_for('main.index'))