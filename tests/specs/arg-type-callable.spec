--DESCRIPTION--

Test callable argument type

--GIVEN--

$fn = (callable $x) => { return $x(); };

--EXPECT--

$fn = function (callable $x) {
    return $x();
};
