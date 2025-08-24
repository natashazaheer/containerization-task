from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Python Flask App</title>
        <style>
            body { font-family: Arial; margin: 50px; background: #f0f8ff; }
            .container { max-width: 800px; margin: 0 auto; padding: 20px; }
            .header { color: #2c3e50; text-align: center; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1 class="header">🐍 Python Flask Application</h1>
            <p>This is a Python Flask web application running on Ubuntu server!</p>
            <p><strong>Server Details:</strong></p>
            <ul>
                <li>Framework: Flask</li>
                <li>Language: Python 3</li>
                <li>Server: Gunicorn</li>
                <li>Status: ✅ Running successfully</li>
            </ul>
        </div>
    </body>
    </html>
    ''')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)