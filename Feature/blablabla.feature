# Created by hodor at 19.04.19
Feature: Checking game creation and working
  Scenario: Checking game field creation
    Given I have my game class
    When I create new game
    Then I have created field with size 4x4 and numbers from 1 to 15 and one empty cell
#2
  Scenario: Checking game field down move
    Given I have created field
    When I do move down
    Then Cell above the zero cell move down and the zero cell move up
#3
  Scenario: Checking game field left move
     Given I have created field
     When I do left move
     Then Cell right from the zero cell move left and the zero cell move right

  Scenario: Checking game field right move
     Given I have created field
     When I do right move
     Then Cell left from the zero cell move right and the zero cell move left

  Scenario: Checking game field up move
     Given I have created field
     When I do up move
     Then Cell under the zero cell move up and the zero cell move down