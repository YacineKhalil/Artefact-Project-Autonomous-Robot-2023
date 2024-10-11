from bottle import route, run, static_file, request
import stocke_donnees as stkd

@route('/static/site_joystick')
def serve_homepage():
    return static_file('site_joystick.html', root='./static')
    
@route('/static/javascript')
def serve_javascript():
    return static_file('site_joystick.js', root='./static/')
    
@route('/static/image_joystick')
def serve_image_joystick():
    return static_file('image_joystick_walle.jpg', root='./static/')
    
@route('/static/css')
def serve_css():
    return static_file('site_joystick.css', root='./static/')

@route('/envoie_donnees', method='POST')
def envoyer_donnees():
    x_y = request.POST.get('x_y')
    R = request.POST.get('R')
    isAuto = request.POST.get('isAuto')
    if x_y!="" and R!="" and isAuto!= None:           #debug : si la requête POST saute
        stkd.stocke_donnees(x_y,R,isAuto)
    return
    
run(host='0.0.0.0', port=8080, debug=True)