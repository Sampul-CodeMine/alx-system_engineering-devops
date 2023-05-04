#!/usr/bin/env ruby
# Regular expression to match a particular character in an expression
puts ARGV[0].scan(/hb[t]{2,5}n/).join
