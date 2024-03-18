Feature: scenarios for markets

  Background: On Markets Page
    Given Open the Markets Page

  Scenario: check trade item show in table
    When Click USDT Tab
    Then Show ZIL_USDT
    When click trade button for ZIL/USDT
    Then show trade page for ZIL/USDT


