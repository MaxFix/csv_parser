
from csv_parser.storage import Food


def test_food_method_init_aliases_01():
    f = Food('апельсин', '123 ккал')
    assert f.aliases_all == ['апельсин']


def test_food_method_init_aliases_02():
    f = Food('яблоко печеное', '123 ккал')
    assert f.aliases_all == ['яблоко', 'печеное']


def test_food_method_init_aliases_03():
    f = Food('слива черная сушеная.?*:\'*&^', '123 ккал')
    assert f.aliases_all == ['слива', 'черная', 'сушеная']


def test_food_method_init_aliases_without_state_changes():
    f = Food('слива черная сушеная.?*:\'*&^', '123 ккал')
    assert f.aliases_all == ['слива', 'черная', 'сушеная']

    assert f.name == 'слива черная сушеная.?*:\'*&^'


def test_food_method_has_alias():
    f = Food('слива черная сушеная', '123 ккал')

    assert f.has_alias('слива')
    assert f.has_alias('черная')
    assert f.has_alias('сушеная')

    assert not f.has_alias('вишня')
    assert not f.has_alias('красная')
    assert not f.has_alias('замороженная')

