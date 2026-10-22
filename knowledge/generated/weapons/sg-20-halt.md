---
id: "sg-20-halt"
name: "SG-20 Halt"
collection: "weapons"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/SG-20_Halt"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/weapons/sg-20-halt.json"
---

# SG-20 Halt

**分类：** 武器 (`weapons`) · **ID：** `sg-20-halt`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/SG-20_Halt

## 简介

The SG-20 Halt is a dual-tube, pump-action Primary Shotgun. It can switch between Medium-armor penetrating flechettes and Light-armor penetrating stun pellets.

## 主要属性

| 字段 | 数值 |
|---|---|
| 类别 (`category`) | primary |
| 子类别 (`subcategory`) | shotgun |
| 特性 ID (`traitIds`) | light-armor-penetrating, medium-armor-penetrating, rounds-reload |


## 枪械属性

| 字段 | 数值 |
|---|---|
| `firingModes` | semi |
| 射速（RPM） (`fireRateRpm`) | 80 |
| `dps` | 513, 160 |
| 容量 (`capacity`) | 16 |
| 备用弹匣 (`spareMagazines`) | 60 |
| 初始弹匣 (`startingMagazines`) | 32 |
| `magazinesFromSupply` | 60 |
| `magazinesFromAmmoBox` | 30 |
| 后坐力 (`recoil`) | 82.5 |
| `horizontalRecoil` | 45 |
| `verticalRecoil` | 120 |
| `spread.horizontal` | 300 |
| `spread.vertical` | 200 |
| `sway` | 1 |
| `ergonomics` | 65 |
| `reloadKind` | rounds |
| 装填时间（秒） (`reloadTimeS`) | 3.7 |
| `reloadTimeUpgradedS` | — |
| `tacticalReloadTimeS` | — |


## 攻击模式、伤害与穿甲

### 1. SG-20 P（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 35 |
| `damage.durable` | 10 |
| `damage.type` | Ballistic |
| `penetration.direct` | medium |
| `penetration.slightAngle` | medium |
| `penetration.largeAngle` | medium |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | 11 |
| `projectile.massG` | 6 |
| `projectile.initialVelocityMps` | 385 |
| `projectile.dragFactorPct` | 30 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 10 |
| `forces.stagger` | 20 |
| `forces.push` | 20 |


### 2. SG-20 P1（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 6 |
| `damage.durable` | 2 |
| `damage.type` | Ballistic |
| `penetration.direct` | light |
| `penetration.slightAngle` | light |
| `penetration.largeAngle` | light |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | 20 |
| `projectile.massG` | 4.5 |
| `projectile.initialVelocityMps` | 800 |
| `projectile.dragFactorPct` | 30 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 10 |
| `forces.stagger` | 15 |
| `forces.push` | 10 |


### 3. Stun Large（status）

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
| `label` | Truth Enforcers P1 |
| 战争债券 ID (`warbondId`) | truth-enforcers |
| `page` | 1 |
| `cost.currency` | medals |
| `cost.amount` | 20 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/weapons/sg-20-halt.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/SG-20_Halt
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

