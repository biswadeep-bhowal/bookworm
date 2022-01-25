from django.shortcuts import render

def home( request ) : 
    
    context = {
        'first' :   [ i for i in range( 1, 13 ) ],
        'second' :  [ i for i in range( 13, 19 ) ],
        'third' :   [ i for i in range( 19, 31 ) ],
        'fourth' :  [ i for i in range( 31, 37 ) ]
    }
    
    return render( request, 'home.html', context )