---
id: "plas-1-scorcher"
name: "PLAS-1 Scorcher"
collection: "weapons"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/PLAS-1_Scorcher"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/weapons/plas-1-scorcher.json"
---

# PLAS-1 Scorcher

**分类：** 武器 (`weapons`) · **ID：** `plas-1-scorcher`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/PLAS-1_Scorcher

## 简介

The PLAS-1 Scorcher is a Primary Energy-Based weapon that fires explosive energy projectiles.

## 主要属性

| 字段 | 数值 |
|---|---|
| 类别 (`category`) | primary |
| 子类别 (`subcategory`) | energy_based |
| 特性 ID (`traitIds`) | light-armor-penetrating, explosive |


## 枪械属性

| 字段 | 数值 |
|---|---|
| `firingModes` | semi, auto |
| 射速（RPM） (`fireRateRpm`) | 350 |
| `dps` | 1166 |
| 容量 (`capacity`) | 20 |
| 备用弹匣 (`spareMagazines`) | 5 |
| 初始弹匣 (`startingMagazines`) | 3 |
| `magazinesFromSupply` | 5 |
| `magazinesFromAmmoBox` | 2 |
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

### 1. PLAS-1 P（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 100 |
| `damage.durable` | 50 |
| `damage.type` | Ballistic |
| `penetration.direct` | light |
| `penetration.slightAngle` | light |
| `penetration.largeAngle` | light |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | — |
| `projectile.massG` | 25 |
| `projectile.initialVelocityMps` | 550 |
| `projectile.dragFactorPct` | 150 |
| `projectile.gravityFactorPct` | 50 |
| `projectile.penetrationSlowdownPct` | 35 |
| `area` | — |
| `forces.demolition` | 10 |
| `forces.stagger` | 20 |
| `forces.push` | 10 |


### 2. PLAS-1 P IE（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 100 |
| `damage.durable` | 100 |
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


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | warbond |
| `label` | Helldivers Mobilize! P10 |
| 战争债券 ID (`warbondId`) | helldivers-mobilize |
| `page` | 10 |
| `cost.currency` | medals |
| `cost.amount` | 75 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/weapons/plas-1-scorcher.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/PLAS-1_Scorcher
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

