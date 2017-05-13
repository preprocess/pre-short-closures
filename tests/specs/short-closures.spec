--DESCRIPTION--

Test short closure macros

--GIVEN--

class Fixture
{
    public function foo($end, $thing) {
        return ($name) => {
            $this->something();
            return "hello {$name}{$end}{$thing}";
        };
    }
}

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
