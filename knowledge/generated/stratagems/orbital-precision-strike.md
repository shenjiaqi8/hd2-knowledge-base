---
id: "orbital-precision-strike"
name: "Orbital Precision Strike"
collection: "stratagems"
aliases: ["OPS"]
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/Orbital_Precision_Strike"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/orbital-precision-strike.json"
---

# Orbital Precision Strike

**分类：** 战略配备 (`stratagems`) · **ID：** `orbital-precision-strike`

**别名：** OPS

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/Orbital_Precision_Strike

## 简介

The Orbital Precision Strike, abbreviated as OPS, is a Stratagem in the Bridge category that fires a heavy-caliber artillery shell precisely at the Stratagem beacon.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | offensive |
| `availability` | loadout |
| 类别 (`category`) | bridge |
| 类型 (`kind`) | orbital |
| 特性 ID (`traitIds`) | explosive, orbital, anti-tank |
| 输入指令 (`code`) | right, right, up |
| 冷却时间（秒） (`cooldownS`) | 80 |
| `cooldownVariants\[1\].label` | With Morale Augmentation |
| `cooldownVariants\[1\].seconds` | 76 |
| `cooldownVariants\[2\].label` | With Zero-G Breech Loading |
| `cooldownVariants\[2\].seconds` | 72 |
| `cooldownVariants\[3\].label` | With All Upgrades |
| `cooldownVariants\[3\].seconds` | 68.4 |
| 呼叫时间（秒） (`callInTimeS`) | 4.45 |
| `callInTimeUpgradedS` | 3.45 |
| 使用次数 (`uses`) | unlimited |
| `unlockLevel` | 1 |
| `shipModules\[1\].department` | orbital_cannons |
| `shipModules\[1\].module` | Exploding Shrapnel |
| `shipModules\[1\].effect` | Reduces damage falloff from the center of explosions caused by orbital Stratagems. |
| `shipModules\[2\].department` | orbital_cannons |
| `shipModules\[2\].module` | Zero-G Breech Loading |
| `shipModules\[2\].effect` | Orbital stratagem cooldown time reduced by 10%. |
| `shipModules\[3\].department` | orbital_cannons |
| `shipModules\[3\].module` | High-Density Explosives |
| `shipModules\[3\].effect` | Increases the damage radius on explosions caused by orbital Stratagems by 10%. |
| `shipModules\[4\].department` | bridge |
| `shipModules\[4\].module` | Targeting Software Upgrade |
| `shipModules\[4\].effect` | 1-second reduction in call-in time for all Orbital Stratagems. |
| `shipModules\[5\].department` | bridge |
| `shipModules\[5\].module` | Morale Augmentation |
| `shipModules\[5\].effect` | Reduces cooldown time for all Stratagems by 5%. |


## 攻击模式、伤害与穿甲

### 1. S P13（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 4000 |
| `damage.durable` | 4000 |
| `damage.type` | Ballistic |
| `penetration.direct` | anti_tank_iv |
| `penetration.slightAngle` | anti_tank_iii |
| `penetration.largeAngle` | anti_tank_ii |
| `penetration.extremeAngle` | anti_tank_ii |
| `projectile.pellets` | — |
| `projectile.massG` | 30000 |
| `projectile.initialVelocityMps` | 400 |
| `projectile.dragFactorPct` | 0 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 50 |
| `forces.stagger` | 50 |
| `forces.push` | 20 |


### 2. S P13 IE（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 1500 |
| `damage.durable` | 1500 |
| `damage.type` | Explosion |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 4 |
| `area.outerRadiusM` | 12 |
| `area.shockwaveRadiusM` | 18 |
| `forces.demolition` | 50 |
| `forces.stagger` | 70 |
| `forces.push` | 60 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | requisition |
| `label` | Bridge |
| 战争债券 ID (`warbondId`) | — |
| `page` | — |
| `cost.currency` | requisition |
| `cost.amount` | 0 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/orbital-precision-strike.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/Orbital_Precision_Strike
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

