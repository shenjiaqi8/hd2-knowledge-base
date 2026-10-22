---
id: "sg-97-sweeper"
name: "SG-97 Sweeper"
collection: "weapons"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/SG-97_Sweeper"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/weapons/sg-97-sweeper.json"
---

# SG-97 Sweeper

**分类：** 武器 (`weapons`) · **ID：** `sg-97-sweeper`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/SG-97_Sweeper

## 简介

The SG-97 Sweeper is a Primary Shotgun with Medium armor penetrating flechettes, able to inflict high damage per round in exchange for a significantly reduced magazine size. It is affixed with a bayonet, improving melee damage and range.

## 主要属性

| 字段 | 数值 |
|---|---|
| 类别 (`category`) | primary |
| 子类别 (`subcategory`) | shotgun |
| 特性 ID (`traitIds`) | medium-armor-penetrating, rounds-reload |


## 枪械属性

| 字段 | 数值 |
|---|---|
| `firingModes` | auto |
| 射速（RPM） (`fireRateRpm`) | 150 |
| `dps` | 1260 |
| 容量 (`capacity`) | 7 |
| 备用弹匣 (`spareMagazines`) | 70 |
| 初始弹匣 (`startingMagazines`) | 46 |
| `magazinesFromSupply` | 70 |
| `magazinesFromAmmoBox` | 35 |
| 后坐力 (`recoil`) | 76.25 |
| `horizontalRecoil` | 57.5 |
| `verticalRecoil` | 95 |
| `spread.horizontal` | 125 |
| `spread.vertical` | 105 |
| `sway` | 1 |
| `ergonomics` | 65 |
| `reloadKind` | rounds |
| 装填时间（秒） (`reloadTimeS`) | 4 |
| `reloadTimeUpgradedS` | — |
| `tacticalReloadTimeS` | — |


## 攻击模式、伤害与穿甲

### 1. SG-97 P（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 42 |
| `damage.durable` | 11 |
| `damage.type` | Ballistic |
| `penetration.direct` | medium |
| `penetration.slightAngle` | medium |
| `penetration.largeAngle` | medium |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | 12 |
| `projectile.massG` | 10 |
| `projectile.initialVelocityMps` | 385 |
| `projectile.dragFactorPct` | 30 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 10 |
| `forces.stagger` | 20 |
| `forces.push` | 20 |


### 2. Bayonet Melee（melee）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 165 |
| `damage.durable` | 83 |
| `damage.type` | Melee |
| `penetration.direct` | medium |
| `penetration.slightAngle` | unarmored |
| `penetration.largeAngle` | unarmored |
| `penetration.extremeAngle` | unarmored |
| `projectile` | — |
| `area` | — |
| `forces.demolition` | 10 |
| `forces.stagger` | 25 |
| `forces.push` | 30 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | superstore |
| `label` | Superstore |
| 战争债券 ID (`warbondId`) | — |
| `page` | — |
| `cost.currency` | super_credits |
| `cost.amount` | 400 |
| `rotating` | 否 |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/weapons/sg-97-sweeper.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/SG-97_Sweeper
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

