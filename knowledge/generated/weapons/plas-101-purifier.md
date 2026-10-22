---
id: "plas-101-purifier"
name: "PLAS-101 Purifier"
collection: "weapons"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/PLAS-101_Purifier"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/weapons/plas-101-purifier.json"
---

# PLAS-101 Purifier

**分类：** 武器 (`weapons`) · **ID：** `plas-101-purifier`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/PLAS-101_Purifier

## 简介

The PLAS-101 Purifier is a Primary Energy-Based weapon that can fire variable-charge bolts of gas.

## 主要属性

| 字段 | 数值 |
|---|---|
| 类别 (`category`) | primary |
| 子类别 (`subcategory`) | energy_based |
| 特性 ID (`traitIds`) | chargeup, explosive, medium-armor-penetrating |


## 枪械属性

| 字段 | 数值 |
|---|---|
| `firingModes` | — |
| 射速（RPM） (`fireRateRpm`) | 1000 |
| `dps` | 2916 |
| 容量 (`capacity`) | 15 |
| 备用弹匣 (`spareMagazines`) | 6 |
| 初始弹匣 (`startingMagazines`) | 4 |
| `magazinesFromSupply` | 6 |
| `magazinesFromAmmoBox` | 3 |
| 后坐力 (`recoil`) | 15.5 |
| `horizontalRecoil` | 11 |
| `verticalRecoil` | 20 |
| `spread.horizontal` | 10 |
| `spread.vertical` | 10 |
| `sway` | 1 |
| `ergonomics` | 65 |
| `reloadKind` | magazine |
| 装填时间（秒） (`reloadTimeS`) | 2.5 |
| `reloadTimeUpgradedS` | — |
| `tacticalReloadTimeS` | 2.5 |


## 攻击模式、伤害与穿甲

### 1. P（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 200 |
| `damage.durable` | 100 |
| `damage.type` | Ballistic |
| `penetration.direct` | medium |
| `penetration.slightAngle` | medium |
| `penetration.largeAngle` | medium |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | — |
| `projectile.massG` | 25 |
| `projectile.initialVelocityMps` | 550 |
| `projectile.dragFactorPct` | 150 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 35 |
| `area` | — |
| `forces.demolition` | 10 |
| `forces.stagger` | 20 |
| `forces.push` | 10 |


### 2. P IE（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 75 |
| `damage.durable` | 75 |
| `damage.type` | Explosion |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 1 |
| `area.outerRadiusM` | 2 |
| `area.shockwaveRadiusM` | 2 |
| `forces.demolition` | 10 |
| `forces.stagger` | 10 |
| `forces.push` | 7 |


### 3. PLAS-101 P（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 200 |
| `damage.durable` | 100 |
| `damage.type` | Ballistic |
| `penetration.direct` | medium |
| `penetration.slightAngle` | medium |
| `penetration.largeAngle` | medium |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | — |
| `projectile.massG` | 25 |
| `projectile.initialVelocityMps` | 350 |
| `projectile.dragFactorPct` | 150 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 35 |
| `area` | — |
| `forces.demolition` | 10 |
| `forces.stagger` | 20 |
| `forces.push` | 10 |


### 4. PLAS-101 P IE（explosion）

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
| `area.innerRadiusM` | 2.9000001 |
| `area.outerRadiusM` | 3 |
| `area.shockwaveRadiusM` | 4 |
| `forces.demolition` | 10 |
| `forces.stagger` | 35 |
| `forces.push` | 30 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | warbond |
| `label` | Polar Patriots P3 |
| 战争债券 ID (`warbondId`) | polar-patriots |
| `page` | 3 |
| `cost.currency` | medals |
| `cost.amount` | 80 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/weapons/plas-101-purifier.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/PLAS-101_Purifier
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

