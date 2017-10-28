--DESCRIPTION--

Test object return type

--GIVEN--

$fn = ($x) :SomeClass => { return new SomeClass($x); };

--EXPECT--

$fn = function ($x) :SomeClass {
    return new SomeClass($x);
};
