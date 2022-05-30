import cgitb, cgi
import geo_funcs

# habilita a visualização de erros
cgitb.enable(display=0, logdir=".")

# instancia um form para receber dados do navegador
form = cgi.FieldStorage()

# logica do script
# recebe o valor do raio de usuário
base_ = float(form.getvalue('base'))
altura_ = float(form.getvalue('altura'))

# calcular área
area_triangulo = (base_ * altura_) / 2

# HTML
title = "Triânguluzinho do amor"
geo_funcs.print_header(title)
print("<h1>{}</h1>".format(title))

print('<hr>')

print("<p>Base: {:.2f}</p>".format(base_))
print("<p>Altura: {:.2f}</p>".format(altura_))
print("<p>Área do Triângulo: {:.1f}</p>".format(area_triangulo))

# calcular perimetro
perimetro_triangulo = base_ + altura_ * 2

print("<p>Perímetro do Triangulo: {:.1f}</p>".format(perimetro_triangulo))

print('<hr>')

print("<p>Clique <a href=\'/triangulo.html\'>aqui</a> para novo cálculo.</p>")
print("<p>Clique <a href=\'/\'>aqui</a> para voltar ao menu principal.</p>")
geo_funcs.print_footer()
