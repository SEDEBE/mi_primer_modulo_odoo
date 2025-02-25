#__manifest__.py
{
     'name': 'Mi primer modulo personalizado',
     'version':'1.0',
     'category':'Custom',
     'author':'Alejandro Cordoba Perez',
     'summary':'Mi primer modulo custom para Odoo',
     'depends':['base'],
     'data':[
         'views/mi_modulo_view.xml',
     ],
     'installable': True,
     'application': True,
    
}