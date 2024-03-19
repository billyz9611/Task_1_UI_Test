class MarketsPage(object):
    url = "https://crypto.com/exchange/markets"
    token_pair_list_table = '.table__body'

    @staticmethod
    def tab(base_token):
        return '//span[text()="%s"]' % base_token

    @staticmethod
    def pair_token_link(main_token, base_token):
        return 'a[href*="{}_{}"]'.format(main_token, base_token)

    @staticmethod
    def trade_button(main_token, base_token):
        return 'tr.tbody__row:contains("{}/{}") button.btn-trade'.format(main_token, base_token)


class TradePage(object):
    pair_token_toggle = "div.toggle"
    order_book = ".order-book-title"
    trading_history = ".trade-history-title"
    chart = ".chart-gui-wrapper"
    trade_box = ".trade-box"
