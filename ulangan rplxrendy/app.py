from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Ganti dengan kunci rahasia yang kuat

# Halaman Beranda
@app.route('/')
def home():
    return render_template('home.html')

# Halaman Katalog Produk
@app.route('/catalog')
def catalog():
    products = [
        {'id': 1, 'name': 'Produk 1', 'description': 'Deskripsi Produk 1'},
        {'id': 2, 'name': 'Produk 2', 'description': 'Deskripsi Produk 2'},
        # Tambahkan produk lainnya
    ]
    return render_template('catalog.html', products=products)

# Detail Produk
@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = {'id': product_id, 'name': f'Produk {product_id}', 'description': f'Deskripsi Produk {product_id}'}
    return render_template('product_detail.html', product=product)

# Halaman Checkout
@app.route('/checkout')
def checkout():
    if 'username' not in session:
        return redirect(url_for('login'))  # Arahkan ke halaman login jika belum login
    return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ")  # Ganti dengan nomor WhatsApp Anda

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('home'))
    return render_template('login.html')

# Logout
@app.route('/logout')
def logout():
    session.pop('username', None)  # Menghapus username dari session
    return render_template('logout.html')  # Mengarahkan ke halaman logout

if __name__ == '__main__':
    app.run(debug=True)