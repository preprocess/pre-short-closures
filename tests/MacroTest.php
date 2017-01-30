<?php

namespace Pre\Tests;

use PHPUnit\Framework\TestCase;

use function Pre\process;

class MacroTest extends TestCase
{
    public function testShortClosures()
    {
        $fixture = new Fixture();

        $cb = $fixture->foo("!");

        $this->assertEquals("hello chris!", $cb("chris"));
    }

    public function testNestedClosures()
    {
        $base = getenv("PRE_BASE_DIR");
        $pre = __DIR__ . "/nested.pre";
        $php = __DIR__ . "/nested.php";

        process($base, $pre, $php);

        $this->assertEquals("hello world", require $php);
    }
}
