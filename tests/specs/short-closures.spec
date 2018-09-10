class Fixture
{
    public function foo($end, $thing)
    {
        return ($name) ~> {
            $this->something();
            return "hello {$name}{$end}{$thing}";
        };
    }
}

~~~

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

---

$thing = (array $args = []) ~> {
    print_r($args);
};

~~~

$thing = function (array $args = []) {
    print_r($args);
};
