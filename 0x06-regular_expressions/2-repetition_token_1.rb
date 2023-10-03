#!/usr/bin/env ruby
# This script matches 'hbtn' where b can occur 0 or 1 times

puts ARGV[0].scan(/hb?tn/).join
