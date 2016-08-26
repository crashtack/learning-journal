import pytest
from learning_journal.views import detail
from pyramid import testing
from pyramid.httpexceptions import (HTTPNotFound, HTTPFound)




# TODO: parametrize this test for value in the actual journal data
def test_detail():
    from learning_journal.views import detail
    request = testing.DummyRequest()
    request.matchdict["id"] = 3
    info = detail(request)
    # import pdb; pdb.set_trace()
    assert 'title' in info['entry']


# TODO: parametrize this test for value in the actual journal data
def test_detail():
    from learning_journal.views import detail
    request = testing.DummyRequest()
    request.matchdict["id"] = 3
    info = detail(request)
    # import pdb; pdb.set_trace()
    assert 'Day 3' == info['entry']['title']


def test_detail_not_found():
    request = testing.DummyRequest()
    with pytest.raises(HTTPNotFound):
        request.matchdict["id"] = 3


@pytest.fixture()
def testapp():
    from learning_journal import main
    app = main({})
    from webtest import TestApp
    return TestApp(app)


def test_layout_root(testapp):
    response = testapp.get('/', status=200)
    assert b'<p>David Banks</p>' in response.body


def test_root_contents(testapp):
    from learning_journal.views import ENTRIES
    response = testapp.get('/', status=200)
    html = response.html
    assert len(ENTRIES) == len(html.findAll('article'))
