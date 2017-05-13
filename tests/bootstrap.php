<?php

namespace Yay;

function md5($value) {
    return $value;
}

require __DIR__ . "/../vendor/autoload.php";

putenv("PRE_BASE_DIR=" . __DIR__ . "/../");

\Pre\Plugin\addMacroPath(__DIR__ . "/../src/macros.yay");
