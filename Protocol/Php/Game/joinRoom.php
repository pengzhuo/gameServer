<?php
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game.proto

namespace Game;

use Google\Protobuf\Internal\GPBType;
use Google\Protobuf\Internal\RepeatedField;
use Google\Protobuf\Internal\GPBUtil;

/**
 * <pre>
 *加入房间
 * </pre>
 *
 * Protobuf type <code>game.joinRoom</code>
 */
class joinRoom extends \Google\Protobuf\Internal\Message
{
    /**
     * <pre>
     *房间ID
     * </pre>
     *
     * <code>string roomId = 1;</code>
     */
    private $roomId = '';
    /**
     * <pre>
     *玩家唯一ID
     * </pre>
     *
     * <code>string userId = 2;</code>
     */
    private $userId = '';

    public function __construct() {
        \GPBMetadata\Game::initOnce();
        parent::__construct();
    }

    /**
     * <pre>
     *房间ID
     * </pre>
     *
     * <code>string roomId = 1;</code>
     */
    public function getRoomId()
    {
        return $this->roomId;
    }

    /**
     * <pre>
     *房间ID
     * </pre>
     *
     * <code>string roomId = 1;</code>
     */
    public function setRoomId($var)
    {
        GPBUtil::checkString($var, True);
        $this->roomId = $var;

        return $this;
    }

    /**
     * <pre>
     *玩家唯一ID
     * </pre>
     *
     * <code>string userId = 2;</code>
     */
    public function getUserId()
    {
        return $this->userId;
    }

    /**
     * <pre>
     *玩家唯一ID
     * </pre>
     *
     * <code>string userId = 2;</code>
     */
    public function setUserId($var)
    {
        GPBUtil::checkString($var, True);
        $this->userId = $var;

        return $this;
    }

}

