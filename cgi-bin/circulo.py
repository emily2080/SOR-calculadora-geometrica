import cgitb, cgi
import math
import geo_funcs

# habilita a visualização de erros
cgitb.enable(display=0, logdir=".")

# instancia um form para receber dados do navegador
form = cgi.FieldStorage()

# logica do script
# recebe o valor do raio de usuário
raio_ = float(form.getvalue('raio'))

# calcular área
area_circ = math.pi * math.pow(raio_, 2)

# HTML
title = "Circulo"
geo_funcs.print_header(title)
print("<h1>{}</h1>".format(title))

print('<hr>')

print("<p>Raio: {:.2f}</p>".format(raio_))
print("<p>Área do círculo: {:.1f}</p>".format(area_circ))

# calcular perimetro
perimetro_circ = 2 * math.pi * raio_

print("<p>Perímetro do Circulo: {:.1f}</p>".format(perimetro_circ))

print('<hr>')

print("<p>Clique <a href=\'/circulo.html\'>aqui</a> para novo cálculo.</p>")
print("<p>Clique <a href=\'/\'>aqui</a> para voltar ao menu principal.</p>")
geo_funcs.print_footer()
