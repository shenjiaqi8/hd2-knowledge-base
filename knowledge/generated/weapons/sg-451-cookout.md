---
id: "sg-451-cookout"
name: "SG-451 Cookout"
collection: "weapons"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/SG-451_Cookout"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/weapons/sg-451-cookout.json"
---

# SG-451 Cookout

**分类：** 武器 (`weapons`) · **ID：** `sg-451-cookout`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/SG-451_Cookout

## 简介

The SG-451 Cookout is a Primary Shotgun, a variant of the standard Punisher that fires incendiary buckshot.

## 主要属性

| 字段 | 数值 |
|---|---|
| 类别 (`category`) | primary |
| 子类别 (`subcategory`) | shotgun |
| 特性 ID (`traitIds`) | light-armor-penetrating, rounds-reload, incendiary |


## 枪械属性

| 字段 | 数值 |
|---|---|
| `firingModes` | semi |
| 射速（RPM） (`fireRateRpm`) | 80 |
| `dps` | 426.67 |
| 容量 (`capacity`) | 16 |
| 备用弹匣 (`spareMagazines`) | 60 |
| 初始弹匣 (`startingMagazines`) | 32 |
| `magazinesFromSupply` | 60 |
| `magazinesFromAmmoBox` | 30 |
| 后坐力 (`recoil`) | 71.25 |
| `horizontalRecoil` | 42.5 |
| `verticalRecoil` | 100 |
| `spread.horizontal` | 180 |
| `spread.vertical` | 140 |
| `sway` | 1 |
| `ergonomics` | 65 |
| `reloadKind` | rounds |
| 装填时间（秒） (`reloadTimeS`) | 6.45 |
| `reloadTimeUpgradedS` | — |
| `tacticalReloadTimeS` | — |


## 攻击模式、伤害与穿甲

### 1. SG-451 P（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 16 |
| `damage.durable` | 3 |
| `damage.type` | Ballistic |
| `penetration.direct` | light |
| `penetration.slightAngle` | light |
| `penetration.largeAngle` | light |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | 20 |
| `projectile.massG` | 2 |
| `projectile.initialVelocityMps` | 120 |
| `projectile.dragFactorPct` | 80 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 100 |
| `area` | — |
| `forces.demolition` | 10 |
| `forces.stagger` | 35 |
| `forces.push` | 20 |


### 2. Fire（status）

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


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | warbond |
| `label` | Freedom's Flame P1 |
| 战争债券 ID (`warbondId`) | freedoms-flame |
| `page` | 1 |
| `cost.currency` | medals |
| `cost.amount` | 20 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/weapons/sg-451-cookout.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/SG-451_Cookout
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

