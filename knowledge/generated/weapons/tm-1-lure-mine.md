---
id: "tm-1-lure-mine"
name: "TM-1 Lure Mine"
collection: "weapons"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/TM-1_Lure_Mine"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/weapons/tm-1-lure-mine.json"
---

# TM-1 Lure Mine

**分类：** 武器 (`weapons`) · **ID：** `tm-1-lure-mine`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/TM-1_Lure_Mine

## 简介

The TM-1 Lure Mine is a Special Throwable that lures in enemies before proximity detonating with a high damage explosion and shrapnel.

## 主要属性

| 字段 | 数值 |
|---|---|
| 类别 (`category`) | throwable |
| 子类别 (`subcategory`) | special |
| 特性 ID (`traitIds`) | anti-tank, sticky, explosive |
| `throwable.capacity` | 4 |
| `throwable.startingCount` | 3 |
| `throwable.fromSupply` | 2 |
| `throwable.fuseTimeS` | — |
| `throwable.cookable` | 否 |


## 攻击模式、伤害与穿甲

### 1. TM-1 LURE MINE E（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 1000 |
| `damage.durable` | 1000 |
| `damage.type` | Explosion |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 2 |
| `area.outerRadiusM` | 8 |
| `area.shockwaveRadiusM` | 12 |
| `forces.demolition` | 30 |
| `forces.stagger` | 30 |
| `forces.push` | 40 |


### 2. AC-8 P2（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 110 |
| `damage.durable` | 35 |
| `damage.type` | Ballistic |
| `penetration.direct` | medium |
| `penetration.slightAngle` | medium |
| `penetration.largeAngle` | light |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | — |
| `projectile.massG` | 100 |
| `projectile.initialVelocityMps` | 30 |
| `projectile.dragFactorPct` | 40 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 10 |
| `forces.stagger` | 10 |
| `forces.push` | 20 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | warbond |
| `label` | Redacted Regiment P3 |
| 战争债券 ID (`warbondId`) | redacted-regiment |
| `page` | 3 |
| `cost.currency` | medals |
| `cost.amount` | 65 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/weapons/tm-1-lure-mine.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/TM-1_Lure_Mine
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

