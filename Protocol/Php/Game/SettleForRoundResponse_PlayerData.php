<?php
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game.proto

namespace Game;

use Google\Protobuf\Internal\GPBType;
use Google\Protobuf\Internal\RepeatedField;
use Google\Protobuf\Internal\GPBUtil;

/**
 * Protobuf type <code>game.SettleForRoundResponse.PlayerData</code>
 */
class SettleForRoundResponse_PlayerData extends \Google\Protobuf\Internal\Message
{
    /**
     * <pre>
     * 玩家UUID
     * </pre>
     *
     * <code>string player = 1;</code>
     */
    private $player = '';
    /**
     * <pre>
     * 玩家手牌
     * </pre>
     *
     * <code>repeated .game.Card cards_in_hand = 2;</code>
     */
    private $cards_in_hand;
    /**
     * <pre>
     * 玩家当局分数
     * </pre>
     *
     * <code>int32 score = 3;</code>
     */
    private $score = 0;
    /**
     * <pre>
     * 玩家累计总分
     * </pre>
     *
     * <code>int32 total = 4;</code>
     */
    private $total = 0;
    /**
     * <pre>
     * 玩家出了的炸弹数
     * </pre>
     *
     * <code>uint32 bomb_count = 5;</code>
     */
    private $bomb_count = 0;
    /**
     * <pre>
     * 玩家是输是赢, 1：赢 2：平局  3；输
     * </pre>
     *
     * <code>int32 is_win = 6;</code>
     */
    private $is_win = 0;
    /**
     * <pre>
     *是否亮A方 0：不是； 1是；
     * </pre>
     *
     * <code>uint32 is_a = 7;</code>
     */
    private $is_a = 0;

    public function __construct() {
        \GPBMetadata\Game::initOnce();
        parent::__construct();
    }

    /**
     * <pre>
     * 玩家UUID
     * </pre>
     *
     * <code>string player = 1;</code>
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
     * <code>string player = 1;</code>
     */
    public function setPlayer($var)
    {
        GPBUtil::checkString($var, True);
        $this->player = $var;
    }

    /**
     * <pre>
     * 玩家手牌
     * </pre>
     *
     * <code>repeated .game.Card cards_in_hand = 2;</code>
     */
    public function getCardsInHand()
    {
        return $this->cards_in_hand;
    }

    /**
     * <pre>
     * 玩家手牌
     * </pre>
     *
     * <code>repeated .game.Card cards_in_hand = 2;</code>
     */
    public function setCardsInHand(&$var)
    {
        $arr = GPBUtil::checkRepeatedField($var, \Google\Protobuf\Internal\GPBType::MESSAGE, \Game\Card::class);
        $this->cards_in_hand = $arr;
    }

    /**
     * <pre>
     * 玩家当局分数
     * </pre>
     *
     * <code>int32 score = 3;</code>
     */
    public function getScore()
    {
        return $this->score;
    }

    /**
     * <pre>
     * 玩家当局分数
     * </pre>
     *
     * <code>int32 score = 3;</code>
     */
    public function setScore($var)
    {
        GPBUtil::checkInt32($var);
        $this->score = $var;
    }

    /**
     * <pre>
     * 玩家累计总分
     * </pre>
     *
     * <code>int32 total = 4;</code>
     */
    public function getTotal()
    {
        return $this->total;
    }

    /**
     * <pre>
     * 玩家累计总分
     * </pre>
     *
     * <code>int32 total = 4;</code>
     */
    public function setTotal($var)
    {
        GPBUtil::checkInt32($var);
        $this->total = $var;
    }

    /**
     * <pre>
     * 玩家出了的炸弹数
     * </pre>
     *
     * <code>uint32 bomb_count = 5;</code>
     */
    public function getBombCount()
    {
        return $this->bomb_count;
    }

    /**
     * <pre>
     * 玩家出了的炸弹数
     * </pre>
     *
     * <code>uint32 bomb_count = 5;</code>
     */
    public function setBombCount($var)
    {
        GPBUtil::checkUint32($var);
        $this->bomb_count = $var;
    }

    /**
     * <pre>
     * 玩家是输是赢, 1：赢 2：平局  3；输
     * </pre>
     *
     * <code>int32 is_win = 6;</code>
     */
    public function getIsWin()
    {
        return $this->is_win;
    }

    /**
     * <pre>
     * 玩家是输是赢, 1：赢 2：平局  3；输
     * </pre>
     *
     * <code>int32 is_win = 6;</code>
     */
    public function setIsWin($var)
    {
        GPBUtil::checkInt32($var);
        $this->is_win = $var;
    }

    /**
     * <pre>
     *是否亮A方 0：不是； 1是；
     * </pre>
     *
     * <code>uint32 is_a = 7;</code>
     */
    public function getIsA()
    {
        return $this->is_a;
    }

    /**
     * <pre>
     *是否亮A方 0：不是； 1是；
     * </pre>
     *
     * <code>uint32 is_a = 7;</code>
     */
    public function setIsA($var)
    {
        GPBUtil::checkUint32($var);
        $this->is_a = $var;
    }

}
