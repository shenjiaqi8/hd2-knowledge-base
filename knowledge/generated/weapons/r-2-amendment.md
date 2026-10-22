---
id: "r-2-amendment"
name: "R-2 Amendment"
collection: "weapons"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/R-2_Amendment"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/weapons/r-2-amendment.json"
---

# R-2 Amendment

**分类：** 武器 (`weapons`) · **ID：** `r-2-amendment`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/R-2_Amendment

## 简介

The R-2 Amendment is a Primary Marksman Rifle that can fire in semi-automatic or three-round bursts modes. It is affixed with a bayonet, improving melee damage and range.

## 主要属性

| 字段 | 数值 |
|---|---|
| 类别 (`category`) | primary |
| 子类别 (`subcategory`) | marksman_rifle |
| 特性 ID (`traitIds`) | light-armor-penetrating |


## 枪械属性

| 字段 | 数值 |
|---|---|
| `firingModes` | semi, burst |
| 射速（RPM） (`fireRateRpm`) | 480 |
| `dps` | 1600 |
| 容量 (`capacity`) | 20 |
| 备用弹匣 (`spareMagazines`) | 8 |
| 初始弹匣 (`startingMagazines`) | 6 |
| `magazinesFromSupply` | 8 |
| `magazinesFromAmmoBox` | 4 |
| 后坐力 (`recoil`) | 28.75 |
| `horizontalRecoil` | 17.5 |
| `verticalRecoil` | 40 |
| `spread.horizontal` | 0.1 |
| `spread.vertical` | 0.1 |
| `sway` | 1 |
| `ergonomics` | 50 |
| `reloadKind` | magazine |
| 装填时间（秒） (`reloadTimeS`) | 3.5 |
| `reloadTimeUpgradedS` | — |
| `tacticalReloadTimeS` | 2.8 |


## 攻击模式、伤害与穿甲

### 1. R-2 P（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 200 |
| `damage.durable` | 50 |
| `damage.type` | Ballistic |
| `penetration.direct` | light |
| `penetration.slightAngle` | light |
| `penetration.largeAngle` | light |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | — |
| `projectile.massG` | 20 |
| `projectile.initialVelocityMps` | 850 |
| `projectile.dragFactorPct` | 30 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 10 |
| `forces.stagger` | 20 |
| `forces.push` | 14 |


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
| `type` | warbond |
| `label` | Masters of Ceremony P1 |
| 战争债券 ID (`warbondId`) | masters-of-ceremony |
| `page` | 1 |
| `cost.currency` | medals |
| `cost.amount` | 35 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/weapons/r-2-amendment.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/R-2_Amendment
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

