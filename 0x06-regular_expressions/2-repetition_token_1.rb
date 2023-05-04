#!/usr/bin/env ruby
# Regular expression to match a pattern in an expression
# that could be optional
puts ARGV[0].scan(/h[b]?tn/).join
