<?php

namespace Pre\ShortClosures;

use PHPUnit\Framework\TestCase;

use function Pre\process;

class MacroTest extends TestCase
{
    public function testShortClosures()
    {
        $fixture = new Fixture\Fixture();

        $cb = $fixture->foo("!");

        $this->assertEquals("hello chris!", $cb("chris"));
    }

    public function testNestedClosures()
    {
        $base = getenv("PRE_BASE_DIR");
        $pre = __DIR__ . "/Fixture/nested.pre";
        $php = __DIR__ . "/Fixture/nested.php";

        process($pre, $php);

        $this->assertEquals("hello world", require $php);
    }
}
