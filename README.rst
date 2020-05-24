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


``docker_engine_bench_security_enabled``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Enable to run `docker-bench-security`_ daily. Default: ``no``.


.. _docker docs: https://docs.docker.com/engine/reference/commandline/dockerd/
.. _docker-bench-security: https://github.com/docker/docker-bench-security
