$cb = fn() => {
    return fn() => {
        return fn() => {
            return "hello world";
        };
    };
};

~~~

$cb = function () {
    return function () {
        return function () {
            return "hello world";
        };
    };
};

---

$foo = "hello";
$bar = "world";

$cb = fn() => {
    return fn() => {
        return fn() => {
            print $foo . $bar;
        };
    };
};

~~~

$foo = "hello";
$bar = "world";

$cb = [
    ($foo = $foo ?? null),
    ($bar = $bar ?? null),
    "fn" => function () use (&$foo, &$bar) {
        return [
            ($foo = $foo ?? null),
            ($bar = $bar ?? null),
            "fn" => function () use (&$foo, &$bar) {
                return [
                    ($foo = $foo ?? null),
                    ($bar = $bar ?? null),
                    "fn" => function () use (&$foo, &$bar) {
                        print $foo . $bar;
                    }
                ]["fn"];
            }
        ]["fn"];
    }
]["fn"];
