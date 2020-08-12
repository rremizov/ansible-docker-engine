import json

import pytest


class TestDaemonJson:
    @pytest.fixture()
    def daemon_json(self, host):
        return host.file("/etc/docker/daemon.json")

    @pytest.fixture()
    def daemon_json_content(self, daemon_json):
        return daemon_json.content_string

    def test_readable_by_root_only(self, daemon_json):
        assert daemon_json.user == "root"
        assert daemon_json.group == "root"
        assert oct(daemon_json.mode) == "0o640"

    def test_is_valid_json(self, daemon_json_content):
        json.loads(daemon_json_content)

    @pytest.mark.parametrize(
        "config_option", ["no-new-privileges", "icc", "userland-proxy"]
    )
    def test_booleans(self, daemon_json_content, config_option):
        assert isinstance(json.loads(daemon_json_content)[config_option], bool)


class TestDockerService:
    def test_is_enabled(self, host):
        assert host.service("docker").is_enabled

    def test_is_running(self, host):
        assert host.service("docker").is_running
