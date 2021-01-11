from datetime import datetime

from reportlab.pdfgen import canvas

import os

import var


class Printer():

    def cabecera(self):
        logo = '.\\img\logo.jpg'
        var.rep.drawImage(logo,450,752)
        var.rep.setTitle('INFORMES')
        var.rep.setAuthor('Administración')
        var.rep.setFont('Helvetica', size=10)
        var.rep.line(45, 820, 525, 820)
        var.rep.line(45, 745, 525, 745)
        textcif ='A00000000H'
        textnom='INPORTACIONES Y EXPORTACIONES'
        textdir='Avenida Galicia, 101 -Vigo'
        texttlfo='886 12 04 64'
        var.rep.drawString(50,805,textcif)
        var.rep.drawString(50, 790, textnom)
        var.rep.drawString(50, 775, textdir)
        var.rep.drawString(50, 760, texttlfo)
        var.rep.drawImage(logo, 450, 752)

    def pie(textlistado):
        try:
            var.rep.line(50,50,525,50)
            fecha=datetime.today()
            fecha=fecha.strftime('%d.%m.%Y   %H.%M.%S')
            var.rep.drawString(460,40,str(fecha))
            var.rep.drawString(275,40,str('Pagina %s' % var.rep.getPageNumber()))
            var.rep.drawString(50,40,str(textlistado))
        except Exception as error:
            print('Error en el pie de informe: %s' %str(error))

    def reportCli(self):
        try:
            var.rep = canvas.Canvas('informes/listadoclientes.pdf')
            Printer.cabecera(self)
            Printer.pie(self)
            var.rep.drawString(100, 750, 'Listado Clientes')
            var.rep.save()
            rootPath = ".\\informes"
            cont = 0
            for file in os.listdir(rootPath):
                if file.endswith('.pdf'):
                    os.startfile("%s/%s" % (rootPath, file))
                cont = cont + 1
        except Exception as error:
            print('Error reportcli %s' % str(error))