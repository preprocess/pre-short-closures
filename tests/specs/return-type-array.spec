--DESCRIPTION--

Test array return type

--GIVEN--

$fn = ($x) :array => { return explode(', ', $x); };

--EXPECT--

$fn = function ($x) :array {
    return explode(', ', $x);
};
