---
id: "g-7-pineapple"
name: "G-7 Pineapple"
collection: "weapons"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/G-7_Pineapple"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/weapons/g-7-pineapple.json"
---

# G-7 Pineapple

**分类：** 武器 (`weapons`) · **ID：** `g-7-pineapple`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/G-7_Pineapple

## 简介

The G-7 Pineapple is a Standard Throwable that explodes into several bomblets with shrapnel, able to inflict damage over a large area.

## 主要属性

| 字段 | 数值 |
|---|---|
| 类别 (`category`) | throwable |
| 子类别 (`subcategory`) | standard |
| 特性 ID (`traitIds`) | explosive |
| `throwable.capacity` | 5 |
| `throwable.startingCount` | 4 |
| `throwable.fromSupply` | 3 |
| `throwable.fuseTimeS` | 2.4 |
| `throwable.cookable` | 是 |


## 攻击模式、伤害与穿甲

### 1. G-7 PINEAPPLE E（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 300 |
| `damage.durable` | 300 |
| `damage.type` | Explosion |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 4 |
| `area.outerRadiusM` | 10 |
| `area.shockwaveRadiusM` | 14 |
| `forces.demolition` | 30 |
| `forces.stagger` | 25 |
| `forces.push` | 40 |


### 2. G-7 P（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 300 |
| `damage.durable` | 300 |
| `damage.type` | Ballistic |
| `penetration.direct` | medium |
| `penetration.slightAngle` | unarmored |
| `penetration.largeAngle` | unarmored |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | — |
| `projectile.massG` | 150 |
| `projectile.initialVelocityMps` | 25 |
| `projectile.dragFactorPct` | 50 |
| `projectile.gravityFactorPct` | 400 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 30 |
| `forces.stagger` | 25 |
| `forces.push` | 40 |


### 3. G-7 P IE（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 100 |
| `damage.durable` | 100 |
| `damage.type` | Explosion |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 2.5 |
| `area.outerRadiusM` | 5 |
| `area.shockwaveRadiusM` | 14 |
| `forces.demolition` | 20 |
| `forces.stagger` | 25 |
| `forces.push` | 40 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | warbond |
| `label` | Dust Devils P3 |
| 战争债券 ID (`warbondId`) | dust-devils |
| `page` | 3 |
| `cost.currency` | medals |
| `cost.amount` | 65 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/weapons/g-7-pineapple.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/G-7_Pineapple
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

