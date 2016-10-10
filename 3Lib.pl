$Number = 10**2;
$Randomtime =  10**2;
@data = (0) x 5;

for (my $i = 0; $i < $Randomtime; $i++) {
    $data[int(rand($Number))]++;
}

for (my $i = 0; $i < $Number; $i++) {
    if (!$data[$i]) {
        $data[$i] = 0;
    }

    #print($i." ".$data[$i]."\n");
}
