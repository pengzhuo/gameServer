<?php
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game.proto

namespace Game;

use Google\Protobuf\Internal\GPBType;
use Google\Protobuf\Internal\RepeatedField;
use Google\Protobuf\Internal\GPBUtil;

/**
 * Protobuf type <code>game.Card</code>
 */
class Card extends \Google\Protobuf\Internal\Message
{
    /**
     * <pre>
     * 牌
     * </pre>
     *
     * <code>uint32 card = 1;</code>
     */
    private $card = 0;

    public function __construct() {
        \GPBMetadata\Game::initOnce();
        parent::__construct();
    }

    /**
     * <pre>
     * 牌
     * </pre>
     *
     * <code>uint32 card = 1;</code>
     */
    public function getCard()
    {
        return $this->card;
    }

    /**
     * <pre>
     * 牌
     * </pre>
     *
     * <code>uint32 card = 1;</code>
     */
    public function setCard($var)
    {
        GPBUtil::checkUint32($var);
        $this->card = $var;
    }

}
