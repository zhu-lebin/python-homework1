from flask import Flask, render_template, url_for, redirect, flash
from flask_bootstrap import Bootstrap
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length
from cid import wdcloud
import base64
# https://bootstrap-flask.readthedocs.io/en/latest/
#引入表单类，继承LoginForm，
class WdcloudForm(FlaskForm):
    bv = StringField(label='BV', validators=[DataRequired(), Length(1, 30)])
    #password = StringField(label='Password', validators=[DataRequired(), Length(4, 10)])
    #remember = BooleanField(label='Remember me')
    submit = SubmitField(label='submit')

class SForm(FlaskForm):
    bv = StringField(label='BV', validators=[DataRequired(), Length(1, 30)])
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello-flask'   # RuntimeError: A secret key is required to use CSRF.
bootstrap = Bootstrap(app=app)  # 初始化bootstrap

bv = None


@app.route('/login_success')
def success():
    #   wdcloud是在cid中定义的类，其中方法makeph可以生成词云图并将其保存到静态文件夹
    #   success.html用于显示生成的词云图
    wd = wdcloud(bv)
    wd.makeph()


    return render_template('success.html')


@app.route('/', methods=['GET', 'POST'])
def index():
    #   使用定义的form类
    form = WdcloudForm()
    if form.validate_on_submit():
        #   得到bv值，也可以放到success里
        global bv
        bv = form.bv.data
        #   重定向为GET请求
        return redirect((url_for('success')))
    return render_template('index.html', form=form)
app.run()

