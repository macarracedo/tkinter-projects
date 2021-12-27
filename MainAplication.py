import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

from Cliente import Cliente
from Oficina import Oficina
from Poliza import Poliza
from Vivienda import Vivienda

class MainApplication(tk.Tk):
    def __init__(self, parent, miOficina, *args, **kwargs, ):
        tk.Tk.__init__(self, parent, *args, **kwargs)

        self._oficina = miOficina
        self.frIntroducirDatos = tk.Frame(self,borderwidth=3)
        self.btAdd = tk.Button(self.frIntroducirDatos, text="Introducir Datos", command=self.insertaDato, bg="white")
        self.btRemove = tk.Button(self.frIntroducirDatos, text="Eliminar Datos", command=self.checkDeleteSelection, bg="white")
        self.btPrintPoliza = tk.Button(self.frIntroducirDatos, text="Consulta Datos Poliza", command=self.checkPrintSelection, bg="white")

        self.frDatosCliente=tk.Frame(self,borderwidth=3)


        self.datosCliente = tk.Label(self.frDatosCliente, text="Datos Cliente")
        self.name = tk.Label(self.frDatosCliente,text="Nombre")
        self.nameEntry = tk.Entry(self.frDatosCliente)
        self.dni = tk.Label(self.frDatosCliente, text="Dni")
        self.dniEntry = tk.Entry(self.frDatosCliente)
        self.age = tk.Label(self.frDatosCliente, text="Edad")
        self.ageEntry = tk.Entry(self.frDatosCliente)


        self.frDatosVivienda = tk.Frame(self,borderwidth=10)

        self.datosVivienda = tk.Label(self.frDatosVivienda,text="Datos Vivienda")
        self.reference = tk.Label(self.frDatosVivienda,text="Ref. Catastral")
        self.referenceEntry = tk.Entry(self.frDatosVivienda)
        self.area = tk.Label(self.frDatosVivienda,text="Superficie (m2)")
        self.areaEntry = tk.Entry(self.frDatosVivienda)
        self.value = tk.Label(self.frDatosVivienda,text="Valor catastral")
        self.valueEntry = tk.Entry(self.frDatosVivienda)

        self.frIntroducirDatos['borderwidth'] = 5
        self.frIntroducirDatos['relief'] = 'sunken'
        self.frIntroducirDatos.pack(side="bottom", fill="both")
        self.btAdd.pack()
        #self.btAdd.grid(column=0, row=0, padx=5, pady=5)
        #self.btRemove.grid(column=0, row=2, padx=5, pady=5)

        self.frDatosCliente['borderwidth'] = 5
        self.frDatosCliente['relief'] = 'sunken'

        self.frDatosCliente.pack(side="left", fill="both")
        self.datosCliente.grid(column=0,row=0, columnspan=2,padx=10, pady=10, sticky=tk.EW)
        self.name.grid(column=0,row=1,padx=10, pady=10)
        self.nameEntry.grid(column=1,row=1,padx=10, pady=10)
        self.dni.grid(column=0,row=2,padx=10, pady=10)
        self.dniEntry.grid(column=1,row=2,padx=10, pady=10)
        self.age.grid(column=0,row=3,padx=10, pady=10)
        self.ageEntry.grid(column=1,row=3,padx=10, pady=10)

        self.frDatosVivienda['borderwidth'] = 5
        self.frDatosVivienda['relief'] = 'sunken'
        self.frDatosVivienda.pack(side="right", fill="both")
        self.datosVivienda.grid(column=0,row=0, columnspan=2,padx=10, pady=10)
        self.reference.grid(column=0, row=1, padx=10, pady=10)
        self.referenceEntry.grid(column=1, row=1, padx=10, pady=10)
        self.area.grid(column=0, row=2, padx=10, pady=10)
        self.areaEntry.grid(column=1, row=2, padx=10, pady=10)
        self.value.grid(column=0, row=3, padx=10, pady=10)
        self.valueEntry.grid(column=1, row=3, padx=10, pady=10)


        """ TreeView con listado de asegurados-viviendas"""
        columns = ('num_poliza','name', 'dni', 'age', 'reference', 'area', 'value')
        self.tree = ttk.Treeview(self.frIntroducirDatos, columns=columns, show='headings')
        self.tree.column('num_poliza', width=100, anchor=tk.W)
        self.tree.heading('num_poliza', text='Num. Póliza')
        self.tree.column('name', width=100, anchor=tk.W)
        self.tree.heading('name', text='Cliente')
        self.tree.column('dni', width=100, anchor=tk.W)
        self.tree.heading('dni', text='Dni')
        self.tree.column('age', width=100, anchor=tk.W)
        self.tree.heading('age', text='Edad')
        self.tree.column('reference', width=200, anchor=tk.W)
        self.tree.heading('reference', text='Ref. Catastral')
        self.tree.column('area', width=120, anchor=tk.W)
        self.tree.heading('area', text='Superficie(m2)')
        self.tree.column('value', width=120, anchor=tk.W)
        self.tree.heading('value', text='Valor Catastral')
        #self.tree.grid(column=0, row=1, padx=5, pady=5)
        self.tree.pack()
        self.btRemove.pack()
        self.btPrintPoliza.pack()
        #username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

    def insertaTreeview(self, poliza):
        cliente = poliza.cliente
        vivienda = poliza.vivienda
        toAdd = [f'{poliza.num_poliza}', f'{cliente.nombre}', f'{cliente.dni}', f'{cliente.edad}',
                 f'{vivienda.refCatastral}', f'{vivienda.metrosCuadrados}', f'{vivienda.valorCatastral}']
        self.tree.insert('', tk.END, values=toAdd)

    def updateTreeView(self):
        self.tree.delete(*self.tree.get_children())
        for x, y in self._oficina.getItems():
            # x - num_poliza
            # y - poliza
            self.insertaTreeview(y)

    def clearEntries(self):
        #self.nameEntry.select_clear()
        self.nameEntry.option_clear()

    def validaDatosNumericos(self):
        toret = False
        if self.ageEntry.get().strip().isdigit() and self.areaEntry.get().strip().isdigit() and self.valueEntry.get().strip().isdigit():
            toret = True
        return toret

    def insertaDato(self):
        if self.validaDatosNumericos():
            cliente1 = Cliente(self.nameEntry.get().strip(), self.dniEntry.get().strip(), int(self.ageEntry.get().strip()))
            vivienda1 = Vivienda(self.referenceEntry.get().strip(), int(self.areaEntry.get().strip()), int(self.valueEntry.get().strip()))
            poliza1 = Poliza(cliente1, vivienda1)
            self._oficina.addPair(poliza1)
            self._oficina.saveJSON()
            self.insertaTreeview(poliza1)
            self.clearEntries()
            showinfo(title='Información',
                     message="Se ha insertado con éxito: "
                             "\nCliente: {0} "
                             "\nVivienda: {1}".format(cliente1, vivienda1))
        else:
            showinfo(title='*** Error ***',
                     message="Algunos campos numéricos no tienen el formato correcto.")

    """
        Verifica que se ha seleccionado como máximo y como mínimo 1 elemento del treeView antes de eliminar
    """
    def checkDeleteSelection(self):
        if len(self.tree.selection()) == 1:
            self.eliminaPoliza()
        else:
            showinfo(title='*** Error ***',
                     message="Error al intentar borrar.\nDebe seleccionar un elemento de la lista!"
                             "\nElementos seleccionados: {0} ".format(len(self.tree.selection())))

    def eliminaPoliza(self):
        num_poliza = self.tree.item(self.tree.selection())["values"][0]
        self._oficina.delPair(num_poliza)
        self._oficina.saveJSON()
        self.updateTreeView()
        showinfo(title='*** Información ***',
                 message="Se ha eliminado con éxito la póliza del siguiente asegurado: "
                         "\n{0} ".format(num_poliza))

    def checkPrintSelection(self):
        if len(self.tree.selection()) == 1:
            self.printPoliza()
        else:
            showinfo(title='*** Error ***',
                     message="Error al intentar consultar una poliza.\nDebe seleccionar un elemento de la lista!"
                             "\nElementos seleccionados: {0} ".format(len(self.tree.selection())))

    def printPoliza(self):
        num_poliza = self.tree.item(self.tree.selection())["values"][0]
        par = self._oficina.getPair(num_poliza)
        print(num_poliza)
        print(par)
        #print(par.poliza)
        showinfo(title='Información',
                 message="Datos de la póliza: {0}\n".format(par))

    def __del__(self):
        print("cerrando...")
        #self._oficina.__del__() #Se cierra automáticamente antes que la main windows
        #self._oficina.saveJSON()

if __name__ == "__main__":
    #root = tk.Tk()
    #root.title('Geometría Pack Demostración')
    #root.geometry("400x200")
    miOficina = Oficina()
    #miOficina.loadJSON()
    vistaPpal = MainApplication(None, miOficina)
    vistaPpal.title("Correduría de seguros")
    vistaPpal.geometry("1200x600")
    vistaPpal.mainloop()