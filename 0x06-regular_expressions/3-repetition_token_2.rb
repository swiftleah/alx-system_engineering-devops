#!/usr/bin/env ruby
# This script matches 'hbtn' where t can occur 1 or more times

puts ARGV[0].scan(/hbt+n/).join
