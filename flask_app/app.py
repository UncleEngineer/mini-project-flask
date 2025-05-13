from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps


app = Flask(__name__)
app.secret_key = 'loongwissawakorn'  # สำหรับ flash messages

# SQLite Database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contact.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Contact model
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)

# สร้างฐานข้อมูล (รันครั้งเดียว)
with app.app_context():
    db.create_all()





# Admin table
class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# สร้าง superuser default ถ้ายังไม่มี
with app.app_context():
    db.create_all()
    if not Admin.query.filter_by(username='admin').first():
        superuser = Admin(username='admin')
        superuser.set_password('rankaikhongloong')
        db.session.add(superuser)
        db.session.commit()



# localhost:8000
# 210.155.77.100
# www.loongshop.com

@app.route('/')
def home():
    name = 'Uncle Engineer'
    context = {'nm':name}
    friend = ['somchai','somsak','somsri']

    return render_template('index.html',context=context, friend=friend)

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        new_contact = Contact(name=name, email=email, subject=subject, message=message)
        db.session.add(new_contact)
        db.session.commit()
        flash('ส่งข้อความเรียบร้อยแล้ว!', 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html')


@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        admin = Admin.query.filter_by(username=username).first()
        if admin and admin.check_password(password):
            session['admin_logged_in'] = True
            return redirect(url_for('admin_dashboard'))
        else:
            flash('ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง', 'danger')
    return render_template('admin_login.html')



def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('admin_logged_in'):
            return redirect(url_for('admin_login'))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/admin/dashboard')
@login_required
def admin_dashboard():
    contacts = Contact.query.all()
    return render_template('admin_dashboard.html', contacts=contacts)


@app.route('/admin/add', methods=['GET', 'POST'])
@login_required
def add_admin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if Admin.query.filter_by(username=username).first():
            flash('มีผู้ใช้นี้อยู่แล้ว', 'warning')
        else:
            new_admin = Admin(username=username)
            new_admin.set_password(password)
            db.session.add(new_admin)
            db.session.commit()
            flash('เพิ่มผู้ดูแลระบบสำเร็จ', 'success')
            return redirect(url_for('add_admin'))
    return render_template('add_admin.html')

@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_logged_in', None)
    flash('คุณได้ออกจากระบบแล้ว', 'info')
    return redirect(url_for('admin_login'))


if __name__ == '__main__':
    app.run(debug=True)