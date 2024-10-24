from flask import Flask, send_file, request, render_template, jsonify  # type: ignore
from flask_mail import Mail, Message

app = Flask(__name__)

# Configuration for email server
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'your-email-password'  # Replace with your email password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

# Create email instance
mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/download-pdf')
def download_pdf():
    file_path = 'results.pdf'
    return send_file(file_path, as_attachment=True, download_name='results.pdf')


@app.route('/send_message', methods=['POST'])
def send_message():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # Create message object
    msg = Message(subject="Message from Contact Form",
                  sender=email,
                  recipients=['christtech81@gmail.com'])  # Replace with your email
    msg.body = message
    mail.send(msg)

    # Print the details to console
    print(f"Name: {name}, Email: {email}, Message: {message}")

    # Send response back to the client
    return jsonify({"status": "success", "message": "Message sent!"})

# alvj ewhd vlqx shf


if __name__ == '__main__':
    app.run(debug=True)
