from flask import Flask
from flask_mail import Mail,Message
app=Flask(__name__)
mail=Mail(app)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='kumar99484@gmail.com'
app.config['MAIL_PASSWORD']='9948435657'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
mail=Mail(app)
@app.route('/mail')
def mail():
    msg=Message('Hello',sender='kumar99484@gmail.com',recipients=['kumar99484@gmail.com'])
    msg.body='i am fine.How are you?'
    mail.send(msg)
    return "mail sent successfully"
if __name__=='__main__':
    app.run()