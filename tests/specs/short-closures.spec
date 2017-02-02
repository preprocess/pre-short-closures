--DESCRIPTION--

Test short closure macros

--GIVEN--

class Fixture
{
    public function foo($end) {
        return ($name) => {
            return "hello {$name}{$end}";
        };
    }
}

--EXPECT--

class Fixture
{
    public function foo($end)
    {
        return call_user_func(function ($context·0) {
            return function ($name) use ($context·0) {
                extract($context·0);
                return "hello {$name}{$end}";
            };
        }, get_defined_vars());
    }
}
