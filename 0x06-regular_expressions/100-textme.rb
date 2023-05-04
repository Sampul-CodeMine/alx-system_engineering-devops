#!/usr/bin/env ruby
# Regular expression to do the following
# It should output [SENDER],[RECEIVER],[FLAGS] from a TextMe VoIP message
# Sender's phone number including country code if any'
#  Receiver's phone number including country code if any'
# the flag that was used.
puts ARGV[0].scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).join(',')
