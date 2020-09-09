from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort


from .db import get_db

bp = Blueprint('views', __name__)


@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, Name,Block,UnitNo,MaintenanceFee,Due'
        ' FROM income p'
         
    ).fetchall()
    return render_template('index.html', posts=posts)

@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        Name = request.form['Name']
        Block = request.form['Block']
        UnitNo = request.form['UnitNo']
        MaintenanceFee = request.form['MaintenanceFee']
        Due = request.form['Due']
        error = None

        if not Name:
            error = 'Name is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO income (Name,Block,UnitNo,MaintenanceFee,Due)'
                ' VALUES (?, ?, ?, ?, ?)',
                (Name,Block,UnitNo,MaintenanceFee,Due)
                
            )
            db.commit()
            return redirect(url_for('views.index'))

    return render_template('create.html')    


@bp.route('/payment/<int:income_id>', methods=('GET', 'POST'))
def payment(income_id):
    if request.method == 'POST':
        amount = request.form['amount']
        error = None

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO Payment (income_id,amount)'
                ' VALUES (?, ?)',
                (income_id, amount)
            )
            db.commit()
            return redirect(url_for('views.index'))
    else: 

        db = get_db()
        due = db.execute(
            'SELECT Due'
            ' FROM income p WHERE p.id == income_id'
            ).fetchall()

    return render_template('payment.html', due=due)   