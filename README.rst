Gallery - Photo Album Organizer
===============================

The `Gallery Project`_ is a web application enabling management and
publication of digital photographs and other media. Photo manipulation
features includes automatic thumbnails, resizing, rotation, and
flipping, among other things. Albums can be organized hierarchically and
individually controlled by administrators or privileged users.

This appliance includes all the standard features in `TurnKey Core`_,
and on top of that:

- Gallery configurations:
   
   - Installed from upstream source code to /var/www/gallery.
   - Preconfigured gallery to use webroot and database.
   - Includes support for URL rewriting.
   - Includes ffmpeg for video support.

- SSL support out of the box.
- `Adminer`_ administration frontend for MySQL (listening on port
  12322 - uses SSL).
- Postfix MTA (bound to localhost) to allow sending of email (e.g.,
  password recovery).
- All secrets will be regenerated during installation / firstboot
  (security).
- Webmin modules for configuring Apache2, PHP, MySQL and Postfix.

Credentials *(passwords set at first boot)*
-------------------------------------------

- Webmin, Webshell, SSH, MySQL: username **root**
- Gallery: username **admin**


.. _Gallery Project: http://gallery.menalto.com
.. _TurnKey Core: https://www.turnkeylinux.org/core
.. _Adminer: http://www.adminer.org/
