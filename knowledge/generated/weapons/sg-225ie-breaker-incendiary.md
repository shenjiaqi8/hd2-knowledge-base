---
id: "sg-225ie-breaker-incendiary"
name: "SG-225IE Breaker Incendiary"
collection: "weapons"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/SG-225IE_Breaker_Incendiary"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/weapons/sg-225ie-breaker-incendiary.json"
---

# SG-225IE Breaker Incendiary

**分类：** 武器 (`weapons`) · **ID：** `sg-225ie-breaker-incendiary`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/SG-225IE_Breaker_Incendiary

## 简介

The SG-225IE Breaker Incendiary is a burst fire Primary Shotgun, a variant of the standard Breaker that fires incendiary buckshot.

## 主要属性

| 字段 | 数值 |
|---|---|
| 类别 (`category`) | primary |
| 子类别 (`subcategory`) | shotgun |
| 特性 ID (`traitIds`) | light-armor-penetrating, incendiary |


## 枪械属性

| 字段 | 数值 |
|---|---|
| `firingModes` | burst, semi |
| 射速（RPM） (`fireRateRpm`) | 300 |
| `dps` | 1200 |
| 容量 (`capacity`) | 26 |
| 备用弹匣 (`spareMagazines`) | 4 |
| 初始弹匣 (`startingMagazines`) | 3 |
| `magazinesFromSupply` | 4 |
| `magazinesFromAmmoBox` | 2 |
| 后坐力 (`recoil`) | 32.5 |
| `horizontalRecoil` | 22.5 |
| `verticalRecoil` | 42.5 |
| `spread.horizontal` | 300 |
| `spread.vertical` | 300 |
| `sway` | 1 |
| `ergonomics` | 65 |
| `reloadKind` | magazine |
| 装填时间（秒） (`reloadTimeS`) | 3 |
| `reloadTimeUpgradedS` | — |
| `tacticalReloadTimeS` | — |


## 攻击模式、伤害与穿甲

### 1. SG-225IE P（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 20 |
| `damage.durable` | 10 |
| `damage.type` | Ballistic |
| `penetration.direct` | light |
| `penetration.slightAngle` | light |
| `penetration.largeAngle` | light |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | 12 |
| `projectile.massG` | 2 |
| `projectile.initialVelocityMps` | 120 |
| `projectile.dragFactorPct` | 80 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 100 |
| `area` | — |
| `forces.demolition` | 10 |
| `forces.stagger` | 10 |
| `forces.push` | 10 |


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
| `label` | Steeled Veterans P2 |
| 战争债券 ID (`warbondId`) | steeled-veterans |
| `page` | 2 |
| `cost.currency` | medals |
| `cost.amount` | 60 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/weapons/sg-225ie-breaker-incendiary.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/SG-225IE_Breaker_Incendiary
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

