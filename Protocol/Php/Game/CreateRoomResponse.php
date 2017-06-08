<?php
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game.proto

namespace Game;

use Google\Protobuf\Internal\GPBType;
use Google\Protobuf\Internal\RepeatedField;
use Google\Protobuf\Internal\GPBUtil;

/**
 * Protobuf type <code>game.CreateRoomResponse</code>
 */
class CreateRoomResponse extends \Google\Protobuf\Internal\Message
{
    /**
     * <pre>
     * 返回开房结果
     * </pre>
     *
     * <code>uint32 code = 1;</code>
     */
    private $code = 0;

    public function __construct() {
        \GPBMetadata\Game::initOnce();
        parent::__construct();
    }

    /**
     * <pre>
     * 返回开房结果
     * </pre>
     *
     * <code>uint32 code = 1;</code>
     */
    public function getCode()
    {
        return $this->code;
    }

    /**
     * <pre>
     * 返回开房结果
     * </pre>
     *
     * <code>uint32 code = 1;</code>
     */
    public function setCode($var)
    {
        GPBUtil::checkUint32($var);
        $this->code = $var;
    }

}
