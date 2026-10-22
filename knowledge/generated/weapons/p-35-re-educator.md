---
id: "p-35-re-educator"
name: "P-35 Re-Educator"
collection: "weapons"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/P-35_Re-Educator"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/weapons/p-35-re-educator.json"
---

# P-35 Re-Educator

**分类：** 武器 (`weapons`) · **ID：** `p-35-re-educator`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/P-35_Re-Educator

## 简介

The P-35 Re-Educator is a Secondary Special pistol that fires Gas darts to disorient enemies.

## 主要属性

| 字段 | 数值 |
|---|---|
| 类别 (`category`) | secondary |
| 子类别 (`subcategory`) | special |
| 特性 ID (`traitIds`) | one-handed, caustic, heavy-armor-penetrating |


## 枪械属性

| 字段 | 数值 |
|---|---|
| `firingModes` | semi |
| 射速（RPM） (`fireRateRpm`) | 110 |
| `dps` | 110 |
| 容量 (`capacity`) | 6 |
| 备用弹匣 (`spareMagazines`) | 2 |
| 初始弹匣 (`startingMagazines`) | 2 |
| `magazinesFromSupply` | 2 |
| `magazinesFromAmmoBox` | 1 |
| 后坐力 (`recoil`) | 10 |
| `horizontalRecoil` | 5 |
| `verticalRecoil` | 15 |
| `spread.horizontal` | 5 |
| `spread.vertical` | 5 |
| `sway` | 1 |
| `ergonomics` | 100 |
| `reloadKind` | magazine |
| 装填时间（秒） (`reloadTimeS`) | 3 |
| `reloadTimeUpgradedS` | — |
| `tacticalReloadTimeS` | 3 |


## 攻击模式、伤害与穿甲

### 1. P-35 P（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 60 |
| `damage.durable` | 10 |
| `damage.type` | Gas |
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
| `forces.demolition` | 1 |
| `forces.stagger` | 1 |
| `forces.push` | 1 |


### 2. Gas（status）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 25 |
| `damage.durable` | 25 |
| `damage.type` | Gas |
| `penetration.direct` | anti_tank_ii |
| `penetration.slightAngle` | anti_tank_ii |
| `penetration.largeAngle` | anti_tank_ii |
| `penetration.extremeAngle` | unarmored |
| `projectile` | — |
| `area` | — |
| `forces.demolition` | 0 |
| `forces.stagger` | 0 |
| `forces.push` | 0 |


### 3. Gas Confusion（status）

| 字段 | 数值 |
|---|---|
| `damage.standard` | — |
| `damage.durable` | — |
| `damage.type` | — |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area` | — |
| `forces.demolition` | — |
| `forces.stagger` | — |
| `forces.push` | — |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | warbond |
| `label` | Redacted Regiment P1 |
| 战争债券 ID (`warbondId`) | redacted-regiment |
| `page` | 1 |
| `cost.currency` | medals |
| `cost.amount` | 20 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/weapons/p-35-re-educator.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/P-35_Re-Educator
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

