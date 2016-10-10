<?php
    $Number = pow(10,2);
    $Randomtime = pow(10,2);
    $data = array_fill(0, $Number, 0);

    //echo rand(0, $Number);

    for ($i=0; $i < $Number; $i++) {
        $data[rand(0, $Number)]++;
    }
    //var_dump($data);
    
    $myfile = fopen("data-2.txt", "w") or die("Unable to open file!");
    $txt = "John Doe\n";
    fwrite($myfile, $txt);
    $txt = "Jane Doe\n";
    fwrite($myfile, $txt);
    fclose($myfile);
 ?>
