Docker Engine
=============

Install Docker Engine and Docker Compose.

Features
--------

- Settings to make [docker-bench-security](https://github.com/docker/docker-bench-security) happy.
- Change data root (`/var/lib/docker`) location.
- Login into docker registries.

Requirements
------------

- Debian

Role Vars
---------

**[defaults/main.yml](defaults/main.yml)**

Example
-------

```yaml
    docker_engine_data_root: /mnt/volume
    docker_engine_auditd: yes
    docker_engine_no_new_privileges: yes
    docker_engine_icc: no
    docker_engine_login:
      - registry_url: https://url1.com
        username: username1
        password: password1
      - registry_url: https://url2.com
        username: username2
        password: password2
```
