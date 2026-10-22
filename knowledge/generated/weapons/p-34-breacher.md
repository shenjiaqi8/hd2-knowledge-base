---
id: "p-34-breacher"
name: "P-34 Breacher"
collection: "weapons"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/P-34_Breacher"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/weapons/p-34-breacher.json"
---

# P-34 Breacher

**分类：** 武器 (`weapons`) · **ID：** `p-34-breacher`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/P-34_Breacher

## 简介

The P-34 Breacher is a Special Secondary single-shot weapon that fires an explosive thermite projectile at targets.

## 主要属性

| 字段 | 数值 |
|---|---|
| 类别 (`category`) | secondary |
| 子类别 (`subcategory`) | special |
| 特性 ID (`traitIds`) | one-handed, anti-tank, sticky, explosive |


## 枪械属性

| 字段 | 数值 |
|---|---|
| `firingModes` | — |
| 射速（RPM） (`fireRateRpm`) | 20 |
| `dps` | — |
| 容量 (`capacity`) | 1 |
| 备用弹匣 (`spareMagazines`) | 2 |
| 初始弹匣 (`startingMagazines`) | 1 |
| `magazinesFromSupply` | 1 |
| `magazinesFromAmmoBox` | 1 |
| 后坐力 (`recoil`) | 312.5 |
| `horizontalRecoil` | 150 |
| `verticalRecoil` | 475 |
| `spread.horizontal` | 8 |
| `spread.vertical` | 8 |
| `sway` | 1 |
| `ergonomics` | 45 |
| `reloadKind` | magazine |
| 装填时间（秒） (`reloadTimeS`) | 2.68 |
| `reloadTimeUpgradedS` | — |
| `tacticalReloadTimeS` | — |


## 攻击模式、伤害与穿甲

### 1. P-34 P（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 60 |
| `damage.durable` | 0 |
| `damage.type` | Ballistic |
| `penetration.direct` | heavy |
| `penetration.slightAngle` | heavy |
| `penetration.largeAngle` | medium |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | — |
| `projectile.massG` | 10 |
| `projectile.initialVelocityMps` | 150 |
| `projectile.dragFactorPct` | 200 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 0 |
| `area` | — |
| `forces.demolition` | 15 |
| `forces.stagger` | 10 |
| `forces.push` | 10 |


### 2. P-34 BREACHER E（explosion）

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
| `area.innerRadiusM` | 1.5 |
| `area.outerRadiusM` | 2.5 |
| `area.shockwaveRadiusM` | 4 |
| `forces.demolition` | 30 |
| `forces.stagger` | 20 |
| `forces.push` | 40 |


### 3. Fire（status）

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


### 4. Thermite（status）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 150 |
| `damage.durable` | 150 |
| `damage.type` | Damage |
| `penetration.direct` | anti_tank_iii |
| `penetration.slightAngle` | anti_tank_iii |
| `penetration.largeAngle` | anti_tank_iii |
| `penetration.extremeAngle` | unarmored |
| `projectile` | — |
| `area` | — |
| `forces.demolition` | 10 |
| `forces.stagger` | 0 |
| `forces.push` | 0 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | warbond |
| `label` | Ironclad DemocracyP2 |
| 战争债券 ID (`warbondId`) | ironclad-democracy |
| `page` | 2 |
| `cost.currency` | medals |
| `cost.amount` | 50 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/weapons/p-34-breacher.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/P-34_Breacher
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

