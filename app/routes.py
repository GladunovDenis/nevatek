from app import app
from flask import render_template
from app.settings import *

contacts.update(dict(sitename=sitename))

@app.route('/')
@app.route('/index')
def index_page():
    title = 'Главная'
    context = dict(
        id = 'index',
        title=f'{sitename} - {title}', 
        heading = title
        )
    context.update(contacts)
    return render_template('index.html', **context)


@app.route('/about')
def about_page():
    title = 'О компании'
    context = dict(
        id = 'about',
        title=f'{sitename} - {title}',
        heading = title
        )
    context.update(contacts)
    return render_template('about.html', **context)


@app.route('/services')
def services_page():
    title = 'Услуги'
    context = dict(
        id = 'services',
        title=f'{sitename} - {title}', 
        heading = title)
    context.update(contacts)
    return render_template('services.html', **context)
    
    
@app.route('/services/legal')
def legal_page():
    
    title = 'Юридические услуги'
    context = dict(
        id = 'legal',
        title=f'{sitename} - {title}', 
        heading = title)
    context.update(contacts)
    return render_template('legal.html', **context)
    
    
@app.route('/services/accounting')
def accounting_page():
    
    title = 'Бухгалтерские'
    context = dict(
        id = 'accounting',
        title=f'{sitename} - {title}', 
        heading = title)
    context.update(contacts)
    return render_template('accounting.html', **context)


@app.route('/services/price')
def price_page():
    title = 'Стоимость услуг'
    context = dict(
        id = 'price',
        title=f'{sitename} - {title}', 
        heading = title)
    context.update(contacts)
    return render_template('price.html', **context)


@app.route('/contacts')
def contact_page():
    title = 'Контакты'
    context = dict(
        id = 'contacts',
        title=f'{sitename} - {title}', 
        heading = title)
    context.update(contacts)
    return render_template('contacts.html', **context)