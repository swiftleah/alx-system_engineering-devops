#!/usr/bin/env ruby
# This script accepts one argument & passes it to regular expression matching method 'School'

puts ARGV[0].scan(/School/).join
