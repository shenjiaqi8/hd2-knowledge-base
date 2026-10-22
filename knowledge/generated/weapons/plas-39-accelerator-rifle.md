---
id: "plas-39-accelerator-rifle"
name: "PLAS-39 Accelerator Rifle"
collection: "weapons"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: []
wiki_url: "https://helldivers.wiki.gg/wiki/PLAS-39_Accelerator_Rifle"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/weapons/plas-39-accelerator-rifle.json"
---

# PLAS-39 Accelerator Rifle

**分类：** 武器 (`weapons`) · **ID：** `plas-39-accelerator-rifle`

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/PLAS-39_Accelerator_Rifle

## 简介

The PLAS-39 Accelerator Rifle is a Primary Energy-Based, burst-firing plasma sniper rifle. It is part of the Helldivers 2 x Killzone Legendary Warbond or the Helldivers x Killzone crossover package.

## 主要属性

| 字段 | 数值 |
|---|---|
| 类别 (`category`) | primary |
| 子类别 (`subcategory`) | energy_based |
| 特性 ID (`traitIds`) | explosive, medium-armor-penetrating |


## 枪械属性

| 字段 | 数值 |
|---|---|
| `firingModes` | burst |
| 射速（RPM） (`fireRateRpm`) | 550 |
| `dps` | 3208.33 |
| 容量 (`capacity`) | 9 |
| 备用弹匣 (`spareMagazines`) | 12 |
| 初始弹匣 (`startingMagazines`) | 8 |
| `magazinesFromSupply` | 12 |
| `magazinesFromAmmoBox` | 6 |
| 后坐力 (`recoil`) | 3 |
| `horizontalRecoil` | 3 |
| `verticalRecoil` | 3 |
| `spread.horizontal` | 0.5 |
| `spread.vertical` | 0.5 |
| `sway` | 1 |
| `ergonomics` | 60 |
| `reloadKind` | magazine |
| 装填时间（秒） (`reloadTimeS`) | 3.4 |
| `reloadTimeUpgradedS` | — |
| `tacticalReloadTimeS` | 3.4 |


## 攻击模式、伤害与穿甲

### 1. PLAS-39 P（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 250 |
| `damage.durable` | 125 |
| `damage.type` | Ballistic |
| `penetration.direct` | medium |
| `penetration.slightAngle` | medium |
| `penetration.largeAngle` | medium |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | — |
| `projectile.massG` | 25 |
| `projectile.initialVelocityMps` | 1000 |
| `projectile.dragFactorPct` | 10 |
| `projectile.gravityFactorPct` | 50 |
| `projectile.penetrationSlowdownPct` | 35 |
| `area` | — |
| `forces.demolition` | 10 |
| `forces.stagger` | 15 |
| `forces.push` | 10 |


### 2. PLAS-39 P IE（explosion）

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
| `label` | Righteous Revenants P2 |
| 战争债券 ID (`warbondId`) | righteous-revenants |
| `page` | 2 |
| `cost.currency` | medals |
| `cost.amount` | 50 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/weapons/plas-39-accelerator-rifle.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/PLAS-39_Accelerator_Rifle
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

