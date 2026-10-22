---
id: "gp-20-ultimatum"
name: "GP-20 Ultimatum"
collection: "weapons"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/GP-20_Ultimatum"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/weapons/gp-20-ultimatum.json"
---

# GP-20 Ultimatum

**分类：** 武器 (`weapons`) · **ID：** `gp-20-ultimatum`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/GP-20_Ultimatum

## 简介

The Ultimatum is a Secondary Special, powerful single-shot weapon that fires extremely destructive explosive rounds.

## 主要属性

| 字段 | 数值 |
|---|---|
| 类别 (`category`) | secondary |
| 子类别 (`subcategory`) | special |
| 特性 ID (`traitIds`) | one-handed, explosive |


## 枪械属性

| 字段 | 数值 |
|---|---|
| `firingModes` | — |
| 射速（RPM） (`fireRateRpm`) | 900 |
| `dps` | — |
| 容量 (`capacity`) | 1 |
| 备用弹匣 (`spareMagazines`) | 1 |
| 初始弹匣 (`startingMagazines`) | 0 |
| `magazinesFromSupply` | 1 |
| `magazinesFromAmmoBox` | 1 |
| 后坐力 (`recoil`) | 30.75 |
| `horizontalRecoil` | 11.5 |
| `verticalRecoil` | 50 |
| `spread.horizontal` | 50 |
| `spread.vertical` | 50 |
| `sway` | 1 |
| `ergonomics` | 35 |
| `reloadKind` | magazine |
| 装填时间（秒） (`reloadTimeS`) | 3 |
| `reloadTimeUpgradedS` | — |
| `tacticalReloadTimeS` | — |


## 攻击模式、伤害与穿甲

### 1. GP-20 P（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 1000 |
| `damage.durable` | 1000 |
| `damage.type` | Ballistic |
| `penetration.direct` | anti_tank_ii |
| `penetration.slightAngle` | anti_tank_ii |
| `penetration.largeAngle` | anti_tank_ii |
| `penetration.extremeAngle` | anti_tank_ii |
| `projectile.pellets` | — |
| `projectile.massG` | 500 |
| `projectile.initialVelocityMps` | 20 |
| `projectile.dragFactorPct` | 50 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 40 |
| `forces.stagger` | 50 |
| `forces.push` | 20 |


### 2. GP-20 P IE（explosion）

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
| `area.innerRadiusM` | 2 |
| `area.outerRadiusM` | 12 |
| `area.shockwaveRadiusM` | 25 |
| `forces.demolition` | 40 |
| `forces.stagger` | 70 |
| `forces.push` | 60 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | warbond |
| `label` | Servants of Freedom P2 |
| 战争债券 ID (`warbondId`) | servants-of-freedom |
| `page` | 2 |
| `cost.currency` | medals |
| `cost.amount` | 40 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/weapons/gp-20-ultimatum.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/GP-20_Ultimatum
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

