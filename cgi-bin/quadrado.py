import cgitb, cgi
import geo_funcs

# habilita a visualização de erros
cgitb.enable(display=0, logdir=".")

# instancia um form para receber dados do navegador
form = cgi.FieldStorage()

# logica do script
# recebe o valor do raio de usuário
lado_ = float(form.getvalue('lado'))

# calcular área
area_quadrado = lado_ ** 2

# HTML
title = "Quadrado"
geo_funcs.print_header(title)
print("<h1>{}</h1>".format(title))

print('<hr>')

print("<p>Lado: {:.2f}</p>".format(lado_))
print("<p>Área do quadrado: {:.1f}</p>".format(area_quadrado))

# calcular perimetro
perimetro_quadrado = lado_ * 4

print("<p>Perímetro do Quadrado: {:.1f}</p>".format(perimetro_quadrado))

print('<hr>')

print("<p>Clique <a href=\'/quadrado.html\'>aqui</a> para novo cálculo.</p>")
print("<p>Clique <a href=\'/\'>aqui</a> para voltar ao menu principal.</p>")
geo_funcs.print_footer()
