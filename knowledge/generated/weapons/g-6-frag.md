---
id: "g-6-frag"
name: "G-6 Frag"
collection: "weapons"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/G-6_Frag"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/weapons/g-6-frag.json"
---

# G-6 Frag

**分类：** 武器 (`weapons`) · **ID：** `g-6-frag`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/G-6_Frag

## 简介

The G-6 Frag is a Standard Throwable with a large explosive radius, producing shrapnel that can deal additional damage.

## 主要属性

| 字段 | 数值 |
|---|---|
| 类别 (`category`) | throwable |
| 子类别 (`subcategory`) | standard |
| 特性 ID (`traitIds`) | medium-armor-penetrating, explosive |
| `throwable.capacity` | 6 |
| `throwable.startingCount` | 4 |
| `throwable.fromSupply` | 4 |
| `throwable.fuseTimeS` | 2.4 |
| `throwable.cookable` | 是 |


## 攻击模式、伤害与穿甲

### 1. G-6 FRAG E（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 500 |
| `damage.durable` | 500 |
| `damage.type` | Explosion |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 4 |
| `area.outerRadiusM` | 10 |
| `area.shockwaveRadiusM` | 14 |
| `forces.demolition` | 20 |
| `forces.stagger` | 25 |
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
| `label` | Helldivers Mobilize! P1 |
| 战争债券 ID (`warbondId`) | helldivers-mobilize |
| `page` | 1 |
| `cost.currency` | medals |
| `cost.amount` | 2 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/weapons/g-6-frag.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/G-6_Frag
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

