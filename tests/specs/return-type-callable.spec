--DESCRIPTION--

Test callable return type

--GIVEN--

$fn = ($x) :callable => { return () => { return $x; }; };

--EXPECT--

$fn = function ($x) :callable {
    return [$x = $x ?? null, "fn" => function () use (&$x) {
        return $x;
    }]["fn"];
};
