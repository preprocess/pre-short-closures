--DESCRIPTION--

Test async macro

--GIVEN--

$async = * ($path) => {
    return $path;
};

--EXPECT--

$async = async function($path) {return $path;
};
