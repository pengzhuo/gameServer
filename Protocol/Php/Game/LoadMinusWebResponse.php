<?php
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game.proto

namespace Game;

use Google\Protobuf\Internal\GPBType;
use Google\Protobuf\Internal\RepeatedField;
use Google\Protobuf\Internal\GPBUtil;

/**
 * Protobuf type <code>game.LoadMinusWebResponse</code>
 */
class LoadMinusWebResponse extends \Google\Protobuf\Internal\Message
{
    /**
     * <code>string addr = 1;</code>
     */
    private $addr = '';
    /**
     * <code>uint32 port = 2;</code>
     */
    private $port = 0;

    public function __construct() {
        \GPBMetadata\Game::initOnce();
        parent::__construct();
    }

    /**
     * <code>string addr = 1;</code>
     */
    public function getAddr()
    {
        return $this->addr;
    }

    /**
     * <code>string addr = 1;</code>
     */
    public function setAddr($var)
    {
        GPBUtil::checkString($var, True);
        $this->addr = $var;
    }

    /**
     * <code>uint32 port = 2;</code>
     */
    public function getPort()
    {
        return $this->port;
    }

    /**
     * <code>uint32 port = 2;</code>
     */
    public function setPort($var)
    {
        GPBUtil::checkUint32($var);
        $this->port = $var;
    }

}

