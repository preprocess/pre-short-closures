--DESCRIPTION--

Test short closure recursion

--GIVEN--

$cb = () => {
    return () => {
        return () => {
            return "hello world";
        };
    };
};

--EXPECT--

$cb = call_user_func(function ($context·0) {
    return function () use ($context·0) {
        extract($context·0);
        return call_user_func(function ($context·1) {
            return function () use ($context·1) {
                extract($context·1);
                return call_user_func(function ($context·2) {
                    return function () use ($context·2) {
                        extract($context·2);
                        return "hello world";
                    };
                }, get_defined_vars());
            };
        }, get_defined_vars());
    };
}, get_defined_vars());
