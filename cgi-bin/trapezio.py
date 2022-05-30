import cgitb, cgi
import geo_funcs

# habilita a visualização de erros
cgitb.enable(display=0, logdir=".")

# instancia um form para receber dados do navegador
form = cgi.FieldStorage()

# logica do script
# recebe o valor do raio de usuário
baZinha_ = float(form.getvalue('baZinha'))
baZona_ = float(form.getvalue('baZona'))
altura_ = float(form.getvalue('altura'))

# calcular área
area_trapezio = ((baZinha_ + baZona_) * altura_) / 2

# HTML
title = "Trapézio"
geo_funcs.print_header(title)
print("<h1>{}</h1>".format(title))

print('<hr>')

print("<p>Bazinha: {:.2f}</p>".format(baZinha_))
print("<p>Bazona: {:.2f}</p>".format(baZona_))
print("<p>Altura: {:.2f}</p>".format(altura_))
print("<p>Área do Trapézio: {:.1f}</p>".format(area_trapezio))

# calcular perimetro
perimetro_trapezio = baZona_ + baZinha_ + (altura_ * 2)

print("<p>Perímetro do Trapézio: {:.1f}</p>".format(perimetro_trapezio))

print('<hr>')

print("<p>Clique <a href=\'/trapezio.html\'>aqui</a> para novo cálculo.</p>")
print("<p>Clique <a href=\'/\'>aqui</a> para voltar ao menu principal.</p>")
geo_funcs.print_footer()
