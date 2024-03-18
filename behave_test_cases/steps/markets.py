from behave import step


@step("Open the Markets Page")
def go_to_markets(context):
    sb = context.sb
    sb.open("https://crypto.com/exchange/markets")


@step("Click {tab_name} Tab")
def click_tab(context, tab_name):
    sb = context.sb
    sb.click('//span[text()="%s"]' % tab_name)


@step("Show {trade_coin_name:S}")
def check_trade_items(context, trade_coin_name):
    sb = context.sb
    sb.scroll_to_bottom()
    select_txt = 'a[href*="{}"]'.format(trade_coin_name)
    sb.assert_element(select_txt)
    sb.focus(select_txt)


@step("click trade button for {trade_coin_name}")
def click_trade_button(context, trade_coin_name):
    sb = context.sb
    sb.click('tr.tbody__row:contains("{}") button.btn-trade'.format(trade_coin_name))


@step("show trade page for {trade_coin_name:S}")
def check_trade_page(context, trade_coin_name):
    sb = context.sb
    sb.assert_text(trade_coin_name, "div.toggle")
