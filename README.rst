Singularity
===========

Power Flow Calculator

Scalable and tested backend that makes use of Panda Power https://github.com/e2nIEE/pandapower
Calculates power flow and represents it through RESTful Api using DRF

Basic Commands
--------------

Build up the project
^^^^^^^^^^^^^^^^^^^^^

* To build the project , make sure you're on the same path as local.yml , use this command

::

    $ docker-compose -f local.yml build

* To migrate the db

::

    $ docker-compose -f local.yml run django python manage.py migrate

* Then use this command to bring the project up

::

    $ docker-compose -f local.yml up

For convenience, you can set the environment variable COMPOSE_FILE pointing to local.yml like this

::

    $ export COMPOSE_FILE=local.yml

This way , you can run

::

  $ docker-compose up

The project should be running on http://0.0.0.0:8000/


Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ docker-compose run django pytest


Using the Api
~~~~~~~~~~~~~~~~~~~~~~~~~~
There are 3 Endpoints , you can navigate them by the browser UI on the urls :

``POST : /api/flow/`` This will trigger the calculation , save the values in db and return the response

``GET : /api/flow/active`` This will get from db the last calculated active power value

``GET : /api/flow/reactive`` This will get from db the last calculated reactive power value

