---
id: "gp-31-grenade-pistol"
name: "GP-31 Grenade Pistol"
collection: "weapons"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/GP-31_Grenade_Pistol"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/weapons/gp-31-grenade-pistol.json"
---

# GP-31 Grenade Pistol

**分类：** 武器 (`weapons`) · **ID：** `gp-31-grenade-pistol`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/GP-31_Grenade_Pistol

## 简介

The GP-31 Grenade Pistol is a Secondary Special single-shot weapon that fires a powerful grenade at a medium range.

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
| 备用弹匣 (`spareMagazines`) | 6 |
| 初始弹匣 (`startingMagazines`) | 4 |
| `magazinesFromSupply` | 4 |
| `magazinesFromAmmoBox` | 2 |
| 后坐力 (`recoil`) | 30.75 |
| `horizontalRecoil` | 11.5 |
| `verticalRecoil` | 50 |
| `spread.horizontal` | 30 |
| `spread.vertical` | 30 |
| `sway` | 1 |
| `ergonomics` | 95 |
| `reloadKind` | magazine |
| 装填时间（秒） (`reloadTimeS`) | 1.72 |
| `reloadTimeUpgradedS` | — |
| `tacticalReloadTimeS` | — |


## 攻击模式、伤害与穿甲

### 1. GP-31 P（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 250 |
| `damage.durable` | 250 |
| `damage.type` | Ballistic |
| `penetration.direct` | medium |
| `penetration.slightAngle` | medium |
| `penetration.largeAngle` | medium |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | — |
| `projectile.massG` | 50 |
| `projectile.initialVelocityMps` | 100 |
| `projectile.dragFactorPct` | 120 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 30 |
| `forces.stagger` | 40 |
| `forces.push` | 10 |


### 2. GP-31 P IE（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 400 |
| `damage.durable` | 400 |
| `damage.type` | Explosion |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 2.25 |
| `area.outerRadiusM` | 6.5 |
| `area.shockwaveRadiusM` | 8 |
| `forces.demolition` | 30 |
| `forces.stagger` | 25 |
| `forces.push` | 30 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | warbond |
| `label` | Democratic Detonation P3 |
| 战争债券 ID (`warbondId`) | democratic-detonation |
| `page` | 3 |
| `cost.currency` | medals |
| `cost.amount` | 60 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/weapons/gp-31-grenade-pistol.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/GP-31_Grenade_Pistol
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

