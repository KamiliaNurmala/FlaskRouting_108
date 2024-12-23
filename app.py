from flask import Flask, redirect, url_for, request, render_template

# Membuat instance aplikasi Flask
app = Flask(__name__)

# Route untuk halaman utama
@app.route('/')
def home():
    # Menampilkan file HTML (index.html) yang berada di folder templates
    return render_template('index.html')  

# Route untuk halaman sukses, menerima parameter 'name' dari URL
@app.route('/success/<name>')
def success(name):
    # Mengembalikan pesan selamat datang dengan nama yang diterima
    return f'Welcome {name}!'

# Route untuk login, menangani metode POST dan GET
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':  
        # Jika metode POST, ambil nilai input dari form (name="nm")
        user = request.form['nm']
        # Redirect ke route 'success' dengan parameter nama
        return redirect(url_for('success', name=user))
    else:  
        # Jika metode GET atau tidak ada data, redirect kembali ke form login
        return redirect(url_for('home'))

# Menjalankan aplikasi pada mode debug (untuk pengembangan)
if __name__ == '__main__':
    app.run(debug=True)
