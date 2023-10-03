#!/usr/bin/env ruby
# This script matches a 10 digit number. no spaces.

puts ARGV[0].scan(/^\d{10}$/).join
