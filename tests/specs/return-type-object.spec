$fn = ($x): SomeClass ~> { return new SomeClass($x); };

~~~

$fn = function ($x): SomeClass {
    return new SomeClass($x);
};
