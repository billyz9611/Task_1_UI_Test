import pytest
from parameterized import parameterized
from seleniumbase import BaseCase
from .markets_page_objects import MarketsPage, TradePage

BaseCase.main(__name__, __file__)


class MarketsTestClass(BaseCase):

    @parameterized.expand([['CRO', 'BTC'], ['ZIL', 'USDT']])
    @pytest.mark.markets
    def test_markets_page_go_to_trade_page(self, main_token, base_token):
        self.maximize_window()
        self.open(MarketsPage.url)
        self.wait_for_element(MarketsPage.token_pair_list_table)
        self.click(MarketsPage.tab(base_token))
        self.wait_for_element(MarketsPage.pair_token_link(main_token, base_token))
        self.click(MarketsPage.trade_button(main_token, base_token))
        self.wait_for_element(TradePage.pair_token_toggle)
        current_url = self.get_current_url()
        expect_url = '{}_{}'.format(main_token, base_token)
        assert current_url.endswith(expect_url), f'current_url is {current_url} bu expect endwith {expect_url}'
        self.assert_text('{}/{}'.format(main_token, base_token), TradePage.pair_token_toggle)
        self.assert_element(TradePage.order_book)
        self.assert_element(TradePage.trading_history)
        self.assert_element(TradePage.trade_box)
