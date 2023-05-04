#!/usr/bin/env ruby
# Regular expression to match a particular pattern which must start with
# `h` and end with `n` but must have only a single character in between
puts ARGV[0].scan(/h.n/).join
