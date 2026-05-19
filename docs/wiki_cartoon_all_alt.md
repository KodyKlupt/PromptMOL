# Cartoon all alt

The cartoon_all_alt setting activates cartoon for alternative coordinates. There will be one cartoon geometry per alt-code. The default (**off**) is to only render a single cartoon where only the first alt code is considered.

- New in PyMOL 1.8.4*

##  Example
 fetch 5a0d, async=0
 spectrum alt
 as cartoon

 set cartoon_all_alt
