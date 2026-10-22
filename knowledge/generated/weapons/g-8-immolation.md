---
id: "g-8-immolation"
name: "G-8 Immolation"
collection: "weapons"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: []
wiki_url: "https://helldivers.wiki.gg/wiki/G-8_Immolation"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/weapons/g-8-immolation.json"
---

# G-8 Immolation

**分类：** 武器 (`weapons`) · **ID：** `g-8-immolation`

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/G-8_Immolation

## 简介

The G-8 Immolation is a Special Throwable that explodes into a massive pool of fire upon impact.

## 主要属性

| 字段 | 数值 |
|---|---|
| 类别 (`category`) | throwable |
| 子类别 (`subcategory`) | special |
| 特性 ID (`traitIds`) | incendiary |
| `throwable.capacity` | 6 |
| `throwable.startingCount` | 4 |
| `throwable.fromSupply` | 3 |
| `throwable.fuseTimeS` | — |
| `throwable.cookable` | 否 |


## 攻击模式、伤害与穿甲

### 1. G-8 IMMOLATION E（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 20 |
| `damage.durable` | 20 |
| `damage.type` | Explosion |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 4 |
| `area.outerRadiusM` | 10 |
| `area.shockwaveRadiusM` | 10 |
| `forces.demolition` | 0 |
| `forces.stagger` | 40 |
| `forces.push` | 0 |


### 2. Fire（status）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 100 |
| `damage.durable` | 100 |
| `damage.type` | Fire |
| `penetration.direct` | heavy |
| `penetration.slightAngle` | heavy |
| `penetration.largeAngle` | heavy |
| `penetration.extremeAngle` | unarmored |
| `projectile` | — |
| `area` | — |
| `forces.demolition` | 0 |
| `forces.stagger` | 0 |
| `forces.push` | 0 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | warbond |
| `label` | Ironclad Democracy P1 |
| 战争债券 ID (`warbondId`) | ironclad-democracy |
| `page` | 1 |
| `cost.currency` | medals |
| `cost.amount` | 35 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/weapons/g-8-immolation.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/G-8_Immolation
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

