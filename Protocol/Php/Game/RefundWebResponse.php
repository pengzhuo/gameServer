<?php
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game.proto

namespace Game;

use Google\Protobuf\Internal\GPBType;
use Google\Protobuf\Internal\RepeatedField;
use Google\Protobuf\Internal\GPBUtil;

/**
 * <pre>
 * 退款
 * </pre>
 *
 * Protobuf type <code>game.RefundWebResponse</code>
 */
class RefundWebResponse extends \Google\Protobuf\Internal\Message
{
    /**
     * <code>uint32 code = 1;</code>
     */
    private $code = 0;
    /**
     * <pre>
     * 6位房间号
     * </pre>
     *
     * <code>uint32 room_id = 2;</code>
     */
    private $room_id = 0;
    /**
     * <code>uint32 game_type = 3;</code>
     */
    private $game_type = 0;
    /**
     * <code>uint32 app_id = 4;</code>
     */
    private $app_id = 0;
    /**
     * <code>string owner = 5;</code>
     */
    private $owner = '';
    /**
     * <code>string room_uuid = 6;</code>
     */
    private $room_uuid = '';

    public function __construct() {
        \GPBMetadata\Game::initOnce();
        parent::__construct();
    }

    /**
     * <code>uint32 code = 1;</code>
     */
    public function getCode()
    {
        return $this->code;
    }

    /**
     * <code>uint32 code = 1;</code>
     */
    public function setCode($var)
    {
        GPBUtil::checkUint32($var);
        $this->code = $var;
    }

    /**
     * <pre>
     * 6位房间号
     * </pre>
     *
     * <code>uint32 room_id = 2;</code>
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
     * <code>uint32 room_id = 2;</code>
     */
    public function setRoomId($var)
    {
        GPBUtil::checkUint32($var);
        $this->room_id = $var;
    }

    /**
     * <code>uint32 game_type = 3;</code>
     */
    public function getGameType()
    {
        return $this->game_type;
    }

    /**
     * <code>uint32 game_type = 3;</code>
     */
    public function setGameType($var)
    {
        GPBUtil::checkUint32($var);
        $this->game_type = $var;
    }

    /**
     * <code>uint32 app_id = 4;</code>
     */
    public function getAppId()
    {
        return $this->app_id;
    }

    /**
     * <code>uint32 app_id = 4;</code>
     */
    public function setAppId($var)
    {
        GPBUtil::checkUint32($var);
        $this->app_id = $var;
    }

    /**
     * <code>string owner = 5;</code>
     */
    public function getOwner()
    {
        return $this->owner;
    }

    /**
     * <code>string owner = 5;</code>
     */
    public function setOwner($var)
    {
        GPBUtil::checkString($var, True);
        $this->owner = $var;
    }

    /**
     * <code>string room_uuid = 6;</code>
     */
    public function getRoomUuid()
    {
        return $this->room_uuid;
    }

    /**
     * <code>string room_uuid = 6;</code>
     */
    public function setRoomUuid($var)
    {
        GPBUtil::checkString($var, True);
        $this->room_uuid = $var;
    }

}

