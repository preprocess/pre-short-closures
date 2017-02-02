<?php

namespace Pre\ShortClosures;

use Pre\Testing\Runner;

class SpecTest extends Runner
{
    protected function path(): string
    {
        return __DIR__ . "/specs";
    }
}
