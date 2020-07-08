def test_compose_binary(host):
     compose = host.file("/usr/local/bin/docker-compose")
     assert compose.user == "root"
     assert compose.group == "root"
     assert compose.mode == 0o755