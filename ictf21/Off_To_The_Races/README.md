# Off To The Races!

**Category:** Misc
**Difficulty:** Easy/Medium
**Author:** puzzler7

## Description

They say that gambling leads to regrets, but we'll see. This online portal lets you bet on horse races, and if you can guess the admin password, you can collect all the money people lose, too. Maybe you'll collect enough to buy the flag?

## Distribution

races.py, netcat

## Deploy notes

Host so that people can connect to races.py, with flag.txt in the directory. Will make a dockerfile soon(tm).

## Solution

The regex for the password can be reduced to the simpler `ju5tn((eve)+eve)+rl05e`, where the `e` can be replaced with any of e, E, or 3. The money for the flag can be easily collected by betting $100 on 3 different horses, so that one will win, and two will lose, causing a net payment of $100 to the admin.

The most difficult part of the challenge is that admins can't view the flag. However, non-admins can't access the view flag option. The solution is to use the race condition on validating the password. If you login as admin, then enter an incorrect password that takes more than 2 seconds to validate, the admin menu will pop up before you are logged out. Once you are logged out, you can enter the view flag portion as a non-admin.

In order to accomplish this, you can use the catastrophic backtracking vuln in the regex. By repeating the `eve` part of the password, and removing the `r`, you can submit an invalid password that validates in exponential time. The password I used was `ju5tneveeveeveeveeveeveeveeveeveeveeveeveeveeveeveeveeveeveeveeveeveeveeveeveeveeveeveeveeveeveeveeveeveeveeveeveevel05e` to have the login failure pop up a few seconds after the menu. The delay will approximately double with each `eve` added.

In summary:
* Place 3 bets for $100
* Login as admin
* Declare a winner
* Logout with the invalid password above
* Wait until the "Login Failure" pops up, then view the flag.
