<?php

$str = 'JOHN';
$str2 = 'SMITH';

$arr = str_split($str);
$arr2 = str_split($str2);


$max = max(array(strlen($str), strlen($str2)));

$result = '';

for($i = 0; $i < $max; $i++){
    
    if (array_key_exists($i, $arr)){
        $result .= $arr[$i];
    }

    if (array_key_exists($i, $arr2)){
        $result .= $arr2[$i];
    }
}

echo $result;

?>