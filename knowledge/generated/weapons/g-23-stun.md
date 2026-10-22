---
id: "g-23-stun"
name: "G-23 Stun"
collection: "weapons"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/G-23_Stun"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/weapons/g-23-stun.json"
---

# G-23 Stun

**分类：** 武器 (`weapons`) · **ID：** `g-23-stun`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/G-23_Stun

## 简介

The G-23 Stun is a Special Throwable that creates a non-lethal explosion, stunning enemies and slowing Helldivers.

## 主要属性

| 字段 | 数值 |
|---|---|
| 类别 (`category`) | throwable |
| 子类别 (`subcategory`) | special |
| 特性 ID (`traitIds`) | explosive, stun |
| `throwable.capacity` | 5 |
| `throwable.startingCount` | 4 |
| `throwable.fromSupply` | 3 |
| `throwable.fuseTimeS` | 1.8 |
| `throwable.cookable` | 是 |


## 攻击模式、伤害与穿甲

### 1. G-23 STUN E（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 0 |
| `damage.durable` | 0 |
| `damage.type` | Explosion |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 1 |
| `area.outerRadiusM` | 10 |
| `area.shockwaveRadiusM` | 15 |
| `forces.demolition` | 0 |
| `forces.stagger` | 50 |
| `forces.push` | 0 |


### 2. Stun Large（status）

| 字段 | 数值 |
|---|---|
| `damage.standard` | — |
| `damage.durable` | — |
| `damage.type` | — |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area` | — |
| `forces.demolition` | — |
| `forces.stagger` | — |
| `forces.push` | — |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | warbond |
| `label` | Cutting Edge P2 |
| 战争债券 ID (`warbondId`) | cutting-edge |
| `page` | 2 |
| `cost.currency` | medals |
| `cost.amount` | 25 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/weapons/g-23-stun.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/G-23_Stun
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

