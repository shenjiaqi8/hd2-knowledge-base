---
id: "sg-8p-punisher-plasma"
name: "SG-8P Punisher Plasma"
collection: "weapons"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/SG-8P_Punisher_Plasma"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/weapons/sg-8p-punisher-plasma.json"
---

# SG-8P Punisher Plasma

**分类：** 武器 (`weapons`) · **ID：** `sg-8p-punisher-plasma`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/SG-8P_Punisher_Plasma

## 简介

The SG-8P Punisher Plasma is a Primary Energy-Based weapon, a variant of the standard Punisher that fires Medium armor penetrating, exploding plasma rounds.

## 主要属性

| 字段 | 数值 |
|---|---|
| 类别 (`category`) | primary |
| 子类别 (`subcategory`) | energy_based |
| 特性 ID (`traitIds`) | explosive |


## 枪械属性

| 字段 | 数值 |
|---|---|
| `firingModes` | semi |
| 射速（RPM） (`fireRateRpm`) | 80 |
| `dps` | 299.99 |
| 容量 (`capacity`) | 10 |
| 备用弹匣 (`spareMagazines`) | 8 |
| 初始弹匣 (`startingMagazines`) | 6 |
| `magazinesFromSupply` | 8 |
| `magazinesFromAmmoBox` | 4 |
| 后坐力 (`recoil`) | 77.5 |
| `horizontalRecoil` | 45 |
| `verticalRecoil` | 110 |
| `spread.horizontal` | 8 |
| `spread.vertical` | 8 |
| `sway` | 1 |
| `ergonomics` | 65 |
| `reloadKind` | magazine |
| 装填时间（秒） (`reloadTimeS`) | 2.5 |
| `reloadTimeUpgradedS` | — |
| `tacticalReloadTimeS` | 2.5 |


## 攻击模式、伤害与穿甲

### 1. SG-8P P（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 0 |
| `damage.durable` | 0 |
| `damage.type` | Ballistic |
| `penetration.direct` | light |
| `penetration.slightAngle` | light |
| `penetration.largeAngle` | light |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | — |
| `projectile.massG` | 100 |
| `projectile.initialVelocityMps` | 90 |
| `projectile.dragFactorPct` | 400 |
| `projectile.gravityFactorPct` | 300 |
| `projectile.penetrationSlowdownPct` | 35 |
| `area` | — |
| `forces.demolition` | 10 |
| `forces.stagger` | 20 |
| `forces.push` | 10 |


### 2. SG-8P P IE（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 225 |
| `damage.durable` | 225 |
| `damage.type` | Explosion |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 2.29999995 |
| `area.outerRadiusM` | 3 |
| `area.shockwaveRadiusM` | 4 |
| `forces.demolition` | 10 |
| `forces.stagger` | 35 |
| `forces.push` | 30 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | warbond |
| `label` | Cutting Edge P2 |
| 战争债券 ID (`warbondId`) | cutting-edge |
| `page` | 2 |
| `cost.currency` | medals |
| `cost.amount` | 60 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/weapons/sg-8p-punisher-plasma.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/SG-8P_Punisher_Plasma
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

