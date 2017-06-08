<?php
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game.proto

namespace Game;

use Google\Protobuf\Internal\GPBType;
use Google\Protobuf\Internal\RepeatedField;
use Google\Protobuf\Internal\GPBUtil;

/**
 * Protobuf type <code>game.ShowARequest</code>
 */
class ShowARequest extends \Google\Protobuf\Internal\Message
{
    /**
     * <pre>
     * 1亮主A  2亮次A  3亮双A
     * </pre>
     *
     * <code>uint32 flag = 1;</code>
     */
    private $flag = 0;
    /**
     * <pre>
     *亮的牌 
     * </pre>
     *
     * <code>.game.Card card = 2;</code>
     */
    private $card = null;

    public function __construct() {
        \GPBMetadata\Game::initOnce();
        parent::__construct();
    }

    /**
     * <pre>
     * 1亮主A  2亮次A  3亮双A
     * </pre>
     *
     * <code>uint32 flag = 1;</code>
     */
    public function getFlag()
    {
        return $this->flag;
    }

    /**
     * <pre>
     * 1亮主A  2亮次A  3亮双A
     * </pre>
     *
     * <code>uint32 flag = 1;</code>
     */
    public function setFlag($var)
    {
        GPBUtil::checkUint32($var);
        $this->flag = $var;
    }

    /**
     * <pre>
     *亮的牌 
     * </pre>
     *
     * <code>.game.Card card = 2;</code>
     */
    public function getCard()
    {
        return $this->card;
    }

    /**
     * <pre>
     *亮的牌 
     * </pre>
     *
     * <code>.game.Card card = 2;</code>
     */
    public function setCard(&$var)
    {
        GPBUtil::checkMessage($var, \Game\Card::class);
        $this->card = $var;
    }

}
