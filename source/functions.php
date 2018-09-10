<?php

namespace Pre\ShortClosures;

use Yay\Ast;

function closure($ast, $implicit = false) {
    if ($implicit) {
        $defined = [(string) $ast->{"functionArgumentName"} => true];
    } else {
        $defined = [];

        foreach ($ast->{"functionArguments"} as $node) {
            $defined[(string) $node["functionArgument"]["functionArgumentName"]] = true;
        }
    }

    $scoped = [];
    $scope = new \Yay\Ast("scope");

    foreach ($ast->{"* body"}->tokens() as $token) {
        $name = $token->value();

        if ($name !== '$this' && $token->is(T_VARIABLE) && !isset($scoped[$name]) && !isset($defined[$name])) {
            $scope->push(new \Yay\Ast("var", $token));
            $scoped[(string) $token] = true;
        }
    }

    $ast->append($scope);
}
