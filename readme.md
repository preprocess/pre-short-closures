# Pre Short Closures

This adds short closure macros, to allow much more concise closure syntax, similar to modern JS.

## Using

The first step is to require this repository in your plugin repository:

```
composer require pre/short-closures
```

Then, you can replace longer closures with a more concise variant:

```php
array_filter($array, ($item) => {
    return !empty($item);
});
```

Short closures require both the parameter parenthesis, and the function body braces. They do not allow optional parameter parenthesis, or implicit returns and braces.

They also automatically transfer variables in the parent scope, using the built-in `get_defined_vars` and `extract` functions. Be aware of how your functions are compiled - it's a significant change from what you're used to, with traditional PHP!

## Testing

There are a few tests, to make sure short closures are compiled to syntactically valid PHP functions. You can run these tests with:

```
vendor/bin/phpunit
```

This assumes you've cloned this repository and run `composer install` beforehand.

## Versioning

This library follows [Semver](http://semver.org). According to Semver, you will be able to upgrade to any minor or patch version of this library without any breaking changes to the public API. Semver also requires that we clearly define the public API for this library.

All methods, with `public` visibility, are part of the public API. All other methods are not part of the public API. Where possible, we'll try to keep `protected` methods backwards-compatible in minor/patch versions, but if you're overriding methods then please test your work before upgrading.
