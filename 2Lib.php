<?php
    $Number = pow(10,5);
    $Randomtime = pow(10,8);
    $data = array_fill(0, $Number, 0);

    //echo rand(0, $Number);

    for ($i=0; $i < $Randomtime; $i++) {
        $data[rand(0, $Number-1)]++;
    }
    //var_dump($data);

    $myfile = fopen("data-2.txt", "wb") or die("Unable to open file!");

    for ($i=0; $i < $Number; $i++) {
        $txt = $i.' '.$data[$i]."\n";
        //echo $txt;
        fwrite($myfile, $txt);
    }

    fclose($myfile);
?>
