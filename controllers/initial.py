# coding=UTF-8

def principal():
	response.title = 'Padrão'
	teste = "página principal"
	
	return response.render("initial/principal.html", teste=teste)


def voos():
	response.title = 'Busque por vôos'
	teste = "página secundaria"
	
	return response.render("initial/voos.html", teste=teste)


def user():
	#if request.args(0) == 'register':
    #    	db.auth_user.bio.writable = db.auth_user.bio.readable = False
	return response.render("initial/user.html", user=auth())

def register():
	return auth.register()

def login():
	return response.render("initial/login.html")

def account():
    return dict(register=auth.register(),
                login=auth.login())
	
def download():
	return response.download(request, db)



	



