---
id: "cb-9-exploding-crossbow"
name: "CB-9 Exploding Crossbow"
collection: "weapons"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/CB-9_Exploding_Crossbow"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/weapons/cb-9-exploding-crossbow.json"
---

# CB-9 Exploding Crossbow

**分类：** 武器 (`weapons`) · **ID：** `cb-9-exploding-crossbow`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/CB-9_Exploding_Crossbow

## 简介

The CB-9 Exploding Crossbow is a Primary Explosive weapon. It fires explosive-tipped crossbow bolts that deal damage in an area.

## 主要属性

| 字段 | 数值 |
|---|---|
| 类别 (`category`) | primary |
| 子类别 (`subcategory`) | explosive |
| 特性 ID (`traitIds`) | explosive, one-handed |


## 枪械属性

| 字段 | 数值 |
|---|---|
| `firingModes` | — |
| 射速（RPM） (`fireRateRpm`) | 50 |
| `dps` | 516 |
| 容量 (`capacity`) | 5 |
| 备用弹匣 (`spareMagazines`) | 8 |
| 初始弹匣 (`startingMagazines`) | 6 |
| `magazinesFromSupply` | 8 |
| `magazinesFromAmmoBox` | 4 |
| 后坐力 (`recoil`) | 26.25 |
| `horizontalRecoil` | 17.5 |
| `verticalRecoil` | 35 |
| `spread.horizontal` | 0.5 |
| `spread.vertical` | 0.5 |
| `sway` | 1 |
| `ergonomics` | 45 |
| `reloadKind` | magazine |
| 装填时间（秒） (`reloadTimeS`) | 3.33 |
| `reloadTimeUpgradedS` | — |
| `tacticalReloadTimeS` | 3.33 |


## 攻击模式、伤害与穿甲

### 1. CB-9 P（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 270 |
| `damage.durable` | 50 |
| `damage.type` | Ballistic |
| `penetration.direct` | medium |
| `penetration.slightAngle` | medium |
| `penetration.largeAngle` | medium |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | — |
| `projectile.massG` | 100 |
| `projectile.initialVelocityMps` | 100 |
| `projectile.dragFactorPct` | 100 |
| `projectile.gravityFactorPct` | 50 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 30 |
| `forces.stagger` | 30 |
| `forces.push` | 10 |


### 2. CB-9 P IE（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 350 |
| `damage.durable` | 350 |
| `damage.type` | Explosion |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 3 |
| `area.outerRadiusM` | 6 |
| `area.shockwaveRadiusM` | 7 |
| `forces.demolition` | 20 |
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
| `cost.amount` | 80 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/weapons/cb-9-exploding-crossbow.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/CB-9_Exploding_Crossbow
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

