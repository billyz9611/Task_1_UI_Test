Feature: scenarios for markets

  Background: On Markets Page
    Given Open the Markets Page

  Scenario Outline: go to trade page through click trade button on markets page
    When Click <base_token> Tab
    Then Show <main_token> trade item in table
    When click <main_token> trade button
    Then go to <main_token> trade page
    Then assert items on trade page

    Examples: Tokens
      | base_token | main_token |
      | BTC        | CRO        |
      | USDT       | ZIL        |


