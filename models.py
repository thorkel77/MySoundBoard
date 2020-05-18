from flask import Flask, redirect, url_for, render_template, request, session, flash, jsonify
from flask_sqlalchemy import SQLAlchemy





app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:""@localhost/mysoundboard"
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Chansons (db.Model):
    _tablename__ = 'chansons'

    id_chans = db.Column(db.Integer, primary_key=True)
    type =db.Column(db.String(255))
    durée = db.Column(db.Integer)
    date_sortie = db.Column(db.Date)
    nom_chans = db.Column(db.String(255))
    id_grp = db.Column('id_grp', db.Integer, db.ForeignKey('Groupes.id_group'))

    def __init__(self, type, durée, date_sortie, nom_chans, id_grp):
        self.type = type
        self.durée = durée
        self.date_sortie = date_sortie
        self.nom_chans = nom_chans
        self.id_grp = id_grp





class Groupes (db.Model):
    __tablename__ = 'groupes'

    id_group = db.Column(db.Integer, primary_key=True)
    nom_grp = db.Column(db.String(255))
    nb_album = db.Column(db.Integer)
    nb_musique = db.Column(db.Integer)
    nom_chanteur = db.Column(db.String(20))
    id_chans =  db.Column('id_chans', db.Integer, db.ForeignKey('Chansons.id_chans'))

    def __init__(self, nom_grp, nb_album, nb_musique, nb_chanteur, id_chans):
        self.nom_grp
        self.nb_album
        self.nb_musique
        self.nb_chanteur
        self.id_chans

class Users (db.Model):
    __tablename__ = 'users'

    id_user = db.Column (db.Integer, primary_key=True)
    nom = db.Column (db.String(255))
    prenom = db.Column (db.String(255))
    email = db.Column (db.String(255))
    telephone = db.Column(db.Integer)
    password = db.Column (db.String(15))
    username = db.Column(db.String(15))


    def __init__(self, nom, prenom, email, telephone, password, username):
        self.nom
        self.prenom
        self.email
        self.telephone
        self.password
        self.username




class Recherches(db.Model):
    __tablename__ = 'recherches'


    id_recherche = db.Column(db.Integer, primary_key=True)
    id_grp = db.Column('id_grp', db.Integer, db.ForeignKey('Groupes.id_group'))
    id_chans = db.Column('id_chans', db.Integer, db.ForeignKey('Chansons.id_chans'))

    def __init__(self, ig_grp, id_chans):
        self.id_grp
        self.id_chans





class Maplaylists (db.Model):
    __tablename__ = 'maplaylists'

    id_playlist = db.Column(db.Integer, primary_key=True)
    id_chans = db.Column('id_chans', db.Integer, db.ForeignKey('chansons.id_chans'))
    id_user = db.Column('id_user', db.Integer, db.ForeignKey('Users.id_user'))



    def __init__(self, id_chans, id_user):
        self.id_chans
        self.id_user




if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)