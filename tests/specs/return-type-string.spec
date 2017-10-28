--DESCRIPTION--

Test string return type

--GIVEN--

$fn = ($x) :string => { return $x . 'x'; };

--EXPECT--

$fn = function ($x) :string {
    return $x . 'x';
};
