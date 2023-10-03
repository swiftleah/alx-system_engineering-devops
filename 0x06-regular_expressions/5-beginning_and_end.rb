#!/usr/bin/env ruby
# This script matches 'hn' where there must be one letter between h and n

puts ARGV[0].scan(/^h[a-z]n$/).join
