from seeded_bugs.demo_app.inventory_stock import add_stock, reserve_stock

# NOTE: this only checks sequential behavior. A plain single-threaded
# test like this one can't reliably demonstrate the race condition the
# buggy branch introduces (that needs real concurrent callers) - which
# is exactly why this class of bug is the hardest of the four to catch
# by testing alone, and often only surfaces under real production load.


def test_reserve_stock_never_goes_negative():
    add_stock("widget", 5)

    assert reserve_stock("widget", 5) is True
    assert reserve_stock("widget", 1) is False
