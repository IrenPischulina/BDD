# Created by hodor at 19.04.19
Feature: Checking game creation and working
  Scenario: Checking game field creation
    Given I have my game class
    When I create new game
    Then I have created field with size 4x4 and numbers from 1 to 15 and one empty cell

  Scenario: Checking game field down move
    Given I have created field
    When I do move down
    Then Cell above the zero cell move down and the zero cell move up