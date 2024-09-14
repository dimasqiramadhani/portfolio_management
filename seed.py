from app import create_app, db
from app.models import Project

app = create_app()

with app.app_context():
    db.create_all()  # Membuat semua tabel di database

    # Menghapus data lama jika ada
    Project.query.delete()
    
    # Menambahkan data dummy
    project1 = Project(title='Project Alpha', description='A sample project description', technology='Python, Flask', link='http://example.com')
    project2 = Project(title='Project Beta', description='Another sample project description', technology='JavaScript, React', link='http://example.com')
    
    db.session.add_all([project1, project2])
    db.session.commit()

    print('Database telah diinisialisasi dengan data dummy.')
