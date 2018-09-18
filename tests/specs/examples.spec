$files = array_map(
    $path ~> file_get_contents($path), $paths
);

$needles = [
    "PHP",
    "Go",
    "Javascript",
];

$matches = array_filter($files, ($content = "") ~> {
    foreach ($needles as $needle) {
        if (stristr($content, $needle)) {
            return true;
        }
    }

    return false;
});

~~~

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
