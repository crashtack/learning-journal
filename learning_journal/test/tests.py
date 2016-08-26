import pytest
from learning_journal.views import detail
from pyramid import testing
from pyramid.httpexceptions import (HTTPNotFound, HTTPFound)

TABLE = [
    (1, 'title', 'Day 1'),
    (2, 'title', 'Day 2'),
    (3, 'title', 'Day 3'),
    (4, 'title', 'Day 4'),
]

ROUTES = [
    ('/', b'<p>David Banks</p>'),
    ('/journal/new-entry', b'<h1>new-entry.jinja2</h1>'),
    ('/journal/1', b'<h1>Day 1</h1>'),
    ('/journal/2', b'<h1>Day 2</h1>'),
    ('/journal/3', b'<h1>Day 3</h1>'),
    ('/journal/4', b'<h1>Day 4</h1>'),
    ('/journal/1/edit-entry', b'Entry ID: 1'),
    ('/journal/2/edit-entry', b'Entry ID: 2'),
    ('/journal/3/edit-entry', b'Entry ID: 3'),
    ('/journal/4/edit-entry', b'Entry ID: 4'),
]


@pytest.mark.parametrize('journal_id, word, result', TABLE)
def test_detail(journal_id, word, result):
    '''test the entries from the ENTRIES dictioniary are correct'''
    request = testing.DummyRequest()
    request.matchdict["id"] = journal_id
    info = detail(request)
    # import pdb; pdb.set_trace()
    assert word in info['entry']


@pytest.mark.parametrize('journal_id, word, result', TABLE)
def test_detail2(journal_id, word, result):
    '''Test the value for title is corretct for each entry in ENTRIES dictionay'''
    request = testing.DummyRequest()
    request.matchdict["id"] = journal_id
    info = detail(request)
    # import pdb; pdb.set_trace()
    assert result == info['entry']['title']


def test_detail_not_found():
    '''Testst that entry ID 30 does not exit and returns a HTTPNotFound error'''
    request = testing.DummyRequest()
    with pytest.raises(HTTPNotFound) as excinfo:
        request.matchdict["id"] = 30
    assert 'Entry Not Found' in str(excinfo)


@pytest.fixture()
def testapp():
    '''testapp fixture'''
    from learning_journal import main
    app = main({})
    from webtest import TestApp
    return TestApp(app)


@pytest.mark.parametrize('path, content', ROUTES)
def test_rendered_layouts(path, content, testapp):
    '''tests that a particular HTML binary string is in the response body'''
    response = testapp.get(path, status=200)
    assert content in response.body


def test_root_contents(testapp):
    '''Test that the # of rendered articles matches the # of entries in ENTRIES'''
    from learning_journal.views import ENTRIES
    response = testapp.get('/', status=200)
    html = response.html
    assert len(ENTRIES) == len(html.findAll('article'))
