<?php

namespace Yay;

// let's use a namespace trick, to make non-colliding variables predictable.

function md5($value)
{
    return $value;
}

putenv("PRE_BASE_DIR=" . __DIR__ . "/..");

require __DIR__ . "/../vendor/autoload.php";
