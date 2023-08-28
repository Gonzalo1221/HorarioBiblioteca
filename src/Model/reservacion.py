from config.db import db, app, ma

class Reservacion(db.Model):
    __tablename__ = "tblreservacion"

    ReservacionID = db.Column(db.Integer, primary_key=True, autoincrement=False)
    UsuarioID = db.Column(db.Integer,db.ForeignKey('tblusuarios.id'))
    FechaInicio = db.Column(db.DateTime)
    FechaFin = db.Column(db.DateTime)
    Estado = db.Column(db.String(100))
    
    def __init__(self, ReservacionID, UsuarioID, FechaInicio, FechaFin, Estado, ):
        self.ReservacionID = ReservacionID
        self.UsuarioID = UsuarioID
        self.FechaInicio = FechaInicio
        self.FechaFin = FechaFin
        self.Estado = Estado

with app.app_context():
    db.create_all()

class ReservacionSchema(ma.Schema):
    class Meta:
        fields = ('ReservacionID', 'UsuarioID', 'FechaInicio', 'FechaFin', 'Estado')