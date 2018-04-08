import pytest

from csv_parser.storage import get_words

@pytest.mark.parametrize('src,res',(
    ('beet', ['beet']),
    ('beet;', ['beet']),
    ('fresh beet', ['fresh', 'beet']),
    ('   fresh   beet  ', ['fresh', 'beet']),
    ('beet   fresh.  ', ['beet', 'fresh']),
    ('beet ,  fresh. ', ['beet', 'fresh']),
    (', fresh. beet', ['fresh', 'beet']),
))
def test_get_words(src, res):

    aliases = get_words(src)

    assert res == aliases
