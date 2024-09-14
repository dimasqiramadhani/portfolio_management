from app import create_app

# buat instance aplikasi flask
app = create_app()

if __name__ == '__main__':
    # jalankan aplikasi flask
    app.run(debug=True)