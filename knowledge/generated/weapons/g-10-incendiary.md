---
id: "g-10-incendiary"
name: "G-10 Incendiary"
collection: "weapons"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/G-10_Incendiary"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/weapons/g-10-incendiary.json"
---

# G-10 Incendiary

**分类：** 武器 (`weapons`) · **ID：** `g-10-incendiary`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/G-10_Incendiary

## 简介

The G-10 Incendiary is a Standard Throwable that trades direct explosive damage for lingering fire, causing enemies to take damage over time.

## 主要属性

| 字段 | 数值 |
|---|---|
| 类别 (`category`) | throwable |
| 子类别 (`subcategory`) | standard |
| 特性 ID (`traitIds`) | incendiary, explosive |
| `throwable.capacity` | 5 |
| `throwable.startingCount` | 4 |
| `throwable.fromSupply` | 3 |
| `throwable.fuseTimeS` | 2.9 |
| `throwable.cookable` | 是 |


## 攻击模式、伤害与穿甲

### 1. G-10 INCENDIARY E（explosion）

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
| `area.innerRadiusM` | 1 |
| `area.outerRadiusM` | 7 |
| `area.shockwaveRadiusM` | 9 |
| `forces.demolition` | 30 |
| `forces.stagger` | 20 |
| `forces.push` | 15 |


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
| `label` | Steeled Veterans P2 |
| 战争债券 ID (`warbondId`) | steeled-veterans |
| `page` | 2 |
| `cost.currency` | medals |
| `cost.amount` | 25 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/weapons/g-10-incendiary.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/G-10_Incendiary
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

