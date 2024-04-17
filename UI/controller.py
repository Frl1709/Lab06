import flet as ft
from model.retailer import Retailer as rr

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self.retailer = None
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def populate_dd_anno(self):
        anni = self._model.anni
        for anno in anni:
            self._view.dd_anno.options.append(ft.dropdown.Option(anno))

    def populate_dd_brand(self):
        brand = self._model.brand
        for b in brand:
            self._view.dd_brand.options.append(ft.dropdown.Option(b))

    def populate_dd_retailer(self):
        retailers = self._model.retailers
        nessun_retailer = rr(0, "0", "0", "0")
        self._view.dd_retailer.options.append(ft.dropdown.Option(key=str(nessun_retailer.retailer_code),
                                                                 text="Nessun filtro",
                                                                 data=nessun_retailer,
                                                                 on_click=self.read_retailer))
        for r in retailers:
            self._view.dd_retailer.options.append(ft.dropdown.Option(key=r.retailer_code,
                                                                     text=r.retailer_name,
                                                                     data=r,
                                                                     on_click=self.read_retailer))

    def read_retailer(self, e):
        self.retailer = e.control.data

    def prodotti_of_brand(self, brand):
        prodotti = self._model.product
        prod_list = []
        if brand == "Nessun filtro":
            prod_list = prodotti
        else:
            for p in prodotti:
                if p.product_brand == brand:
                    prod_list.append(p.product_number)
        return prod_list

    def get_selected_sales(self):
        vendite = self._model.vendite
        anno = self._view.dd_anno.value
        brand = self._view.dd_brand.value
        prodotti = self.prodotti_of_brand(brand)
        result = []
        if anno is None:
            self._view.create_alert("Inserire una anno")
            return
        elif brand is None:
            self._view.create_alert("Inserire un brand")
            return
        elif self.retailer is None:
            self._view.create_alert("Inserire un retailer")
            return
        else:
            retailer_code = self.retailer.retailer_code
            if str(anno) == "Nessun filtro" and str(retailer_code) != "0":
                for v in vendite:
                    if v.product_number in prodotti and v.retailer_code == retailer_code:
                        result.append(v)
            elif str(anno) != "Nessun filtro" and str(retailer_code) == "0":
                for v in vendite:
                    if v.date[0:4] == anno and v.product_number in prodotti:
                        result.append(v)
            elif str(anno) == "Nessun filtro" and str(retailer_code) == "0":
                for v in vendite:
                    if v.product_number in prodotti:
                        result.append(v)
            elif str(anno) != "Nessun filtro" and str(retailer_code) != "0":
                for v in vendite:
                    if v.date[0:4] == anno and v.product_number in prodotti and v.retailer_code == retailer_code:
                        result.append(v)
        return result

    def get_top_vendite(self, e):
        result = self.get_selected_sales()
        if result is not None:
            sorted_list = sorted(result, key=lambda x: (x.quantity * x.unit_sale_price), reverse=True)[0:5]
            if len(sorted_list) == 0:
                self._view.txt_result.clean()
                self._view.txt_result.controls.append(ft.Text(f"Non ci sono vendite che corrispondono ai valori specificati"))
                self._view.update_page()
            else:
                self._view.txt_result.clean()
                for vv in sorted_list:
                    self._view.txt_result.controls.append(ft.Text(f"Data: {vv.date}; Ricavo: {vv.quantity * vv.unit_sale_price:.2f}; Product: {vv.product_number}"))
                    self._view.update_page()

    def analizza_vendite(self, e):
        vendite = self.get_selected_sales()
        retailer = []
        numero_vendite = len(vendite)
        volume_affari = 0
        prodotti = []
        for v in vendite:
            volume_affari += v.quantity * v.unit_sale_price
            if v.product_number not in prodotti:
                prodotti.append(v.product_number)
            if v.retailer_code not in retailer:
                retailer.append(v.retailer_code)
        n_prodotti = len(prodotti)
        n_retailer = len(retailer)
        if numero_vendite == 0 or n_prodotti == 0 or volume_affari == 0:
            self._view.txt_result.clean()
            self._view.txt_result.controls.append(ft.Text(f"Non ci sono vendite che corrispondono ai valori specificati"))
            self._view.update_page()
        else:
            self._view.txt_result.clean()
            self._view.txt_result.controls.append(ft.Text(f"Statistiche vendite: \nGiro d'affari: {volume_affari:.2f} \nNumero vendite: {numero_vendite} \nNumero retailers coinvolti: {n_retailer} \nNumero prodotti coinvolti: {n_prodotti}"))
            self._view.update_page()