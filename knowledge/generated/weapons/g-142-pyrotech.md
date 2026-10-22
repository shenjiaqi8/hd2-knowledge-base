---
id: "g-142-pyrotech"
name: "G-142 Pyrotech"
collection: "weapons"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/G-142_Pyrotech"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/weapons/g-142-pyrotech.json"
---

# G-142 Pyrotech

**分类：** 武器 (`weapons`) · **ID：** `g-142-pyrotech`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/G-142_Pyrotech

## 简介

The G-142 Pyrotech is a Special Throwable that trades direct explosive damage for lingering fire, causing enemies to take damage over time.

## 主要属性

| 字段 | 数值 |
|---|---|
| 类别 (`category`) | throwable |
| 子类别 (`subcategory`) | special |
| 特性 ID (`traitIds`) | incendiary, explosive |
| `throwable.capacity` | 6 |
| `throwable.startingCount` | 4 |
| `throwable.fromSupply` | 3 |
| `throwable.fuseTimeS` | 2.9 |
| `throwable.cookable` | 否 |


## 攻击模式、伤害与穿甲

### 1. G-142 PYROTECH E（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 50 |
| `damage.durable` | 50 |
| `damage.type` | Fire |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 2.5 |
| `area.outerRadiusM` | 5 |
| `area.shockwaveRadiusM` | 7 |
| `forces.demolition` | 30 |
| `forces.stagger` | 50 |
| `forces.push` | 40 |


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


### 3. G-142 PYROTECH S（spray）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 0 |
| `damage.durable` | 0 |
| `damage.type` | Fire |
| `penetration.direct` | anti_tank_iii |
| `penetration.slightAngle` | anti_tank_iii |
| `penetration.largeAngle` | anti_tank_iii |
| `penetration.extremeAngle` | unarmored |
| `projectile` | — |
| `area` | — |
| `forces.demolition` | 10 |
| `forces.stagger` | 5 |
| `forces.push` | 5 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | warbond |
| `label` | Masters of Ceremony P3 |
| 战争债券 ID (`warbondId`) | masters-of-ceremony |
| `page` | 3 |
| `cost.currency` | medals |
| `cost.amount` | 65 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/weapons/g-142-pyrotech.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/G-142_Pyrotech
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

