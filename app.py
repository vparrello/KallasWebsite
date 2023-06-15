from flask import Flask, render_template, request, redirect
import smtplib

OWN_EMAIL = 'parrellovictoria@gmail.com'
OWN_PASSWORD = 'ozbatjeqsfdootld'
app = Flask(__name__)

@app.route('/successful', methods=["POST", "GET"])
def send_email():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']
    if request.method == 'POST':
        price_packages = request.form.getlist('pricing_package')
        packages = ''
        for package in price_packages:
            packages += package + ", "
    email_message = f"Subject: Test Message From website\n\nName: {name}\nEmail: {email}\nPhone Number: {phone}\n Pricing Packages:{packages}\n {message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)
    return render_template('successful.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Services')
def services():
    return render_template('services.html')

@app.route('/About')
def about():
    return render_template('about.html')

@app.route('/Resume')
def resume():
    return render_template('resume.html')

@app.route('/Portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/Pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/Contact', methods=["POST", "GET"])
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(host='localhost', debug=True)