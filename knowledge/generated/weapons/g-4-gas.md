---
id: "g-4-gas"
name: "G-4 Gas"
collection: "weapons"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/G-4_Gas"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/weapons/g-4-gas.json"
---

# G-4 Gas

**分类：** 武器 (`weapons`) · **ID：** `g-4-gas`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/G-4_Gas

## 简介

The G-4 Gas (or Gas Grenade) is a Special Throwable that releases a cloud of Gas alongside a minuscule explosion.

## 主要属性

| 字段 | 数值 |
|---|---|
| 类别 (`category`) | throwable |
| 子类别 (`subcategory`) | special |
| 特性 ID (`traitIds`) | caustic, explosive |
| `throwable.capacity` | 4 |
| `throwable.startingCount` | 3 |
| `throwable.fromSupply` | 2 |
| `throwable.fuseTimeS` | 2.9 |
| `throwable.cookable` | 是 |


## 攻击模式、伤害与穿甲

### 1. G-4 GAS E（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 3 |
| `damage.durable` | 3 |
| `damage.type` | Gas |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 2 |
| `area.outerRadiusM` | 7 |
| `area.shockwaveRadiusM` | 7 |
| `forces.demolition` | 30 |
| `forces.stagger` | 10 |
| `forces.push` | 10 |


### 2. Gas（status）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 25 |
| `damage.durable` | 25 |
| `damage.type` | Gas |
| `penetration.direct` | anti_tank_ii |
| `penetration.slightAngle` | anti_tank_ii |
| `penetration.largeAngle` | anti_tank_ii |
| `penetration.extremeAngle` | unarmored |
| `projectile` | — |
| `area` | — |
| `forces.demolition` | 0 |
| `forces.stagger` | 0 |
| `forces.push` | 0 |


### 3. Gas Confusion（status）

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
| `label` | Chemical Agents P1 |
| 战争债券 ID (`warbondId`) | chemical-agents |
| `page` | 1 |
| `cost.currency` | medals |
| `cost.amount` | 30 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/weapons/g-4-gas.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/G-4_Gas
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

