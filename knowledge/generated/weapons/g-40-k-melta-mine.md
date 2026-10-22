---
id: "g-40-k-melta-mine"
name: "G/40-K Melta Mine"
collection: "weapons"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: []
wiki_url: "https://helldivers.wiki.gg/wiki/G/40-K_Melta_Mine"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/weapons/g-40-k-melta-mine.json"
---

# G/40-K Melta Mine

**分类：** 武器 (`weapons`) · **ID：** `g-40-k-melta-mine`

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/G/40-K_Melta_Mine

## 简介

The G/40-K Melta Mine is a Special Throwable that deploys a proximity mine which, when detonated, releases a large column of superheated thermal energy before exploding.

## 主要属性

| 字段 | 数值 |
|---|---|
| 类别 (`category`) | throwable |
| 子类别 (`subcategory`) | special |
| 特性 ID (`traitIds`) | anti-tank |
| `throwable.capacity` | 4 |
| `throwable.startingCount` | 3 |
| `throwable.fromSupply` | 2 |
| `throwable.fuseTimeS` | — |
| `throwable.cookable` | 否 |


## 攻击模式、伤害与穿甲

### 1. G/40-K MELTA MINE E（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 2000 |
| `damage.durable` | 2000 |
| `damage.type` | Explosion |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 2.5 |
| `area.outerRadiusM` | 6 |
| `area.shockwaveRadiusM` | 15 |
| `forces.demolition` | 40 |
| `forces.stagger` | 40 |
| `forces.push` | 40 |


### 2. FLAMEWALL（other）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 600 |
| `damage.durable` | 600 |
| `damage.type` | Fire |
| `penetration.direct` | anti_tank_iii |
| `penetration.slightAngle` | anti_tank_iii |
| `penetration.largeAngle` | anti_tank_iii |
| `penetration.extremeAngle` | unarmored |
| `projectile` | — |
| `area` | — |
| `forces.demolition` | 10 |
| `forces.stagger` | 40 |
| `forces.push` | 40 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | warbond |
| `label` | Castellan’s Creed |
| 战争债券 ID (`warbondId`) | castellans-creed |
| `page` | 2 |
| `cost.currency` | medals |
| `cost.amount` | 50 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/weapons/g-40-k-melta-mine.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/G/40-K_Melta_Mine
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

