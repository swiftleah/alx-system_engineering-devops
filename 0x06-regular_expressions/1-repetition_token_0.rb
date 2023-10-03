#!/usr/bin/env ruby
# This script matches 'hbttn' where t can occur between 2 and 5 times

puts ARGV[0].scan(/hbt{2,5}n/).join
