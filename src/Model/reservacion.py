from flask import Blueprint, request, jsonify, json
from common.Toke import *
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template 
from sqlalchemy import text


class RolesUsuarios(db.Model):
    __tablename__ = "tblrolesusuario"

    ReservacionID = db.Column(db.Integer, primary_key=True, autoincrement=False)
    ClienteID = db.Column(db.Integer)
    FechaInicio = db.Column(db.DateTime)
    FechaFin = db.Column(db.DateTime)
    Estado = db.Column(db.String(100))

with app.app_context():
    db.create_all()

class RolesSchema(ma.Schema):
    class Meta:
        fields = ('ReservacionID','roles')