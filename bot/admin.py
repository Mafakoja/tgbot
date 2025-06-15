from flask import Flask, render_template_string, request, redirect, url_for
from .database import SessionLocal, init_db
from .models import Message
from .config import settings

app = Flask(__name__)
init_db()

LOGIN_FORM = """
<form method='post'>
  <input type='password' name='password' placeholder='Password'/>
  <input type='submit' value='Login'/>
</form>
"""


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form.get('password') == settings.admin_password:
            return redirect(url_for('messages'))
    return render_template_string(LOGIN_FORM)


@app.route('/messages')
def messages():
    session = SessionLocal()
    msgs = session.query(Message).order_by(Message.timestamp.desc()).all()
    session.close()
    html = "<h1>Messages</h1><ul>"
    for m in msgs:
        html += f"<li>({m.timestamp}) {m.user_id} [{m.message_type}] - {m.content}</li>"
    html += "</ul>"
    return html


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
