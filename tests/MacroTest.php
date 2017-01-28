<?php

namespace Pre\Tests;

use PHPUnit\Framework\TestCase;

class MacroTest extends TestCase
{
    public function testShortClosures()
    {
        $fixture = new Fixture();

        $cb = $fixture->foo("!");

        $this->assertEquals("hello chris!", $cb("chris"));
    }
}
