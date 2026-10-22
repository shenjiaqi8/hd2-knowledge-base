---
id: "g-31-arc"
name: "G-31 Arc"
collection: "weapons"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/G-31_Arc"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/weapons/g-31-arc.json"
---

# G-31 Arc

**分类：** 武器 (`weapons`) · **ID：** `g-31-arc`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/G-31_Arc

## 简介

The G-31 Arc is a Special Throwable that fires arcs in a similar manner to the De-Escalator.

## 主要属性

| 字段 | 数值 |
|---|---|
| 类别 (`category`) | throwable |
| 子类别 (`subcategory`) | special |
| 特性 ID (`traitIds`) | explosive, arc |
| `throwable.capacity` | 5 |
| `throwable.startingCount` | 4 |
| `throwable.fromSupply` | 3 |
| `throwable.fuseTimeS` | 3 |
| `throwable.cookable` | 否 |


## 攻击模式、伤害与穿甲

### 1. G-31 ARC E（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 0 |
| `damage.durable` | 0 |
| `damage.type` | Arc |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 1 |
| `area.outerRadiusM` | 10 |
| `area.shockwaveRadiusM` | 15 |
| `forces.demolition` | 0 |
| `forces.stagger` | 0 |
| `forces.push` | 0 |


### 2. G-31 ARC E A（arc）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 100 |
| `damage.durable` | 70 |
| `damage.type` | Arc |
| `penetration.direct` | heavy |
| `penetration.slightAngle` | heavy |
| `penetration.largeAngle` | heavy |
| `penetration.extremeAngle` | unarmored |
| `projectile` | — |
| `area` | — |
| `forces.demolition` | 20 |
| `forces.stagger` | 35 |
| `forces.push` | 10 |


### 3. Stun Small（status）

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
| `label` | Control Group P3 |
| 战争债券 ID (`warbondId`) | control-group |
| `page` | 3 |
| `cost.currency` | medals |
| `cost.amount` | 65 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/weapons/g-31-arc.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/G-31_Arc
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

