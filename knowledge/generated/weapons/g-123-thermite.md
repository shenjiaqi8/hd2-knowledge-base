---
id: "g-123-thermite"
name: "G-123 Thermite"
collection: "weapons"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/G-123_Thermite"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/weapons/g-123-thermite.json"
---

# G-123 Thermite

**分类：** 武器 (`weapons`) · **ID：** `g-123-thermite`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/G-123_Thermite

## 简介

The G-123 Thermite is a Special Throwable that can stick and inflict heavy explosion damage to a single target after a delay.

## 主要属性

| 字段 | 数值 |
|---|---|
| 类别 (`category`) | throwable |
| 子类别 (`subcategory`) | special |
| 特性 ID (`traitIds`) | anti-tank, sticky |
| `throwable.capacity` | 3 |
| `throwable.startingCount` | 2 |
| `throwable.fromSupply` | 2 |
| `throwable.fuseTimeS` | 2.9 |
| `throwable.cookable` | 是 |


## 攻击模式、伤害与穿甲

### 1. G-123 THERMITE E（explosion）

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
| `area.innerRadiusM` | 1.5 |
| `area.outerRadiusM` | 2.5 |
| `area.shockwaveRadiusM` | 4 |
| `forces.demolition` | 30 |
| `forces.stagger` | 20 |
| `forces.push` | 40 |


### 2. Thermite（status）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 150 |
| `damage.durable` | 150 |
| `damage.type` | Damage |
| `penetration.direct` | anti_tank_iii |
| `penetration.slightAngle` | anti_tank_iii |
| `penetration.largeAngle` | anti_tank_iii |
| `penetration.extremeAngle` | unarmored |
| `projectile` | — |
| `area` | — |
| `forces.demolition` | 10 |
| `forces.stagger` | 0 |
| `forces.push` | 0 |


### 3. Fire（status）

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
| `label` | Democratic Detonation P1 |
| 战争债券 ID (`warbondId`) | democratic-detonation |
| `page` | 1 |
| `cost.currency` | medals |
| `cost.amount` | 15 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/weapons/g-123-thermite.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/G-123_Thermite
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

