<?php
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game.proto

namespace Game;

use Google\Protobuf\Internal\GPBType;
use Google\Protobuf\Internal\RepeatedField;
use Google\Protobuf\Internal\GPBUtil;

/**
 * Protobuf type <code>game.ExistRoomWebResponse</code>
 */
class ExistRoomWebResponse extends \Google\Protobuf\Internal\Message
{
    /**
     * <code>bool flag = 1;</code>
     */
    private $flag = false;

    public function __construct() {
        \GPBMetadata\Game::initOnce();
        parent::__construct();
    }

    /**
     * <code>bool flag = 1;</code>
     */
    public function getFlag()
    {
        return $this->flag;
    }

    /**
     * <code>bool flag = 1;</code>
     */
    public function setFlag($var)
    {
        GPBUtil::checkBool($var);
        $this->flag = $var;
    }

}
