from flask import Blueprint, request, jsonify, json
from common.Toke import *
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template

from Model.reservacion import Reservacion, ReservacionSchema 

routes_reservacion = Blueprint("routes_reservacion", __name__)
#Roles
reservacion_schema = ReservacionSchema()
reservaciones_schema = ReservacionSchema(many=True)

@routes_reservacion.route('/indexroles', methods=['GET'] )
def indexRoles():
    
    return "Hola Mundo!!"