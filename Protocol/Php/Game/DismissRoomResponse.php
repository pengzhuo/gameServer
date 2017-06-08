<?php
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game.proto

namespace Game;

use Google\Protobuf\Internal\GPBType;
use Google\Protobuf\Internal\RepeatedField;
use Google\Protobuf\Internal\GPBUtil;

/**
 * Protobuf type <code>game.DismissRoomResponse</code>
 */
class DismissRoomResponse extends \Google\Protobuf\Internal\Message
{
    /**
     * <pre>
     * 返回解散房间结果
     * </pre>
     *
     * <code>uint32 code = 1;</code>
     */
    private $code = 0;
    /**
     * <pre>
     * 0 房主发起解散 1 投票发起解散
     * </pre>
     *
     * <code>uint32 flag = 2;</code>
     */
    private $flag = 0;

    public function __construct() {
        \GPBMetadata\Game::initOnce();
        parent::__construct();
    }

    /**
     * <pre>
     * 返回解散房间结果
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
     * 返回解散房间结果
     * </pre>
     *
     * <code>uint32 code = 1;</code>
     */
    public function setCode($var)
    {
        GPBUtil::checkUint32($var);
        $this->code = $var;
    }

    /**
     * <pre>
     * 0 房主发起解散 1 投票发起解散
     * </pre>
     *
     * <code>uint32 flag = 2;</code>
     */
    public function getFlag()
    {
        return $this->flag;
    }

    /**
     * <pre>
     * 0 房主发起解散 1 投票发起解散
     * </pre>
     *
     * <code>uint32 flag = 2;</code>
     */
    public function setFlag($var)
    {
        GPBUtil::checkUint32($var);
        $this->flag = $var;
    }

}
