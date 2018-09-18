<?php

use PHPUnit\Framework\TestCase;

class MacroTest extends TestCase
{
    /**
     * @test
     * @dataProvider specs
     */
    public function can_transform_code($from, $expected)
    {
        Pre\Plugin\addMacro(__DIR__ . "/../source/macros.yay");

        $actual = Pre\plugin\format(Pre\Plugin\parse($this->format($from)));
        $this->assertEquals($this->format($expected), $actual);
    }

    private function format($code)
    {
        return "<?php\n\n" . trim($code) . "\n";
    }

    public static function specs()
    {
        $specs = [];

        $files = [
            __DIR__ . "/specs/arg-type-callable.spec",
            __DIR__ . "/specs/examples.spec",
            __DIR__ . "/specs/expression-bodies.spec",
            __DIR__ . "/specs/recursion.spec",
            __DIR__ . "/specs/return-type-array.spec",
            __DIR__ . "/specs/return-type-callable.spec",
            __DIR__ . "/specs/return-type-object.spec",
            __DIR__ . "/specs/return-type-string.spec",
            __DIR__ . "/specs/return-type-void.spec",
            __DIR__ . "/specs/short-closures.spec",
        ];

        foreach ($files as $file) {
            $contents = file_get_contents($file);
            
            foreach (explode("---", $contents) as $spec) {
                array_push($specs, explode("~~~", $spec));
            }
        }

        return $specs;
    }
}
