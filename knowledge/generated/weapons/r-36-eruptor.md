---
id: "r-36-eruptor"
name: "R-36 Eruptor"
collection: "weapons"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/R-36_Eruptor"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/weapons/r-36-eruptor.json"
---

# R-36 Eruptor

**分类：** 武器 (`weapons`) · **ID：** `r-36-eruptor`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/R-36_Eruptor

## 简介

R-36 Eruptor is a Primary Explosive weapon that fires jet-assisted shells which explode into shrapnel on impact.

## 主要属性

| 字段 | 数值 |
|---|---|
| 类别 (`category`) | primary |
| 子类别 (`subcategory`) | explosive |
| 特性 ID (`traitIds`) | explosive, heavy-armor-penetrating |


## 枪械属性

| 字段 | 数值 |
|---|---|
| `firingModes` | other |
| 射速（RPM） (`fireRateRpm`) | 32 |
| `dps` | 592 |
| 容量 (`capacity`) | 5 |
| 备用弹匣 (`spareMagazines`) | 6 |
| 初始弹匣 (`startingMagazines`) | 4 |
| `magazinesFromSupply` | 6 |
| `magazinesFromAmmoBox` | 3 |
| 后坐力 (`recoil`) | 57.5 |
| `horizontalRecoil` | 40 |
| `verticalRecoil` | 75 |
| `spread.horizontal` | 5 |
| `spread.vertical` | 5 |
| `sway` | 0.8 |
| `ergonomics` | 25 |
| `reloadKind` | magazine |
| 装填时间（秒） (`reloadTimeS`) | 4.67 |
| `reloadTimeUpgradedS` | — |
| `tacticalReloadTimeS` | 2.75 |


## 攻击模式、伤害与穿甲

### 1. R-36 P（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 230 |
| `damage.durable` | 115 |
| `damage.type` | Ballistic |
| `penetration.direct` | heavy |
| `penetration.slightAngle` | heavy |
| `penetration.largeAngle` | heavy |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | — |
| `projectile.massG` | 100 |
| `projectile.initialVelocityMps` | 180 |
| `projectile.dragFactorPct` | 0 |
| `projectile.gravityFactorPct` | 30 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 30 |
| `forces.stagger` | 35 |
| `forces.push` | 20 |


### 2. R-36 P IE（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 225 |
| `damage.durable` | 225 |
| `damage.type` | Explosion |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 4 |
| `area.outerRadiusM` | 7 |
| `area.shockwaveRadiusM` | 8 |
| `forces.demolition` | 20 |
| `forces.stagger` | 35 |
| `forces.push` | 40 |


### 3. AC-8 P2（projectile）

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
| `label` | Democratic Detonation P2 |
| 战争债券 ID (`warbondId`) | democratic-detonation |
| `page` | 2 |
| `cost.currency` | medals |
| `cost.amount` | 60 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/weapons/r-36-eruptor.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/R-36_Eruptor
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

