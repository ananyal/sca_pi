#!/bin/bash

#initial value of counter is set to 3
car=3

while [ $car -le 21 ]
    do
        echo $car
        ((car = $car + 3))
done

echo "All done"
