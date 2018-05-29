BDOC-db ( *Black Desert Online Community, database module* ) 
============================================================

.. image:: https://img.shields.io/github/issues/RealImperialGames/BDOC-db.svg
  :alt: Issues on Github
  :target: https://github.com/RealImperialGames/BDOC-db/issues

.. image:: https://img.shields.io/github/issues-pr/RealImperialGames/BDOC-db.svg
  :alt: Pull Request opened on Github
  :target: https://github.com/RealImperialGames/BDOC-db/issues

.. image:: https://img.shields.io/github/release/RealImperialGames/BDOC-db.svg
  :alt: Release version on Github
  :target: https://github.com/RealImperialGames/BDOC-db/releases/latest

.. image:: https://img.shields.io/github/release-date/RealImperialGames/BDOC-db.svg
  :alt: Release date on Github
  :target: https://github.com/RealImperialGames/BDOC-db/releases/latest


Just module to allow to **BDOC-db** handle *database installation and setup*

PREREQUISITES
-------------

+ 1. Need to install Docker for windows : https://download.docker.com/win/stable/DockerToolbox.exe


How to install ?
----------------

+ 1. *PREREQUISITES*
+ 2. Install from setup.py file : ``python setup.py install``


How to exec tests ?
-------------------

+ 1. *PREREQUISITES*
+ 2. Tests from setup.py file : ``python setup.py test``


How to **start** DB ?
---------------------

+ 1. *PREREQUISITES*
+ 2. *Clone this repo* : ``git clone http://ntz-git.tk/IG/BDO-database.git``
+ 3. *Enter on repo directory* : ``cd BDO-database``
+ 4. *cd to bdodatabase/data/docker and* **start mongodb database with** : ``docker-compose up``


Configuration File
------------------

::

    {
      "TODO":"TODO"
    }



Contributing
~~~~~~~~~~~~

We welcome contributions to BDOC-db! These are the many ways you can help:

* Submit patches and features
* Make BDOC-db ( *new updates for database configuration or queries* )
* Improve the documentation for BDOC-db_
* Report bugs 
* And Donate bdoc-donate_ !

Please read our **documentation** to get started. Also note that this project
is released with a code-of-conduct_ , please make sure to review and follow it.


.. _BDOC-db: https://realimperialgames.github.io/BDOC-db
.. _bdoc-donate: https://opencollective.com/BDOC-db
.. _code-of-conduct: https://github.com/RealImperialGames/BDO-community/blob/master/CODE_OF_CONDUCT.rst