+++++ set values to multiply
>++<

[ 0 multiplier loop
    > 1
    [ copy multiplied value twice
        >+ 2
        >+ 3
        <<- 1
    ]
    >> 3
    [ move value from 4 to 2 pos to complete copy
        <<+ 1
        >>- 3
    ]
    <<[ 1 add first multiply to final counter
        >>>+ 4
        <<<- 1
    ]
    <- 0 subtract from multiply counter
    >>[ 2
        <+ 1
        >- 2
    ]
    << 0 return to start
]
>>>>.
