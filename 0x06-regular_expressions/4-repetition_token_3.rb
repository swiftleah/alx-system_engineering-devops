#!/usr/bin/env ruby
# This scirpt matches 'hbn' where t can occur 0 or more times

puts ARGV[0].scan(/hbt*n/).join
