Precio_del_pan = 3.49
pan_de_otro_día = 60/100
Núm_de_panes_no_frescos = 50

Panes_no_frescos = int(input("Números de panes no frescos vendidos"))


Precio_no_frescas = Panes_no_frescos * Precio_del_pan

Descuento = Precio_no_frescas * pan_de_otro_día

Ganancia = Precio_no_frescas - Descuento

print("Panes no frescos", Núm_de_panes_no_frescos)
print("precio de la barra de pan", Precio_del_pan)
print("descuento de los panes no frescos", Descuento)
print("ganancia de los panes no frescos", Ganancia)