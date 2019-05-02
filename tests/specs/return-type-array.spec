$fn = fn($x): array => { return explode(', ', $x); };

~~~

$fn = function ($x): array {
    return explode(', ', $x);
};
