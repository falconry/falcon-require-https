import falcon
from falcon import testing
import pytest

from falcon_require_https import RequireHTTPS


_TEST_PATH = '/https'


@pytest.fixture()
def simulate():
    app = falcon.API(middleware=[RequireHTTPS()])
    app.add_route(_TEST_PATH, testing.SimpleTestResource())

    def simulate(protocol, headers=None):
        env = testing.create_environ(
            method='GET',
            scheme=protocol,
            path=_TEST_PATH,
            query_string='',
            headers=headers,
        )

        srmock = testing.StartResponseMock()
        iterable = app(env, srmock)

        return testing.Result(iterable, srmock.status, srmock.headers)

    return simulate


@pytest.mark.parametrize('protocol', ['https', 'HTTPS', 'hTTpS'])
def test_allow_https(simulate, protocol):
    result = simulate(protocol)
    assert result.status_code == 200


@pytest.mark.parametrize('protocol', ['http', 'HTTP', 'hTTp'])
def test_disallow_http(simulate, protocol):
    result = simulate(protocol)
    assert result.status_code == 400


@pytest.mark.parametrize('protocol', ['https', 'HTTPS', 'hTTpS'])
def test_allow_https_forwarded_proto(simulate, protocol):
    result = simulate('http', headers={'X-Forwarded-Proto': protocol})
    assert result.status_code == 200


@pytest.mark.parametrize('protocol', ['http', 'HTTP', 'hTTp'])
def test_disallow_http_forwarded_proto(simulate, protocol):
    result = simulate('http', headers={'X-Forwarded-Proto': protocol})
    assert result.status_code == 400


def test_precedence_of_forwarded_over_forwarded_proto(simulate):
    result = simulate('http', headers={
        'X-Forwarded-Proto': 'http',
        'Forwarded': 'proto=https'
    })
    assert result.status_code == 200


@pytest.mark.parametrize('forwarded', [
    'proto=https',
    'for=client;proto=https,proto=http',
    'for=192.0.2.60;proto=https;by=203.0.113.43, by=203.0.113.43;proto=http',
])
def test_allow_https_forwarded(simulate, forwarded):
    result = simulate('http', headers={'Forwarded': forwarded})
    assert result.status_code == 200


@pytest.mark.parametrize('forwarded', [
    'proto=http',
    'for=client,proto=https',  # First hop doesn't specify HTTPS
    'for=client;proto=http,proto=https',
    'for=192.0.2.60;proto=http;by=203.0.113.43, by=203.0.113.43;proto=https',
])
def test_disallow_http_forwarded(simulate, forwarded):
    result = simulate('http', headers={'Forwarded': forwarded})
    assert result.status_code == 400
