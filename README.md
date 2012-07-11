OpenSlides
==========

Dies ist eine für den Landesverband Mecklenburg-Vorpommern angepasste Version von OpenSlides (http://openslides.org). OpenSlides

Anpassen
--------

Die Version kann mit dem Nutzernamen "root" und dem Passwort "asdfg" beliebig angepasst werden.

Installation
------------

Für den Landesparteitag 2012.1 wurde diese Version unter http://openslides.piraten-mv.de gehostet. Dazu wurden die Dateien in einen Ordner `/projects/openslides` kopiert und der Apache mit

    NameVirtualHost openslides.piratenpartei-mv.de
    NameVirtualHost openslides.piraten-mv.de

    <VirtualHost openslides.piratenpartei-mv.de:80>
        ServerName  openslides.piratenpartei-mv.de:80
        ServerAdmin webmaster@piraten-mv.de

        DocumentRoot /projects/openslides
        Alias /static /projects/openslides/openslides/static
        <Directory /projects/openslides>
            Order allow,deny
            Allow from all
        </Directory>

        WSGIDaemonProcess openslides.djangoserver processes=2 threads=15 display-name=%{GROUP}
        WSGIProcessGroup openslides.djangoserver
        WSGIPassAuthorization On
        WSGIScriptAlias / /projects/openslides/openslides/apache/django.wsgi

        # Logging
        LogLevel warn
        ErrorLog /var/log/apache2/openslides_error.log
        CustomLog /var/log/apache2/openslides.log combined
    </VirtualHost>

    <VirtualHost openslides.piraten-mv.de:80>
      ServerName openslides.piraten-mv.de:80
      ServerAdmin webmaster@piraten-mv.de

      RedirectMatch permanent ^(.*)$ http://openslides.piratenpartei-mv.de$1
    </VirtualHost>

konfiguriert.

Lizenz
------

OpenSlides ist Freie Software und steht unter der GNU General Public License (GNU GPL) Version 2+. Die Software darf ohne Restriktionen (unter den Bedingungen der Lizenz) benutzt, verändert und (geändert) weitergegeben werden. Eine Kopie der Lizenz liegt jedem OpenSlides-Release bei und ist auch in der LICENSE-Datei im Quellcode-Repository nachzulesen.
