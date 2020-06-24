# -*- coding: utf-8 -*-

from __future__ import with_statement
from flask import Flask, request, session, url_for, redirect, \
     render_template, abort, g, flash

a = None
b = None
c = None
cal = None

app = Flask(__name__)


@app.route('/')
def jinja2():
    return render_template('main.html')

@app.route('/note1')
def note1():
    return render_template('note1.html')

@app.route('/note2')
def note2():
    return render_template('note2.html')

@app.route('/note3')
def note3():
    return render_template('note3.html')

@app.route('/sessions')
def sessions():
    """calculator"""
    global a
    global b
    global c
    global cal

    if a is not None and b is not None:
        if cal=='+':
            c = str(float(a) + float(b))
        elif cal == '-':
            c = str(float(a) - float(b))
        elif cal == '*':
            c = str(float(a) * float(b))
        elif cal == '/':
            c = str(float(a) / float(b))
        else:
            cal = None
    return render_template('sessions.html', num=a ,num2=b, num3=c, cal=cal)


@app.route('/calculate2',methods=['POST'])
def calculate2():
    global a
    global b
    global cal

    if 'plus' in request.form:
        cal = '+'
    elif 'minus' in request.form:
        cal = '-'
    elif 'pro' in request.form:
        cal = '*'
    elif 'div' in request.form:
        cal = '/'
    else:
        cal = None

    if request.method == 'POST':
        if request.form['num']!='' and request.form['num2']!='':
            a = request.form['num']
            b = request.form['num2']
            return redirect(url_for('sessions'))
        else:
            a = request.form['num']
            b = request.form['num2']
            if a =='':
                if b =='':
                    a = None
                    b = None
                else:
                    a = None
            else:
                b = None
            return redirect(url_for('sessions'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)