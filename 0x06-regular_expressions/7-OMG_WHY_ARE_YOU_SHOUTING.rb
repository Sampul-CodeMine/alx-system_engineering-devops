#!/usr/bin/env ruby
# Regular expression to match only CAPITALIZED alphabets
puts ARGV[0].scan(/[A-Z]/).join
