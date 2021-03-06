<?php
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game.proto

namespace Game;

use Google\Protobuf\Internal\GPBType;
use Google\Protobuf\Internal\RepeatedField;
use Google\Protobuf\Internal\GPBUtil;

/**
 * <pre>
 *连接服务器
 * </pre>
 *
 * Protobuf type <code>game.connect</code>
 */
class connect extends \Google\Protobuf\Internal\Message
{
    /**
     * <pre>
     *玩家唯一ID
     * </pre>
     *
     * <code>string userId = 1;</code>
     */
    private $userId = '';
    /**
     * <pre>
     *玩家设备ID
     * </pre>
     *
     * <code>string deviceId = 2;</code>
     */
    private $deviceId = '';

    public function __construct() {
        \GPBMetadata\Game::initOnce();
        parent::__construct();
    }

    /**
     * <pre>
     *玩家唯一ID
     * </pre>
     *
     * <code>string userId = 1;</code>
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
     * <code>string userId = 1;</code>
     */
    public function setUserId($var)
    {
        GPBUtil::checkString($var, True);
        $this->userId = $var;

        return $this;
    }

    /**
     * <pre>
     *玩家设备ID
     * </pre>
     *
     * <code>string deviceId = 2;</code>
     */
    public function getDeviceId()
    {
        return $this->deviceId;
    }

    /**
     * <pre>
     *玩家设备ID
     * </pre>
     *
     * <code>string deviceId = 2;</code>
     */
    public function setDeviceId($var)
    {
        GPBUtil::checkString($var, True);
        $this->deviceId = $var;

        return $this;
    }

}

