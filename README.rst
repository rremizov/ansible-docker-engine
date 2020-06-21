.. sectnum::

Docker Engine
=============

Install Docker Engine and Docker Compose.

Requirements
------------

- Debian

Role Vars
---------

``docker_engine_data_root``
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Root directory of persistent Docker state (`docker docs`_). Default: ``/var/lib/docker``.

``docker_engine_login``
~~~~~~~~~~~~~~~~~~~~~~~

A list of docker registries to login. See the schema in the examples.

``docker_engine_bench_security_enabled``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Enable to run `docker-bench-security`_ daily. Default: ``no``.

``docker_engine_icc``
~~~~~~~~~~~~~~~~~~~~~

Enable inter-container communication. Default: ``yes``.

``docker_engine_auditd``
~~~~~~~~~~~~~~~~~~~~~~~~

Enable to configure auditd. Default: ``no``.

Example
-------

.. code:: yaml

    docker_engine_login:
      - registry_url: https://url1.com
        username: username1
        password: password1
      - registry_url: https://url2.com
        username: username2
        password: password2

.. _docker docs: https://docs.docker.com/engine/reference/commandline/dockerd/
.. _docker-bench-security: https://github.com/docker/docker-bench-security
