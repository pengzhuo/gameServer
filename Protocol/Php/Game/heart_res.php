<?php
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game.proto

namespace Game;

use Google\Protobuf\Internal\GPBType;
use Google\Protobuf\Internal\RepeatedField;
use Google\Protobuf\Internal\GPBUtil;

/**
 * Protobuf type <code>game.heart_res</code>
 */
class heart_res extends \Google\Protobuf\Internal\Message
{
    /**
     * <pre>
     *占位字段
     * </pre>
     *
     * <code>string ext = 1;</code>
     */
    private $ext = '';

    public function __construct() {
        \GPBMetadata\Game::initOnce();
        parent::__construct();
    }

    /**
     * <pre>
     *占位字段
     * </pre>
     *
     * <code>string ext = 1;</code>
     */
    public function getExt()
    {
        return $this->ext;
    }

    /**
     * <pre>
     *占位字段
     * </pre>
     *
     * <code>string ext = 1;</code>
     */
    public function setExt($var)
    {
        GPBUtil::checkString($var, True);
        $this->ext = $var;

        return $this;
    }

}

