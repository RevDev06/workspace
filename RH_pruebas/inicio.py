from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

###Idiomas


@app.route('/idioma')
def idioma():
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idIdioma, descripcion from idioma order by idIdioma')
    datos = cursor.fetchall()
    return render_template("idioma.html", comentarios = datos)

@app.route('/idioma_agregar')
def idioma_agregar():
    return render_template("idioma_agr.html")


@app.route('/idioma_fagrega', methods=['POST'])
def idioma_fagrega():
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
        cursor = conn.cursor()
        cursor.execute('insert into idioma (descripcion) values (%s)',(desc))
        conn.commit()
    return redirect(url_for('idioma'))

@app.route('/idioma_editar/<string:id>')
def idioma_editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idIdioma, descripcion from idioma where idIdioma = %s', (id))
    dato  = cursor.fetchall()
    return render_template("idioma_edi.html", comentar=dato[0])

@app.route('/idioma_fedita/<string:id>',methods=['POST'])
def idioma_fedita(id):
    if request.method == 'POST':
        desc=request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
        cursor = conn.cursor()
        cursor.execute('update idioma set descripcion=%s where idIdioma=%s', (desc,id))
        conn.commit()
    return redirect(url_for('idioma'))

@app.route('/idioma_borrar/<string:id>')
def idioma_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute('delete from idioma where idIdioma = {0}'.format(id))
    conn.commit()
    return redirect(url_for('idioma'))

###habilidades

@app.route('/habilidad')
def habilidad():
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idHabilidad, descripcion from habilidad order by idHabilidad')
    datos = cursor.fetchall()
    return render_template("habilidad.html", comentarios = datos)

@app.route('/habilidad_agregar')
def habilidad_agregar():
    return render_template("habilidad_agr.html")


@app.route('/habilidad_fagrega', methods=['POST'])
def habilidad_fagrega():
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
        cursor = conn.cursor()
        cursor.execute('insert into habilidad (descripcion) values (%s)',(desc))
        conn.commit()
    return redirect(url_for('habilidad'))

@app.route('/habilidad_editar/<string:id>')
def habilidad_editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idHabilidad, descripcion from habilidad where idHabilidad = %s', (id))
    dato  = cursor.fetchall()
    return render_template("habilidad_edi.html", comentar=dato[0])

@app.route('/habilidad_fedita/<string:id>',methods=['POST'])
def habilidad_fedita(id):
    if request.method == 'POST':
        desc=request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
        cursor = conn.cursor()
        cursor.execute('update habilidad set descripcion=%s where idHabilidad=%s', (desc,id))
        conn.commit()
    return redirect(url_for('habilidad'))

@app.route('/habilidad_borrar/<string:id>')
def habilidad_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute('delete from habilidad where idHabilidad = {0}'.format(id))
    conn.commit()
    return redirect(url_for('habilidad'))


@app.route('/gradoAvance')
def gradoAvance():
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idGradoAvance, descripcion from grado_avance order by idGradoAvance')
    datos = cursor.fetchall()
    return render_template("gradoAvance.html", comentarios = datos)

@app.route('/grado_agregar')
def grado_agregar():
    return render_template("grado_agr.html")


@app.route('/grado_fagrega', methods=['POST'])
def grado_fagrega():
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
        cursor = conn.cursor()
        cursor.execute('insert into grado_avance (descripcion) values (%s)',(desc))
        conn.commit()
    return redirect(url_for('gradoAvance'))

@app.route('/grado_editar/<string:id>')
def grado_editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idGradoAvance, descripcion from grado_avance where idGradoAvance = %s', (id))
    dato  = cursor.fetchall()
    return render_template("grado_edi.html", comentar=dato[0])

@app.route('/grado_fedita/<string:id>',methods=['POST'])
def grado_fedita(id):
    if request.method == 'POST':
        desc=request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
        cursor = conn.cursor()
        cursor.execute('update grado_avance set descripcion=%s where idGradoAvance=%s', (desc,id))
        conn.commit()
    return redirect(url_for('gradoAvance'))

@app.route('/grado_borrar/<string:id>')
def grado_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute('delete from grado_avance where idGradoAvance = {0}'.format(id))
    conn.commit()
    return redirect(url_for('gradoAvance'))

@app.route('/area')
def area():
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idArea, descripcion from area order by idArea')
    datos = cursor.fetchall()
    return render_template("area.html", comentarios = datos)

@app.route('/area_editar/<string:id>')
def area_editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idArea, descripcion from area where idArea = %s', (id))
    dato  = cursor.fetchall()
    return render_template("area_edi.html", comentar=dato[0])

@app.route('/area_fedita/<string:id>',methods=['POST'])
def area_fedita(id):
    if request.method == 'POST':
        desc=request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
        cursor = conn.cursor()
        cursor.execute('update area set descripcion=%s where idArea=%s', (desc,id))
        conn.commit()
    return redirect(url_for('area'))

@app.route('/area_borrar/<string:id>')
def area_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute('delete from area where idArea = {0}'.format(id))
    conn.commit()
    return redirect(url_for('area'))

@app.route('/area_agregar')
def area_agregar():
    return render_template("area_agr.html")

@app.route('/area_fagrega', methods=['POST'])
def area_fagrega():
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
        cursor = conn.cursor()
        cursor.execute('insert into area (descripcion) values (%s)',(desc))
        conn.commit()
    return redirect(url_for('area'))



@app.route('/puesto')
def puesto():
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()

    cursor.execute('select idPuesto, nomPuesto from puesto order by idPuesto')
    datos = cursor.fetchall()

    return render_template("puesto.html", pue = datos, dat='   ', catArea = '   ', catEdoCivil = '   ', catEscolaridad = '   ',
                           catGradoAvance = '    ', catCarrera = '    ', catIdioma = ' ', catHabilidad = ' ')


@app.route('/puesto_fdetalle/<string:idP>', methods=['GET'])
def puesto_fdetalle(idP):
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()

    cursor.execute('select idPuesto, nomPuesto from puesto order by idPuesto')
    datos = cursor.fetchall()

    cursor.execute('select idPuesto,codPuesto,idArea,nomPuesto,puestoJefeSup,jornada,remunMensual,prestaciones,descripcionGeneral,'
            'funciones,edad,sexo,idEstadoCivil,idEscolaridad,idGradoAvance,idCarrera,experiencia,conocimientos,manejoEquipo,'
            'reqFisicos,reqPsicologicos,responsabilidades,condicionesTrabajo from puesto where idPuesto = %s', (idP))
    dato = cursor.fetchall()

    cursor.execute('select a.idArea, a.descripcion from area a, puesto b where a.idArea = b.idArea and b.idPuesto = %s', (idP))
    datos1 = cursor.fetchall()

    cursor.execute('select a.idEstadoCivil, a.descripcion from estado_civil a, puesto b where a.idEstadoCivil = b.idEstadoCivil and b.idPuesto = %s', (idP))
    datos2 = cursor.fetchall()

    cursor.execute('select a.idEscolaridad, a.descripcion from escolaridad a, puesto b where a.idEscolaridad = b.idEscolaridad and b.idPuesto = %s', (idP))
    datos3 = cursor.fetchall()

    cursor.execute('select a.idGradoAvance, a.descripcion from grado_avance a, puesto b where a.idGradoAvance = b.idGradoAvance and b.idPuesto = %s', (idP))
    datos4 = cursor.fetchall()

    cursor.execute('select a.idCarrera, a.descripcion from carrera a, puesto b where a.idCarrera = b.idCarrera and b.idPuesto = %s', (idP))
    datos5 = cursor.fetchall()

    cursor.execute('select a.idPuesto, b.idIdioma, b.descripcion from puesto a, idioma b, puesto_has_idioma c '
                   'where a.idPuesto = c.idPuesto and b.idIdioma = c.idIdioma and a.idPuesto = %s', (idP))
    datos6 = cursor.fetchall()

    cursor.execute('select a.idPuesto, b.idHabilidad, b.descripcion from puesto a, habilidad b, puesto_has_habilidad c '
                   'where a.idPuesto = c.idPuesto and b.idHabilidad = c.idHabilidad and a.idPuesto = %s', (idP))
    datos7 = cursor.fetchall()
    return render_template("puesto.html", pue = datos, dat=dato[0], catArea=datos1[0], catEdoCivil=datos2[0], catEscolaridad=datos3[0],
                           catGradoAvance=datos4[0], catCarrera=datos5[0], catIdioma=datos6, catHabilidad=datos7)

@app.route('/puesto_borrar/<string:idP>')
def puesto_borrar(idP):
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute('delete from puesto where idPuesto = %s',(idP))
    conn.commit()
    cursor.execute('delete from puesto_has_habilidad where idPuesto =%s ', (idP))
    conn.commit()
    cursor.execute('delete from puesto_has_idioma where idPuesto =%s ', (idP))
    conn.commit()
    return redirect(url_for('puesto'))


@app.route('/puesto_agrOp2')
def puesto_agrOp2():
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idArea, descripcion from area ')
    datos1 = cursor.fetchall()

    cursor.execute('select idEstadoCivil, descripcion from estado_civil ')
    datos2 = cursor.fetchall()

    cursor.execute('select idEscolaridad, descripcion from escolaridad ')
    datos3 = cursor.fetchall()

    cursor.execute('select idGradoAvance, descripcion from grado_avance ')
    datos4 = cursor.fetchall()

    cursor.execute('select idCarrera, descripcion from carrera ')
    datos5 = cursor.fetchall()

    cursor.execute('select idIdioma, descripcion from idioma ')
    datos6 = cursor.fetchall()

    cursor.execute('select idHabilidad, descripcion from habilidad ')
    datos7 = cursor.fetchall()

    return render_template("puesto_agrOp2.html", catArea=datos1, catEdoCivil=datos2, catEscolaridad=datos3,
                           catGradoAvance=datos4, catCarrera=datos5, catIdioma=datos6, catHabilidad=datos7)


@app.route('/puesto_fagrega2', methods=['POST'])
def puesto_fagrega():
    if request.method == 'POST':

        if  'idArea' in request.form:
            idAr = request.form['idArea']
        else:
            idAr = '1'
        if 'idEstadoCivil' in request.form:
            idEC = request.form['idEstadoCivil']
        else:
            idEC = '1'
        if 'idEscolaridad' in request.form:
            idEs = request.form['idEscolaridad']
        else:
            idEs = '1'
        if 'idGradoAvance' in request.form:
            idGA = request.form['idGradoAvance']
        else:
            idGA = '1'
        if 'idCarrera' in request.form:
            idCa = request.form['idCarrera']
        else:
            idCa = '1'
        if 'sexo' in request.form:
            sex = request.form['sexo']
        else:
            sex = '1'
        codP = request.form['codPuesto']
        nomP = request.form['nomPuesto']
        pueJ = request.form['puestoJefeSup']
        jorn = request.form['jornada']
        remu = request.form['remunMensual']
        pres = request.form['prestaciones']
        desc = request.form['descripcionGeneral']
        func = request.form['funciones']
        eda = request.form['edad']
        expe = request.form['experiencia']
        cono = request.form['conocimientos']
        manE = request.form['manejoEquipo']
        reqF = request.form['reqFisicos']
        reqP = request.form['reqPsicologicos']
        resp = request.form['responsabilidades']
        conT = request.form['condicionesTrabajo']


    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute(
    'insert into puesto (codPuesto,idArea,nomPuesto,puestoJefeSup,jornada,remunMensual,prestaciones,descripcionGeneral,'
    'funciones,edad,sexo,idEstadoCivil,idEscolaridad,idGradoAvance,idCarrera,experiencia,conocimientos,manejoEquipo,'
    'reqFisicos,reqPsicologicos,responsabilidades,condicionesTrabajo) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
    (codP, idAr, nomP, pueJ, jorn, remu, pres, desc, func, eda, sex, idEC, idEs, idGA, idCa, expe, cono, manE, reqF,
     reqP, resp, conT))
    conn.commit()

    cursor.execute('select idPuesto from puesto where idPuesto=(select max(idPuesto) from puesto) ')
    dato = cursor.fetchall()
    idpue = dato[0]
    idP = idpue[0]

    cursor.execute('select count(*) from idioma ')
    dato = cursor.fetchall()
    nidio = dato[0]
    ni = nidio[0] + 1

    for i in range(1, ni):
        idio = 'i' + str(i)
        if idio in request.form:
            cursor.execute('insert into puesto_has_idioma(idPuesto,idIdioma) values (%s,%s)', (idP, i))
            conn.commit()

    cursor.execute('select count(*) from habilidad ')
    dato = cursor.fetchall()
    nhab = dato[0]
    nh =nhab[0]+1

    for i in range(1,nh):
        habi = 'h' + str(i)
        if habi in request.form:
            cursor.execute('insert into puesto_has_habilidad(idPuesto,idHabilidad) values (%s,%s)', (idP,i))
            conn.commit()

    return redirect(url_for('puesto'))



@app.route('/puesto_editar/<string:idP>')
def puesto_editar(idP):
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()

    cursor.execute('select idPuesto,codPuesto,idArea,nomPuesto,puestoJefeSup,jornada,remunMensual,prestaciones,descripcionGeneral,'
        'funciones,edad,sexo,idEstadoCivil,idEscolaridad,idGradoAvance,idCarrera,experiencia,conocimientos,manejoEquipo,'
        'reqFisicos,reqPsicologicos,responsabilidades,condicionesTrabajo from puesto where idPuesto = %s', (idP))
    dato = cursor.fetchall()

    cursor.execute('select idArea, descripcion from area ')
    datos1 = cursor.fetchall()

    cursor.execute('select idEstadoCivil, descripcion from estado_civil ')
    datos2 = cursor.fetchall()

    cursor.execute('select idEscolaridad, descripcion from escolaridad ')
    datos3 = cursor.fetchall()

    cursor.execute('select idGradoAvance, descripcion from grado_avance ')
    datos4 = cursor.fetchall()

    cursor.execute('select idCarrera, descripcion from carrera ')
    datos5 = cursor.fetchall()

    cursor.execute('select idIdioma, descripcion from idioma ')
    datos6 = cursor.fetchall()

    cursor.execute('select idHabilidad, descripcion from habilidad ')
    datos7 = cursor.fetchall()

    cursor.execute('select a.idArea, a.descripcion from area a, puesto b where a.idArea = b.idArea and b.idPuesto = %s', (idP))
    datos11 = cursor.fetchall()

    cursor.execute('select a.idEstadoCivil, a.descripcion from estado_civil a, puesto b where a.idEstadoCivil = b.idEstadoCivil and b.idPuesto = %s',(idP))
    datos12 = cursor.fetchall()

    cursor.execute('select a.idEscolaridad, a.descripcion from escolaridad a, puesto b where a.idEscolaridad = b.idEscolaridad and b.idPuesto = %s',(idP))
    datos13 = cursor.fetchall()

    cursor.execute('select a.idGradoAvance, a.descripcion from grado_avance a, puesto b where a.idGradoAvance = b.idGradoAvance and b.idPuesto = %s',(idP))
    datos14 = cursor.fetchall()

    cursor.execute('select a.idCarrera, a.descripcion from carrera a, puesto b where a.idCarrera = b.idCarrera and b.idPuesto = %s', (idP))
    datos15 = cursor.fetchall()

    cursor.execute('select a.idPuesto, b.idIdioma, b.descripcion from puesto a, idioma b, puesto_has_idioma c '
                   'where a.idPuesto = c.idPuesto and b.idIdioma = c.idIdioma and a.idPuesto = %s', (idP))
    datos16 = cursor.fetchall()

    cursor.execute('select a.idPuesto, b.idHabilidad, b.descripcion from puesto a, habilidad b, puesto_has_habilidad c '
                   'where a.idPuesto = c.idPuesto and b.idHabilidad = c.idHabilidad and a.idPuesto = %s', (idP))
    datos17 = cursor.fetchall()


    return render_template("puesto_edi.html", dat=dato[0], catArea=datos1, catEdoCivil=datos2, catEscolaridad=datos3,
                           catGradoAvance=datos4, catCarrera=datos5, catIdioma=datos6, catHabilidad=datos7,
                           Area=datos11[0], EdoCivil=datos12[0], Escolaridad=datos13[0], GradoAvance=datos14[0],
                           Carrera=datos15[0], Idioma=datos16, Habilidad=datos17)


@app.route('/puesto_fedita/<string:idP>', methods=['POST'])
def puesto_fedita(idP):
    if request.method == 'POST':
        codP = request.form['codPuesto']
        idAr = request.form['idArea']
        nomP = request.form['nomPuesto']
        pueJ = request.form['puestoJefeSup']
        jorn = request.form['jornada']
        remu = request.form['remunMensual']
        pres = request.form['prestaciones']
        desc = request.form['descripcionGeneral']
        func = request.form['funciones']
        eda = request.form['edad']
        sex = request.form['sexo']
        idEC = request.form['idEstadoCivil']
        idEs = request.form['idEscolaridad']
        idGA = request.form['idGradoAvance']
        idCa = request.form['idCarrera']
        expe = request.form['experiencia']
        cono = request.form['conocimientos']
        manE = request.form['manejoEquipo']
        reqF = request.form['reqFisicos']
        reqP = request.form['reqPsicologicos']
        resp = request.form['responsabilidades']
        conT = request.form['condicionesTrabajo']

    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()

    cursor.execute('update puesto set codPuesto = %s, idArea = %s, nomPuesto = %s, puestoJefeSup = %s, jornada = %s, '
                   'remunMensual = %s, prestaciones = %s, descripcionGeneral = %s, funciones = %s, edad = %s, sexo = %s, '
                   'idEstadoCivil = %s, idEscolaridad = %s, idGradoAvance = %s, idCarrera = %s, experiencia = %s, '
                   'conocimientos = %s, manejoEquipo = %s, reqFisicos = %s, reqPsicologicos = %s, responsabilidades = %s, '
                   'condicionesTrabajo = %s where idPuesto = %s', (codP, idAr, nomP, pueJ, jorn, remu, pres, desc, func, eda,
                   sex, idEC, idEs, idGA, idCa, expe, cono, manE, reqF, reqP, resp, conT, idP))
    conn.commit()

    cursor.execute('delete from puesto_has_habilidad where idPuesto =%s ', (idP))
    conn.commit()
    cursor.execute('delete from puesto_has_idioma where idPuesto =%s ', (idP))
    conn.commit()

    cursor.execute('select count(*) from idioma ')
    dato = cursor.fetchall()
    nidio = dato[0]
    ni = nidio[0] + 1

    for i in range(1, ni):
        idio = 'i' + str(i)
        if idio in request.form:
            cursor.execute('insert into puesto_has_idioma(idPuesto,idIdioma) values (%s,%s)', (idP, i))
            conn.commit()

    cursor.execute('select count(*) from habilidad ')
    dato = cursor.fetchall()
    nhab = dato[0]
    nh = nhab[0] + 1

    for i in range(1, nh):
        habi = 'h' + str(i)
        if habi in request.form:
            cursor.execute('insert into puesto_has_habilidad(idPuesto,idHabilidad) values (%s,%s)', (idP, i))
            conn.commit()
    return redirect(url_for('puesto'))



@app.route('/carrera')
def carrera():
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute("SELECT idCarrera, descripcion FROM carrera ORDER BY idCarrera")
    dato = cursor.fetchall()
    return render_template("carrera.html", datos = dato)

@app.route('/carre_agregar')
def agreCarre():
    return render_template("carre_agre.html")

@app.route("/agregarCarre", methods=['POST'])
def agregarCarrera():
    if request.method == 'POST':
        descrip = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO carrera (descripcion) VALUES (%s)", (descrip))
        conn.commit()
    return redirect(url_for('carrera'))

@app.route("/carre_editar/<string:idd>")
def editarcarre(idd):
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute("SELECT idCarrera, descripcion FROM carrera WHERE idCarrera=%s", (idd))
    dato = cursor.fetchall()
    return render_template("editarCarre.html", dato = dato[0])

@app.route("/updateCarre/<string:idd>", methods=['POST'])
def updateCarre(idd):
    if request.method == 'POST':
        descrip = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
        cursor = conn.cursor()
        cursor.execute("UPDATE carrera SET descripcion = %s WHERE idCarrera = %s", (descrip, idd))
        conn.commit()
    return redirect(url_for('carrera'))

@app.route("/carre_borrar/<string:idd>")
def borrarCarre(idd):
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM carrera WHERE idCarrera = %s", (idd))
    conn.commit()
    return redirect(url_for('carrera'))



@app.route("/escolaridad")
def escolaridad():
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute("SELECT idEscolaridad, descripcion FROM escolaridad ORDER BY idEscolaridad")
    datos = cursor.fetchall()
    return render_template("escolaridad.html", datos = datos)

@app.route("/esco_agregar")
def agreEsco():
    return render_template("esco_agre.html")

@app.route("/agregarEsco", methods=['POST'])
def agregarEscolaridad():
    if request.method == 'POST':
        descrip = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO escolaridad (descripcion) VALUES (%s)", (descrip))
        conn.commit()
    return redirect(url_for("escolaridad"))

@app.route("/esco_editar/<string:idd>")
def editarEsco(idd):
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute("SELECT idEscolaridad, descripcion FROM escolaridad WHERE idEscolaridad = %s", (idd))
    dato = cursor.fetchall()
    return render_template("editarEsco.html", dato = dato[0])

@app.route("/updateEsco/<string:idd>", methods=['POST'])
def updateEsco(idd):
    if request.method == 'POST':
        descrip = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
        cursor = conn.cursor()
        cursor.execute("UPDATE escolaridad SET descripcion = %s WHERE idEscolaridad = %s", (descrip, idd))
        conn.commit()
    return redirect(url_for('escolaridad'))

@app.route("/esco_borrar/<string:idd>")
def borrarEsco(idd):
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM escolaridad WHERE idEscolaridad = %s", (idd))
    conn.commit()
    return redirect(url_for("escolaridad"))


@app.route("/edocivil")
def edocivil():
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute("SELECT idEstadoCivil, descripcion FROM estado_civil ORDER BY idEstadoCivil")
    datos = cursor.fetchall()
    return render_template("edoCivil.html", datos = datos)

@app.route("/edociv_agregar")
def agreEdoCiv():
    return render_template("edociv_agre.html")

@app.route("/agregarEdociv", methods=['POST'])
def agregarEdoCiv():
    if request.method == 'POST':
        descrip = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO estado_civil (descripcion) VALUES (%s)", (descrip))
        conn.commit()
    return redirect(url_for("edocivil"))

@app.route("/edoc_editar/<string:idd>")
def editarEdociv(idd):
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute("SELECT idEstadoCivil, descripcion FROM estado_civil WHERE idEstadoCivil = %s", (idd))
    dato = cursor.fetchall()
    return render_template("editarEdociv.html", dato = dato[0])

@app.route("/updateEdociv/<string:idd>", methods=['POST'])
def updateEdociv(idd):
    if request.method == 'POST':
        descrip = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
        cursor = conn.cursor()
        cursor.execute("UPDATE estado_civil SET descripcion = %s WHERE idEstadoCivil = %s", (descrip, idd))
        conn.commit()
    return redirect(url_for("edocivil"))

@app.route("/edoc_borrar/<string:idd>")
def borrarEdociv(idd):
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM estado_civil WHERE idEstadoCivil = %s", (idd))
    conn.commit()
    return redirect(url_for("edocivil"))


@app.route("/candidatos")
def candidatos():
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute("SELECT b.folio, a.idVacante, c.nomPuesto FROM vacante a, requisicion b, puesto c WHERE a.idRequisicion=b.idRequisicion AND a.idPuesto=c.idPuesto AND b.idPuesto=c.idPuesto")
    datos = cursor.fetchall()
    return render_template("candidatos.html", datos = datos)

@app.route("/capturarCand/<string:idV>")
def capturarCandidatos(idV):
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute("SELECT b.folio, a.idVacante, c.nomPuesto FROM vacante a, requisicion b, puesto c WHERE a.idRequisicion=b.idRequisicion AND a.idPuesto=c.idPuesto AND b.idPuesto=c.idPuesto AND a.idVacante=%s", (idV))
    datos = cursor.fetchall()
    
    cursor.execute('select idEstadoCivil, descripcion from estado_civil ')
    datos2 = cursor.fetchall()

    cursor.execute('select idEscolaridad, descripcion from escolaridad ')
    datos3 = cursor.fetchall()

    cursor.execute('select idGradoAvance, descripcion from grado_avance ')
    datos4 = cursor.fetchall()

    cursor.execute('select idCarrera, descripcion from carrera ')
    datos5 = cursor.fetchall()

    return render_template("capturarCand.html", dato = datos[0], catEdoCivil=datos2, catEscolaridad=datos3, catGradoAvance=datos4, catCarrera=datos5)

@app.route("/seleccionCand/<string:idV>")
def verCandidatosVacante(idV):
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor()
    cursor.execute("SELECT b.nomPuesto FROM puesto b, vacante a WHERE a.idVacante=%s AND a.idPuesto=b.idPuesto", (idV))
    nomPuestoVacante = cursor.fetchall()
    cursor.execute("SELECT a.idCandidato, a.idVacante, a.idRequisicion, a.nombre, a.CURP FROM candidato a, vacante b WHERE a.idVacante=%s AND a.idVacante=b.idVacante", (idV))
    datos = cursor.fetchall()
    return render_template("candVacan.html", datos = datos, nomPuesto = nomPuestoVacante[0][0])

@app.route("/candSelec/<string:idV>")
def showSelectedCand(idV):
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor() 
    cursor.execute("SELECT b.nomPuesto FROM puesto b, vacante a WHERE a.idVacante=%s AND a.idPuesto=b.idPuesto", (idV))
    nomPuestoVacante = cursor.fetchall()
    cursor.execute("SELECT idCandidato, nombre, CURP FROM candidatoSeleccionado WHERE idVacante=%s", (idV))
    datos = cursor.fetchall()
    return render_template("candSelecc.html", datos = datos, nomPuesto = nomPuestoVacante[0][0])

@app.route("/borrarCand/<string:idC>")
def borrarCand(idC):
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='rh3')
    cursor = conn.cursor() 
    cursor.execute("DELETE FROM candidato WHERE idCandidato=%s", (idC))
    conn.commit()
    return redirect(url_for(""))



if __name__ == "__main__":
    app.run(debug=True)