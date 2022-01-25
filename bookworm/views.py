from django.shortcuts import render

def home( request ) : return render( request, 'home.html', { 'range' : [ i for i in range( 1, 41 ) ] } )