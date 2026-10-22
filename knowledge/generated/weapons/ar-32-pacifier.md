---
id: "ar-32-pacifier"
name: "AR-32 Pacifier"
collection: "weapons"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/AR-32_Pacifier"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/weapons/ar-32-pacifier.json"
---

# AR-32 Pacifier

**分类：** 武器 (`weapons`) · **ID：** `ar-32-pacifier`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/AR-32_Pacifier

## 简介

The AR-32 Pacifier is a Primary Assault Rifle that fires Medium armor penetration stun rounds in exchange for significantly lower damage output compared to most other primaries.

## 主要属性

| 字段 | 数值 |
|---|---|
| 类别 (`category`) | primary |
| 子类别 (`subcategory`) | assault_rifle |
| 特性 ID (`traitIds`) | medium-armor-penetrating, stun |


## 枪械属性

| 字段 | 数值 |
|---|---|
| `firingModes` | auto, semi, burst |
| 射速（RPM） (`fireRateRpm`) | 700 |
| `dps` | 641.66 |
| 容量 (`capacity`) | 40 |
| 备用弹匣 (`spareMagazines`) | 8 |
| 初始弹匣 (`startingMagazines`) | 6 |
| `magazinesFromSupply` | 8 |
| `magazinesFromAmmoBox` | 4 |
| 后坐力 (`recoil`) | 17.5 |
| `horizontalRecoil` | 12.5 |
| `verticalRecoil` | 22.5 |
| `spread.horizontal` | 4 |
| `spread.vertical` | 4 |
| `sway` | 1 |
| `ergonomics` | 60 |
| `reloadKind` | magazine |
| 装填时间（秒） (`reloadTimeS`) | 3 |
| `reloadTimeUpgradedS` | — |
| `tacticalReloadTimeS` | 1.85 |


## 攻击模式、伤害与穿甲

### 1. AR-32 P（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 55 |
| `damage.durable` | 10 |
| `damage.type` | Ballistic |
| `penetration.direct` | medium |
| `penetration.slightAngle` | medium |
| `penetration.largeAngle` | medium |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | — |
| `projectile.massG` | 4.5 |
| `projectile.initialVelocityMps` | 900 |
| `projectile.dragFactorPct` | 30 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 10 |
| `forces.stagger` | 15 |
| `forces.push` | 10 |


### 2. Stun Medium（status）

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
| `label` | Force of Law P1 |
| 战争债券 ID (`warbondId`) | force-of-law |
| `page` | 1 |
| `cost.currency` | medals |
| `cost.amount` | 35 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/weapons/ar-32-pacifier.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/AR-32_Pacifier
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

