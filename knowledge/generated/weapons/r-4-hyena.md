---
id: "r-4-hyena"
name: "R-4 Hyena"
collection: "weapons"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: []
wiki_url: "https://helldivers.wiki.gg/wiki/R-4_Hyena"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/weapons/r-4-hyena.json"
---

# R-4 Hyena

**分类：** 武器 (`weapons`) · **ID：** `r-4-hyena`

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/R-4_Hyena

## 简介

The R-4 Hyena is a Primary Marksman Rifle similar to the R-63CS Diligence Counter Sniper, trading magazine count, fire rate, and handling for greater firepower and incendiary rounds.

## 主要属性

| 字段 | 数值 |
|---|---|
| 类别 (`category`) | primary |
| 子类别 (`subcategory`) | marksman_rifle |
| 特性 ID (`traitIds`) | medium-armor-penetrating, incendiary |


## 枪械属性

| 字段 | 数值 |
|---|---|
| `firingModes` | semi |
| 射速（RPM） (`fireRateRpm`) | 190 |
| `dps` | 696.67 |
| 容量 (`capacity`) | 15 |
| 备用弹匣 (`spareMagazines`) | 5 |
| 初始弹匣 (`startingMagazines`) | 4 |
| `magazinesFromSupply` | 5 |
| `magazinesFromAmmoBox` | 2 |
| 后坐力 (`recoil`) | 65 |
| `horizontalRecoil` | 40 |
| `verticalRecoil` | 90 |
| `spread.horizontal` | 0.5 |
| `spread.vertical` | 0.5 |
| `sway` | 1 |
| `ergonomics` | 30 |
| `reloadKind` | magazine |
| 装填时间（秒） (`reloadTimeS`) | 2.5 |
| `reloadTimeUpgradedS` | — |
| `tacticalReloadTimeS` | — |


## 攻击模式、伤害与穿甲

### 1. R-4 P（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 220 |
| `damage.durable` | 45 |
| `damage.type` | Ballistic |
| `penetration.direct` | medium |
| `penetration.slightAngle` | medium |
| `penetration.largeAngle` | medium |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | — |
| `projectile.massG` | 20 |
| `projectile.initialVelocityMps` | 950 |
| `projectile.dragFactorPct` | 30 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 10 |
| `forces.stagger` | 20 |
| `forces.push` | 14 |


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
| `type` | event |
| `label` | Celestial Fence |
| 战争债券 ID (`warbondId`) | — |
| `page` | — |
| 消耗 (`cost`) | — |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/weapons/r-4-hyena.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/R-4_Hyena
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

