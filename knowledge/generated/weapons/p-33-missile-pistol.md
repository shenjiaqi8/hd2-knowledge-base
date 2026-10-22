---
id: "p-33-missile-pistol"
name: "P-33 Missile Pistol"
collection: "weapons"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/P-33_Missile_Pistol"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/weapons/p-33-missile-pistol.json"
---

# P-33 Missile Pistol

**分类：** 武器 (`weapons`) · **ID：** `p-33-missile-pistol`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/P-33_Missile_Pistol

## 简介

The P-33 Missile Pistol is a Secondary Special single-shot weapon that fires guided missiles at targets.

## 主要属性

| 字段 | 数值 |
|---|---|
| 类别 (`category`) | secondary |
| 子类别 (`subcategory`) | special |
| 特性 ID (`traitIds`) | medium-armor-penetrating, anti-tank, one-handed, guided, explosive |


## 枪械属性

| 字段 | 数值 |
|---|---|
| `firingModes` | other |
| 射速（RPM） (`fireRateRpm`) | 60 |
| `dps` | 1300 |
| 容量 (`capacity`) | 1 |
| 备用弹匣 (`spareMagazines`) | 3 |
| 初始弹匣 (`startingMagazines`) | 1 |
| `magazinesFromSupply` | 2 |
| `magazinesFromAmmoBox` | 1 |
| 后坐力 (`recoil`) | 312.5 |
| `horizontalRecoil` | 150 |
| `verticalRecoil` | 475 |
| `spread.horizontal` | 8 |
| `spread.vertical` | 8 |
| `sway` | 1 |
| `ergonomics` | 45 |
| `reloadKind` | magazine |
| 装填时间（秒） (`reloadTimeS`) | 2.7 |
| `reloadTimeUpgradedS` | — |
| `tacticalReloadTimeS` | — |


## 攻击模式、伤害与穿甲

### 1. P-33 P（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 1000 |
| `damage.durable` | 1000 |
| `damage.type` | Ballistic |
| `penetration.direct` | anti_tank_i |
| `penetration.slightAngle` | anti_tank_i |
| `penetration.largeAngle` | anti_tank_i |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | — |
| `projectile.massG` | 15 |
| `projectile.initialVelocityMps` | 1 |
| `projectile.dragFactorPct` | 0 |
| `projectile.gravityFactorPct` | 0 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 30 |
| `forces.stagger` | 40 |
| `forces.push` | 25 |


### 2. P-33 P IE（explosion）

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
| `area.innerRadiusM` | 2 |
| `area.outerRadiusM` | 4 |
| `area.shockwaveRadiusM` | 12 |
| `forces.demolition` | 30 |
| `forces.stagger` | 40 |
| `forces.push` | 40 |


### 3. P-33 P1（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 1000 |
| `damage.durable` | 1000 |
| `damage.type` | Ballistic |
| `penetration.direct` | anti_tank_i |
| `penetration.slightAngle` | anti_tank_i |
| `penetration.largeAngle` | anti_tank_i |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | — |
| `projectile.massG` | 15 |
| `projectile.initialVelocityMps` | 1 |
| `projectile.dragFactorPct` | 0 |
| `projectile.gravityFactorPct` | 0 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 30 |
| `forces.stagger` | 40 |
| `forces.push` | 25 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | warbond |
| `label` | Exo Experts P2 |
| 战争债券 ID (`warbondId`) | exo-experts |
| `page` | 2 |
| `cost.currency` | medals |
| `cost.amount` | 50 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/weapons/p-33-missile-pistol.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/P-33_Missile_Pistol
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

