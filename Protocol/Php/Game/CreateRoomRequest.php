<?php
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game.proto

namespace Game;

use Google\Protobuf\Internal\GPBType;
use Google\Protobuf\Internal\RepeatedField;
use Google\Protobuf\Internal\GPBUtil;

/**
 * Protobuf type <code>game.CreateRoomRequest</code>
 */
class CreateRoomRequest extends \Google\Protobuf\Internal\Message
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
     * 房主UUID
     * </pre>
     *
     * <code>string owner = 2;</code>
     */
    private $owner = '';
    /**
     * <pre>
     * json 创建房间参数，由具体游戏各自解析字段
     * </pre>
     *
     * <code>string kwargs = 3;</code>
     */
    private $kwargs = '';
    /**
     * <pre>
     * 房间唯一标识
     * </pre>
     *
     * <code>string room_uuid = 4;</code>
     */
    private $room_uuid = '';

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
     * 房主UUID
     * </pre>
     *
     * <code>string owner = 2;</code>
     */
    public function getOwner()
    {
        return $this->owner;
    }

    /**
     * <pre>
     * 房主UUID
     * </pre>
     *
     * <code>string owner = 2;</code>
     */
    public function setOwner($var)
    {
        GPBUtil::checkString($var, True);
        $this->owner = $var;
    }

    /**
     * <pre>
     * json 创建房间参数，由具体游戏各自解析字段
     * </pre>
     *
     * <code>string kwargs = 3;</code>
     */
    public function getKwargs()
    {
        return $this->kwargs;
    }

    /**
     * <pre>
     * json 创建房间参数，由具体游戏各自解析字段
     * </pre>
     *
     * <code>string kwargs = 3;</code>
     */
    public function setKwargs($var)
    {
        GPBUtil::checkString($var, True);
        $this->kwargs = $var;
    }

    /**
     * <pre>
     * 房间唯一标识
     * </pre>
     *
     * <code>string room_uuid = 4;</code>
     */
    public function getRoomUuid()
    {
        return $this->room_uuid;
    }

    /**
     * <pre>
     * 房间唯一标识
     * </pre>
     *
     * <code>string room_uuid = 4;</code>
     */
    public function setRoomUuid($var)
    {
        GPBUtil::checkString($var, True);
        $this->room_uuid = $var;
    }

}
