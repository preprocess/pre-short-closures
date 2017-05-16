--DESCRIPTION--

Test short closure macros

--GIVEN--

class Fixture
{
    public function foo($end, $thing)
    {
        return ($name) => {
            $this->something();
            return "hello {$name}{$end}{$thing}";
        };
    }
}

$thing = (array $args = []) => {
    print_r($args);
};

--EXPECT--

class Fixture
{
    public function foo($end, $thing)
    {
        return [$end = $end ?? null, $thing = $thing ?? null, "fn" => function ($name) use (&$end, &$thing) {
            $this->something();
            return "hello {$name}{$end}{$thing}";
        }]["fn"];
    }
}

$thing = function (array $args = []) {
    print_r($args);
};
