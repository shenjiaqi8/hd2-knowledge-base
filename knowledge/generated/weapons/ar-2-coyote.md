---
id: "ar-2-coyote"
name: "AR-2 Coyote"
collection: "weapons"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/AR-2_Coyote"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/weapons/ar-2-coyote.json"
---

# AR-2 Coyote

**分类：** 武器 (`weapons`) · **ID：** `ar-2-coyote`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/AR-2_Coyote

## 简介

The AR-2 Coyote is a Primary Assault Rifle that fires Medium armor penetration incendiary rounds.

## 主要属性

| 字段 | 数值 |
|---|---|
| 类别 (`category`) | primary |
| 子类别 (`subcategory`) | assault_rifle |
| 特性 ID (`traitIds`) | incendiary, medium-armor-penetrating |


## 枪械属性

| 字段 | 数值 |
|---|---|
| `firingModes` | auto, semi |
| 射速（RPM） (`fireRateRpm`) | 600 |
| `dps` | 750 |
| 容量 (`capacity`) | 45 |
| 备用弹匣 (`spareMagazines`) | 8 |
| 初始弹匣 (`startingMagazines`) | 6 |
| `magazinesFromSupply` | 8 |
| `magazinesFromAmmoBox` | 4 |
| 后坐力 (`recoil`) | 19.75 |
| `horizontalRecoil` | 11.5 |
| `verticalRecoil` | 28 |
| `spread.horizontal` | 4 |
| `spread.vertical` | 4 |
| `sway` | 1 |
| `ergonomics` | 50 |
| `reloadKind` | magazine |
| 装填时间（秒） (`reloadTimeS`) | 3 |
| `reloadTimeUpgradedS` | — |
| `tacticalReloadTimeS` | 2 |


## 攻击模式、伤害与穿甲

### 1. AR-2 P（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 75 |
| `damage.durable` | 10 |
| `damage.type` | Ballistic |
| `penetration.direct` | medium |
| `penetration.slightAngle` | medium |
| `penetration.largeAngle` | medium |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | — |
| `projectile.massG` | 8 |
| `projectile.initialVelocityMps` | 650 |
| `projectile.dragFactorPct` | 30 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 10 |
| `forces.stagger` | 12 |
| `forces.push` | 12 |


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
| `label` | Dust Devils P1 |
| 战争债券 ID (`warbondId`) | dust-devils |
| `page` | 1 |
| `cost.currency` | medals |
| `cost.amount` | 35 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/weapons/ar-2-coyote.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/AR-2_Coyote
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

