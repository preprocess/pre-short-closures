--DESCRIPTION--

Test void return type

--GIVEN--

$fn = ($x) :void => { error_log($x); };

--EXPECT--

$fn = function ($x) :void {
    error_log($x);
};
