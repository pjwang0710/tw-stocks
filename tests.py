import os
import pytest
from requests.exceptions import HTTPError
from tw_stocks import TWStocks


def test_invalid_token_raises_HTTPError():
    stocks = TWStocks('invalid token')
    pytest.raises(HTTPError, lambda: stocks.get_cash_flow_statement('1101', '2021-01-01'))


@pytest.fixture(scope='module', params=[{}])
def stocks(request):
    return TWStocks(os.environ['TWSTOCKS_SECRET_KEY'], **request.param)


def test_get_cash_flow_statement(stocks):
    result = stocks.get_cash_flow_statement('1101', '2021-01-01')
    assert result[0].get('CMKey') == '1101'


def test_get_balance_sheet(stocks):
    result = stocks.get_balance_sheet('1101', '2021-01-01')
    assert result[0].get('CMKey') == '1101'


def test_get_financial_ratios(stocks):
    result = stocks.get_financial_ratios('1101', '2021-01-01')
    assert result[0].get('CMKey') == '1101'


def test_get_income_statement(stocks):
    result = stocks.get_income_statement('1101', '2021-01-01')
    assert result[0].get('CMKey') == '1101'


def test_get_k_image(stocks):
    result = stocks.get_k_image('1101', '2021-01-01')
    assert result[0].get('CMKey') == '1101'


def test_get_per_and_pbr(stocks):
    result = stocks.get_per_and_pbr('1101', '2021-01-01')
    assert result[0].get('CMKey') == '1101'


def test_get_reinvestment(stocks):
    result = stocks.get_reinvestment('1101', '2021-01-01')
    assert result[0].get('CMKey') == '1101'


def test_get_stock_basic_info(stocks):
    result = stocks.get_stock_basic_info('1101')
    assert result[0].get('CMKey') == '1101'


def test_get_stock_name(stocks):
    result = stocks.get_stock_name('1101')
    assert result[0].get('CMKey') == '1101'


def test_get_stock_revenue_surplus(stocks):
    result = stocks.get_stock_revenue_surplus('1101', '2021-01-01')
    assert result[0].get('CMKey') == '1101'


def test_get_trader_sum(stocks):
    result = stocks.get_trader_sum('1101', '2021-01-01')
    assert result[0].get('CMKey') == '1101'


def test_invalid_cmkey(stocks):
    result = stocks.get_trader_sum('abcde', '2021-01-01')
    assert len(result) == 0


def test_invalid_date(stocks):
    pytest.raises(ValueError, lambda: stocks.get_trader_sum('1101', '20210101'))
