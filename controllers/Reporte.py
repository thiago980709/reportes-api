from flask import jsonify, request
from db.db import cnx

class Reporte():
    global cur
    cur = cnx.cursor()

    def list():
        lista = []
        cur.execute("SELECT * FROM reporte")
        rows = cur.fetchall()
        columns = [i[0] for i in cur.description]
        for row in rows:
            registro = zip(columns, row)
            json = dict(registro)
            lista.append(json)
        return jsonify(lista)
        cnx.close

    def create(body):
        data = (body['tipoArchivo'], body['archivoDir'], body['estado'], body['resultadoDir'], body['nombreReporte'], body['descripcionReporte'], body['personaEncargada'])
        sql = "INSERT INTO reportes(tipo_archivo, archivo_dir, estado, resultado_dir, nombre_reporte, descripcion_reporte,persona_encargada) VALUES(%s, %s, %s, %s, %s, %s, %s)"
        cur.execute(sql,data)
        cnx.commit()
        return {'estado': 'Insertado'}, 200
        cnx.close
    
    def update(body):
        data = (body['personaEncargada'],body['idReporte'])
        sql = "UPDATE reportes SET persona_encargada =%s WHERE id_reporte=%s"
        cur.execute(sql,data)
        cnx.commit()
        return {'estado': 'Actualizado'}, 200
        cnx.close

    def delete(id_reporte):  
        sql = "DELETE FROM reportes WHERE id_reporte=%s"
        ex = cur.execute(sql,(id_reporte,))
        cnx.commit()
        return {'estado': 'Eliminado'}, 200
        cnx.close
