import pytest

from pyramid import testing


def test_detail():
    from learning_journal.views import detail
    request = testing.DummyRequest()
    info = detail(request)
    # import pdb; pdb.set_trace()
    assert 'title' in info['entries'][0]


@pytest.fixture()
def testapp():
    from learning_journal import main
    app = main({})
    from webtest import TestApp
    return TestApp(app)


def test_layout_root(testapp):
    response = testapp.get('/', status=200)
    assert b'owner: Tatiana Weaver' in response.body


def test_root_contents(testapp):
    from learning_journal.views import ENTRIES
    response = testapp.get('/', status=200)
    html = response.html
    assert len(ENTRIES) == len(html.findAll('article'))
