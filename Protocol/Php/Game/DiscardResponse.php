<?php
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game.proto

namespace Game;

use Google\Protobuf\Internal\GPBType;
use Google\Protobuf\Internal\RepeatedField;
use Google\Protobuf\Internal\GPBUtil;

/**
 * <pre>
 * 牌型
 * CARD_TYPE_ERRO = 0  # 非法
 * CARD_TYPE_DANZ = 1  # 单张
 * CARD_TYPE_YDUI = 2  # 一对
 * CARD_TYPE_SANZ = 3  # 三张牌（什么也不带）
 * CARD_TYPE_SDYI = 4  # 三带一（带一张单牌）
 * CARD_TYPE_SDER = 5  # 三带二（带一对）
 * CARD_TYPE_DANS = 6  # 单顺子
 * CARD_TYPE_LDUI = 7  # 连对（双顺子）
 * CARD_TYPE_SANS = 8  # 三顺子，飞机（什么都不带）
 * CARD_TYPE_SSDY = 9  # 三顺子，飞机（带单牌）
 * CARD_TYPE_SSDE = 10  # 三顺子，飞机（带对）
 * CARD_TYPE_ZHAD = 11  # 炸弹
 * CARD_TYPE_HUOJ = 12  # 王炸，火箭
 * CARD_TYPE_SDLZ = 13  # 四带二（带两张单牌）
 * CARD_TYPE_SDLD = 14  # 四带二（带两对）
 * CARD_TYPE_PASS = 15  # pass
 * </pre>
 *
 * Protobuf type <code>game.DiscardResponse</code>
 */
class DiscardResponse extends \Google\Protobuf\Internal\Message
{
    /**
     * <code>repeated .game.Card card = 1;</code>
     */
    private $card;
    /**
     * <pre>
     * 玩家UUID
     * </pre>
     *
     * <code>string player = 2;</code>
     */
    private $player = '';
    /**
     * <code>uint32 card_type = 3;</code>
     */
    private $card_type = 0;
    /**
     * <pre>
     * 下一个出牌的玩家uuid
     * </pre>
     *
     * <code>string next_discard_player = 4;</code>
     */
    private $next_discard_player = '';
    /**
     * <pre>
     *大A玩家是否全部出现
     * </pre>
     *
     * <code>int32 is_all_show_a = 5;</code>
     */
    private $is_all_show_a = 0;
    /**
     * <pre>
     *0 亮一个A  1 亮双A  2 反A
     * </pre>
     *
     * <code>int32 tableType = 6;</code>
     */
    private $tableType = 0;
    /**
     * <pre>
     *0 非独8  1 独8
     * </pre>
     *
     * <code>int32 singleFlag = 7;</code>
     */
    private $singleFlag = 0;
    /**
     * <pre>
     * 另一个A所属于的玩家
     * </pre>
     *
     * <code>string otherAPlayer = 8;</code>
     */
    private $otherAPlayer = '';

    public function __construct() {
        \GPBMetadata\Game::initOnce();
        parent::__construct();
    }

    /**
     * <code>repeated .game.Card card = 1;</code>
     */
    public function getCard()
    {
        return $this->card;
    }

    /**
     * <code>repeated .game.Card card = 1;</code>
     */
    public function setCard(&$var)
    {
        $arr = GPBUtil::checkRepeatedField($var, \Google\Protobuf\Internal\GPBType::MESSAGE, \Game\Card::class);
        $this->card = $arr;
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
     * <code>uint32 card_type = 3;</code>
     */
    public function getCardType()
    {
        return $this->card_type;
    }

    /**
     * <code>uint32 card_type = 3;</code>
     */
    public function setCardType($var)
    {
        GPBUtil::checkUint32($var);
        $this->card_type = $var;
    }

    /**
     * <pre>
     * 下一个出牌的玩家uuid
     * </pre>
     *
     * <code>string next_discard_player = 4;</code>
     */
    public function getNextDiscardPlayer()
    {
        return $this->next_discard_player;
    }

    /**
     * <pre>
     * 下一个出牌的玩家uuid
     * </pre>
     *
     * <code>string next_discard_player = 4;</code>
     */
    public function setNextDiscardPlayer($var)
    {
        GPBUtil::checkString($var, True);
        $this->next_discard_player = $var;
    }

    /**
     * <pre>
     *大A玩家是否全部出现
     * </pre>
     *
     * <code>int32 is_all_show_a = 5;</code>
     */
    public function getIsAllShowA()
    {
        return $this->is_all_show_a;
    }

    /**
     * <pre>
     *大A玩家是否全部出现
     * </pre>
     *
     * <code>int32 is_all_show_a = 5;</code>
     */
    public function setIsAllShowA($var)
    {
        GPBUtil::checkInt32($var);
        $this->is_all_show_a = $var;
    }

    /**
     * <pre>
     *0 亮一个A  1 亮双A  2 反A
     * </pre>
     *
     * <code>int32 tableType = 6;</code>
     */
    public function getTableType()
    {
        return $this->tableType;
    }

    /**
     * <pre>
     *0 亮一个A  1 亮双A  2 反A
     * </pre>
     *
     * <code>int32 tableType = 6;</code>
     */
    public function setTableType($var)
    {
        GPBUtil::checkInt32($var);
        $this->tableType = $var;
    }

    /**
     * <pre>
     *0 非独8  1 独8
     * </pre>
     *
     * <code>int32 singleFlag = 7;</code>
     */
    public function getSingleFlag()
    {
        return $this->singleFlag;
    }

    /**
     * <pre>
     *0 非独8  1 独8
     * </pre>
     *
     * <code>int32 singleFlag = 7;</code>
     */
    public function setSingleFlag($var)
    {
        GPBUtil::checkInt32($var);
        $this->singleFlag = $var;
    }

    /**
     * <pre>
     * 另一个A所属于的玩家
     * </pre>
     *
     * <code>string otherAPlayer = 8;</code>
     */
    public function getOtherAPlayer()
    {
        return $this->otherAPlayer;
    }

    /**
     * <pre>
     * 另一个A所属于的玩家
     * </pre>
     *
     * <code>string otherAPlayer = 8;</code>
     */
    public function setOtherAPlayer($var)
    {
        GPBUtil::checkString($var, True);
        $this->otherAPlayer = $var;
    }

}

