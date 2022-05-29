from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user)

  

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route("/contact.html")
def contact():
    return render_template('contact.html')

@views.route("/about.html")
def about():
    return render_template('about.html')

@views.route("/services.html")
def services():
    return render_template('services.html')  
    
@views.route("/create.html") 
def create():
    
    return render_template('create.html') 

@views.route("/Audi_viz.html")
def audi():
    return render_template('/Audi_viz.html')      

@views.route("/Audi_viz.html")
def b():
    return render_template('/Audi_viz.html')

@views.route("/BMW_viz.html")
def c():
    return render_template('/BMW_viz.html')

@views.route("/Infiniti_viz.html")
def d():
    return render_template('/Infiniti_viz.html')

@views.route("/Lexus_viz.html")
def e():
    return render_template('/Lexus_viz.html')

@views.route("/mercedes_viz.html")
def f():
    return render_template('/mercedes_viz.html')    

@views.route("/LdaModel_All_brands_viz.html")
def g():
    return render_template('/LdaModel_All_brands_viz.html')
