#!/bin/sh
# bash one-liner
# Returns the list items needed to construct a module's __all__ list .
# Call example: $ cat module.py | . get_module__all__.sh
#

sed -n  "/^[def]/ {/^from/ d; /^del/ d; s/:$//; s/$/\',/; /__/ d; s/([^(]*)//I; s/^def /\'/; p}" $1
