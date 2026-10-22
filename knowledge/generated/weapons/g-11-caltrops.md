---
id: "g-11-caltrops"
name: "G-11 Caltrops"
collection: "weapons"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["broken_file_links"]
wiki_url: "https://helldivers.wiki.gg/wiki/G-11_Caltrops"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/weapons/g-11-caltrops.json"
---

# G-11 Caltrops

**分类：** 武器 (`weapons`) · **ID：** `g-11-caltrops`

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/G-11_Caltrops

## 简介

The G-11 Caltrops is a Special Throwable that deploys a field of proximity stun mines.

## 主要属性

| 字段 | 数值 |
|---|---|
| 类别 (`category`) | throwable |
| 子类别 (`subcategory`) | special |
| 特性 ID (`traitIds`) | stun, sticky |
| `throwable.capacity` | 5 |
| `throwable.startingCount` | 4 |
| `throwable.fromSupply` | 3 |
| `throwable.fuseTimeS` | — |
| `throwable.cookable` | 否 |


## 攻击模式、伤害与穿甲

### 1. G-11 CALTROPS E（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 50 |
| `damage.durable` | 10 |
| `damage.type` | Explosion |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 1 |
| `area.outerRadiusM` | 10 |
| `area.shockwaveRadiusM` | 15 |
| `forces.demolition` | 10 |
| `forces.stagger` | 30 |
| `forces.push` | 0 |


### 2. Stun Small（status）

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
| `label` | Scope of Authority P1 |
| 战争债券 ID (`warbondId`) | scope-of-authority |
| `page` | 1 |
| `cost.currency` | medals |
| `cost.amount` | 35 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/weapons/g-11-caltrops.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/G-11_Caltrops
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

