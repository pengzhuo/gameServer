<?php
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game.proto

namespace Game;

use Google\Protobuf\Internal\GPBType;
use Google\Protobuf\Internal\RepeatedField;
use Google\Protobuf\Internal\GPBUtil;

/**
 * <pre>
 *退出服务器
 * </pre>
 *
 * Protobuf type <code>game.exit</code>
 */
class exit extends \Google\Protobuf\Internal\Message
{
    /**
     * <pre>
     *玩家唯一ID
     * </pre>
     *
     * <code>string userId = 1;</code>
     */
    private $userId = '';

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

}
