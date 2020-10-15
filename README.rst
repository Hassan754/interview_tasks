Singularity
===========

Power Flow Calculator

Scalable and tested backend that makes use of Panda Power https://github.com/e2nIEE/pandapower
Calculates power flow and represents it through RESTful Api using DRF and graphql api using graphene

The main app lies inside backend_engineer_hassan/singularity/flow_app

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

``POST : /api/flow/`` Click "POST" button. This will trigger the calculation , save the values in db + cache them and return the response

``GET : /api/flow/active`` This will get from cache or db if unavailable the last calculated active power value

``GET : /api/flow/reactive`` This will get from cache or db if unavailable the last calculated reactive power value

``GET : /graphql/`` Graphql interface

.. code-block:: python

        mutation {
              calculatePower {
                active
                reactive
              }
            }

        query {
            getActive {
                value
                }
            }
        query {
            getReactive {
                value
                }
            }
