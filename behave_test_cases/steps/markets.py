from behave import step
from seleniumbase import BaseCase


@step("Open the Markets Page")
def go_to_markets(context):
    sb = context.sb
    sb.open("https://crypto.com/exchange/markets")


@step("Click {tab_name} Tab")
def click_tab(context, tab_name):
    sb: BaseCase = context.sb
    selector_txt = '//span[text()="%s"]' % tab_name
    sb.wait_for_element(selector_txt)
    sb.click(selector_txt)


@step("Show {trade_coin_name:S}")
def check_trade_items(context, trade_coin_name):
    sb: BaseCase = context.sb
    sb.scroll_to_bottom()
    selector_txt = 'a[href*="{}"]'.format(trade_coin_name)
    sb.wait_for_element(selector_txt)
    sb.focus(selector_txt)


@step("click trade button for {trade_coin_name}")
def click_trade_button(context, trade_coin_name):
    sb = context.sb
    sb.click('tr.tbody__row:contains("{}") button.btn-trade'.format(trade_coin_name))


@step("show trade page for {trade_coin_name:S}")
def check_trade_page(context, trade_coin_name):
    sb = context.sb
    sb.wait_for_element("div.toggle")
    sb.assert_text(trade_coin_name, "div.toggle")
