[
Initial comment loop
array setup:
0 vals_to_print 0 iters num_to_print curr_num 0
]

generated code to make ascii flag
>>>>+++++++++++[<+++++++++++>-]--[<-------->+]
>++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[<++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>-]-------[<---------------->+]
>++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[<++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>-]--[<----------------------------------------------------------->+]
>+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[<+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>-]-[<->+]
>++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[<++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>-]-----[<-------------------->+]
>++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[<++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>-]-[<-->+]
>++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[<++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>-]--[<----------------------------------------------------------------------------------->+]
>+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[<+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>-]------[<------------------->+]
>++++++++++++++++++++++++++++++++++++++[<++++++++++++++++++++++++++++++++++++++>-]-[<----------------------->+]
>+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[<+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>-]---[<------------------------------->+]
>++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[<++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>-]-------[<--------------------->+]
>++++++++++++++++++++++++++++++++++++++[<++++++++++++++++++++++++++++++++++++++>-]-[<--->+]
>++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[<++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>-]-[<->+]
>++++++++++++++++++++++++++++++++++++++++[<++++++++++++++++++++++++++++++++++++++++>-]--[<------------------------------------->+]
>+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[<+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>-]-----[<----------------->+]
>++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[<++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>-]--[<----------------------------------------------------------------------------------->+]
>+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[<+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>-]---------[<------------->+]
>++++++++++++++++++++++++++++++++++++[<++++++++++++++++++++++++++++++++++++>-]-[<--->+]
>++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[<++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>-]-----[<---------->+]
>++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[<++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>-]--[<-------->+]
>+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[<+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>-]--[<------------------------------------------------------------->+]
>+++++++++++++++++++++++++++++++++[<+++++++++++++++++++++++++++++++++>-]---[<---------------->+]
>++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[<++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>-]---[<------->+]
>+++++++++++++++++++++++++++++++++[<+++++++++++++++++++++++++++++++++>-]---[<------------->+]
>+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[<+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>-]--[<-------------------------------->+]
>+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[<+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>-]-[<----------------------------------------------------------------------------------->+]
>+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[<+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>-]-[<------------------------------------------------------------------------------------------------------->+]
>+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[<+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>-]-[<------------------------------------------------------------------------------------------------------------------------------------------->+]
>++++++++++++++++++++++++++++++++++++++[<++++++++++++++++++++++++++++++++++++++>-]-[<-->+]
>+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[<+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>-]-[<-->+]
>+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[<+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>-]---[<-------------------------------->+]
>++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[<++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>-]---[<------------------------>+]
>>++++++[<++++++>-]--[<-->+] 32 chars in flag
+ put 1 at num

<
[ while iters
    >[->+>++<<] copy double of num to curr and curr plus 1
    >>[-<<+>>] move curr plus 1 to num
    this ends at curr plus 1

    <[[<]<[<]>.[>]>[>]<-] go to value and print curr times
    [<]<[<]<[<]> travel to val
    [-<+<+>>]<<[->>+<<] copy to the left

    >>[ while first
        <[->>-<<] decrement second and val
        >-[-<+<+>>]<<[->>+<<]>> decrement first and copy to the left
    ]

    
    >>[>]>- go to iters and decrement
]