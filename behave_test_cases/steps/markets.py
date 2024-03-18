from behave import step
from seleniumbase import BaseCase


@step("Open the Markets Page")
def go_to_markets(context):
    sb: BaseCase = context.sb
    sb.maximize_window()
    sb.open("https://crypto.com/exchange/markets")


@step("Click {tab_name} Tab")
def click_tab(context, tab_name):
    sb: BaseCase = context.sb
    sb.wait_for_element('.table__body')
    selector_txt = '//span[text()="%s"]' % tab_name
    sb.wait_for_element(selector_txt)
    sb.click(selector_txt)
    sb.variables['base_token'] = tab_name


@step("Show {trade_coin_name:S} trade item in table")
def check_trade_items(context, trade_coin_name):
    sb: BaseCase = context.sb
    sb.scroll_to_bottom()
    selector_txt = 'a[href*="{}_{}"]'.format(trade_coin_name, sb.variables['base_token'])
    sb.wait_for_element(selector_txt)
    sb.focus(selector_txt)


@step("click {trade_coin_name} trade button")
def click_trade_button(context, trade_coin_name):
    sb = context.sb
    sb.click('tr.tbody__row:contains("{}/{}") button.btn-trade'.format(trade_coin_name, sb.variables['base_token']))


@step("go to {trade_coin_name:S} trade page")
def go_to_trade_page(context, trade_coin_name):
    sb: BaseCase = context.sb
    sb.wait_for_element("div.toggle", timeout=200)
    sb.assert_text("{}/{}".format(trade_coin_name, sb.variables['base_token']), "div.toggle")


@step("assert items on trade page")
def check_trade_page(context):
    sb: BaseCase = context.sb
    sb.assert_text("Order Book", ".order-book-title")  # check Order Book show in page
    sb.assert_text("Trading History", ".trade-history-title")  # check Trading History show in page
    # sb.assert_element(".chart-gui-wrapper")  # check chart  show in page
    sb.assert_element(".trade-box")  # check trade box show in page