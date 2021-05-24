# Projecte M12 - Portal Aplicacions




## Instal·lació
Clonar el repositori amb `git clone https://github.com/davidruiztornes/M12-Portal-Aplicacions.git `.\
Crear un entorn virtual amb virtualenv `virtualenv env`.\
Executar `.\env\Scripts\activate` per activar entorn virtual.\
Executar `pip install -r requirements.txt` per instal·lar totes les dependències.\
Executar `python manage.py makemigrations` i `python manage.py migrate`.
Finalment executar `python manage.py runserver` per iniciar el projecte.

### Administració 
Es pot accedir a la seccio d'Administració desde http://127.0.0.1:8000/admin/ \
Usuari: admin Contrasenya: 12345 

Es pot generar un nou administrador amb `python createsuperuser`.


## Desenvolupat amb 🛠️

### Frontend:
 * LLenguatges: HTML5,CSS i JavaScript
 
### Backend:
 * [Django](https://www.djangoproject.com/) - Framework Python per desenvolupar aplicacions web.
> #### Paquets 
* [django-Allauth](https://django-allauth.readthedocs.io/en/latest/overview.html) - Mètode per permetre l'autenticació desde serveis socials(google,github,etc..)
* [crispy-form](https://django-crispy-forms.readthedocs.io/en/latest/) - Permet afegir format als formularis de django.
* [xhtml2pdf](https://xhtml2pdf.readthedocs.io/en/latest/) - Permet generar fitxers pdf a partir de plantilles html.

## Wiki 📖

Pots trobar més informació d'aquest projecte a la [Wiki](https://github.com/davidruiztornes/M12-Portal-Aplicacions/wiki)