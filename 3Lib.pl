use strict;
use warnings;

my $Number = 10**5;
my $Randomtime =  10**8;
my @data = (0) x 5;

for (my $i = 0; $i < $Randomtime; $i++) {
    $data[int(rand($Number))]++;
}

open(my $fh, '>', 'data-3.txt');
for (my $i = 0; $i < $Number; $i++) {
    if (!$data[$i]) {
        $data[$i] = 0;
    }

    my $str = $i." ".$data[$i]."\n";

    #print($str);
    print $fh $str;
    #print($i." ".$data[$i]."\n");
}

close $fh;
