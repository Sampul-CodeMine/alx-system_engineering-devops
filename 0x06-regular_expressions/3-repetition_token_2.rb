#!/usr/bin/env ruby
# Regular expression to match a particular character in an expression
# that could be repeated one or more times
puts ARGV[0].scan(/hb[t]+n/).join
