0x06. Regular expression
This project is a deep dive into Ruby Regular expression.

A regular expression, commonly called a “regexp”, is a sequence of characters that define a search pattern. It is mainly for use in pattern matching with strings, or string matching (i.e. it operates like a “find and replace” command). While it is a very powerful tool, it is also very dangerous because of its complexity.

Background Context;

I used this project to build my 'regular expression' using "Oniguruma", a regular expression library that which is used by Ruby by default.

N/B Other regular expression libraries sometimes have different properties.

Because the focus of this exercise is to play with regular expressions (regex), I just replaced the regexp part. (that is the code in between the //:) Below is the Ruby code that was used;

sylvain@ubuntu$ cat example.rb #!/usr/bin/env ruby puts ARGV[0].scan(/127.0.0.[0-9]/).join sylvain@ubuntu$ sylvain@ubuntu$ ./example.rb 127.0.0.2 127.0.0.2 sylvain@ubuntu$ ./example.rb 127.0.0.1 127.0.0.1 sylvain@ubuntu$ ./example.rb 127.0.0.a

The following files created to execute the following functions;

0-simply_match_school.rb - creates a Ruby script that accepts one argument and pass it to a regular expression matching method using a given instructions.

1-repetition_token_0.rb - ""

2-repetition_token_1.rb - ""

3-repetition_token_2.rb - ""

4-repetition_token_3.rb - ""

5-beginning_and_end.rb - ""

6-phone_number.rb - Creates a regular expression that matches a "10 digits phone number".

7-OMG_WHY_ARE_YOU_SHOUTING.rb - Creates a regular expression that only matches "capital letters".

100-textme.rb - Creates a script that outputs: [SENDER],[RECEIVER],[FLAGS] -The sender phone number or name (including country code if present) -The receiver phone number or name (including country code if present) -The flags that were used.
