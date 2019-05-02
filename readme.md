# Short Closures

Documentation can be found at [preprocess.io](https://preprocess.io#short-closures).

> **Since [this RFC](https://wiki.php.net/rfc/arrow_functions_v2) was approved, we have standardised on the same syntax.** We do still allow function bodies and return type hints, but everything in that RFC can be done, with the same syntax, as far back as Yay will allow (7.1).

You can use closures with similar semantics to Javascript:

```php
$files = array_map(
    fn($path) => file_get_contents($path),
    $paths
);

$needles = [
    "PHP",
    "Go",
    "Javascript",
];

$matches = array_filter($files, fn($content = "") => {
    foreach ($needles as $needle) {
        if (stristr($content, $needle)) {
            return true;
        }
    }

    return false;
});
```

These are converted to:

```php
$files = array_map(
    function ($path) {
        return file_get_contents($path);
    },
    $paths
);

$needles = [
    "PHP",
    "Go",
    "Javascript",
];

$matches = array_filter($files, [$needles = $needles ?? null, $needle = $needle ?? null, "fn" => function ($content = "") use (&$needles, &$needle) {
    foreach ($needles as $needle) {
        if (stristr($content, $needle)) {
            return true;
        }
    }

    return false;
}]["fn"]);
```
