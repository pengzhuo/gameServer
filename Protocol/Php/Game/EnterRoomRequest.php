<?php
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game.proto

namespace Game;

use Google\Protobuf\Internal\GPBType;
use Google\Protobuf\Internal\RepeatedField;
use Google\Protobuf\Internal\GPBUtil;

/**
 * <pre>
 *ENTER_ROOM = 0x1005  # 进入房间
 * </pre>
 *
 * Protobuf type <code>game.EnterRoomRequest</code>
 */
class EnterRoomRequest extends \Google\Protobuf\Internal\Message
{
    /**
     * <pre>
     * 6位房间号
     * </pre>
     *
     * <code>uint32 room_id = 1;</code>
     */
    private $room_id = 0;
    /**
     * <pre>
     * 玩家UUID
     * </pre>
     *
     * <code>string player = 2;</code>
     */
    private $player = '';
    /**
     * <pre>
     * 玩家详细信息
     * </pre>
     *
     * <code>string info = 3;</code>
     */
    private $info = '';

    public function __construct() {
        \GPBMetadata\Game::initOnce();
        parent::__construct();
    }

    /**
     * <pre>
     * 6位房间号
     * </pre>
     *
     * <code>uint32 room_id = 1;</code>
     */
    public function getRoomId()
    {
        return $this->room_id;
    }

    /**
     * <pre>
     * 6位房间号
     * </pre>
     *
     * <code>uint32 room_id = 1;</code>
     */
    public function setRoomId($var)
    {
        GPBUtil::checkUint32($var);
        $this->room_id = $var;
    }

    /**
     * <pre>
     * 玩家UUID
     * </pre>
     *
     * <code>string player = 2;</code>
     */
    public function getPlayer()
    {
        return $this->player;
    }

    /**
     * <pre>
     * 玩家UUID
     * </pre>
     *
     * <code>string player = 2;</code>
     */
    public function setPlayer($var)
    {
        GPBUtil::checkString($var, True);
        $this->player = $var;
    }

    /**
     * <pre>
     * 玩家详细信息
     * </pre>
     *
     * <code>string info = 3;</code>
     */
    public function getInfo()
    {
        return $this->info;
    }

    /**
     * <pre>
     * 玩家详细信息
     * </pre>
     *
     * <code>string info = 3;</code>
     */
    public function setInfo($var)
    {
        GPBUtil::checkString($var, True);
        $this->info = $var;
    }

}
