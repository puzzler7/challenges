#!/usr/bin/env python3

flag = b"ictf{I_really_hope_this_ends_up_being_the_right_amount_of_complicated}"

ret = f"my_int ct[{len(flag)}] = {{"

for c in flag:
    ret += "my_int(%d), "%(c^0x42)

ret += '}';
print(ret)