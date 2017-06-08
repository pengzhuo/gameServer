<?php
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game.proto

namespace Game;

use Google\Protobuf\Internal\GPBType;
use Google\Protobuf\Internal\RepeatedField;
use Google\Protobuf\Internal\GPBUtil;

/**
 * <pre>
 *SETTLEMENT_FOR_ROUND = 0x2004
 * </pre>
 *
 * Protobuf type <code>game.SettleForRoundResponse</code>
 */
class SettleForRoundResponse extends \Google\Protobuf\Internal\Message
{
    /**
     * <pre>
     * 当局底分
     * </pre>
     *
     * <code>uint32 base_score = 1;</code>
     */
    private $base_score = 0;
    /**
     * <pre>
     * 当局倍数
     * </pre>
     *
     * <code>uint32 multiple = 2;</code>
     */
    private $multiple = 0;
    /**
     * <code>repeated .game.SettleForRoundResponse.PlayerData player_data = 3;</code>
     */
    private $player_data;
    /**
     * <pre>
     * 春天或反春；0：没有；1：春天；2：反春
     * </pre>
     *
     * <code>uint32 is_spring = 4;</code>
     */
    private $is_spring = 0;

    public function __construct() {
        \GPBMetadata\Game::initOnce();
        parent::__construct();
    }

    /**
     * <pre>
     * 当局底分
     * </pre>
     *
     * <code>uint32 base_score = 1;</code>
     */
    public function getBaseScore()
    {
        return $this->base_score;
    }

    /**
     * <pre>
     * 当局底分
     * </pre>
     *
     * <code>uint32 base_score = 1;</code>
     */
    public function setBaseScore($var)
    {
        GPBUtil::checkUint32($var);
        $this->base_score = $var;
    }

    /**
     * <pre>
     * 当局倍数
     * </pre>
     *
     * <code>uint32 multiple = 2;</code>
     */
    public function getMultiple()
    {
        return $this->multiple;
    }

    /**
     * <pre>
     * 当局倍数
     * </pre>
     *
     * <code>uint32 multiple = 2;</code>
     */
    public function setMultiple($var)
    {
        GPBUtil::checkUint32($var);
        $this->multiple = $var;
    }

    /**
     * <code>repeated .game.SettleForRoundResponse.PlayerData player_data = 3;</code>
     */
    public function getPlayerData()
    {
        return $this->player_data;
    }

    /**
     * <code>repeated .game.SettleForRoundResponse.PlayerData player_data = 3;</code>
     */
    public function setPlayerData(&$var)
    {
        $arr = GPBUtil::checkRepeatedField($var, \Google\Protobuf\Internal\GPBType::MESSAGE, \Game\SettleForRoundResponse_PlayerData::class);
        $this->player_data = $arr;
    }

    /**
     * <pre>
     * 春天或反春；0：没有；1：春天；2：反春
     * </pre>
     *
     * <code>uint32 is_spring = 4;</code>
     */
    public function getIsSpring()
    {
        return $this->is_spring;
    }

    /**
     * <pre>
     * 春天或反春；0：没有；1：春天；2：反春
     * </pre>
     *
     * <code>uint32 is_spring = 4;</code>
     */
    public function setIsSpring($var)
    {
        GPBUtil::checkUint32($var);
        $this->is_spring = $var;
    }

}
