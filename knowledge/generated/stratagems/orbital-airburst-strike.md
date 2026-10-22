---
id: "orbital-airburst-strike"
name: "Orbital Airburst Strike"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: []
wiki_url: "https://helldivers.wiki.gg/wiki/Orbital_Airburst_Strike"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/orbital-airburst-strike.json"
---

# Orbital Airburst Strike

**分类：** 战略配备 (`stratagems`) · **ID：** `orbital-airburst-strike`

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/Orbital_Airburst_Strike

## 简介

The Orbital Airburst Strike is an offensive Stratagem in Helldivers 2, designed for wiping out large groups of enemy infantry.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | offensive |
| `availability` | loadout |
| 类别 (`category`) | orbital_cannons |
| 类型 (`kind`) | orbital |
| 特性 ID (`traitIds`) | explosive, orbital, medium-armor-penetrating |
| 输入指令 (`code`) | right, right, right |
| 冷却时间（秒） (`cooldownS`) | 90 |
| `cooldownVariants\[1\].label` | With Morale Augmentation |
| `cooldownVariants\[1\].seconds` | 85.5 |
| `cooldownVariants\[2\].label` | With Zero-G Breech Loading |
| `cooldownVariants\[2\].seconds` | 81 |
| `cooldownVariants\[3\].label` | With All Upgrades |
| `cooldownVariants\[3\].seconds` | 76.95 |
| 呼叫时间（秒） (`callInTimeS`) | 4.45 |
| `callInTimeUpgradedS` | 3.45 |
| 使用次数 (`uses`) | unlimited |
| `unlockLevel` | 5 |
| `shipModules\[1\].department` | orbital_cannons |
| `shipModules\[1\].module` | Exploding Shrapnel |
| `shipModules\[1\].effect` | Reduces damage falloff from center of explosions caused by orbital Stratagems. |
| `shipModules\[2\].department` | orbital_cannons |
| `shipModules\[2\].module` | Zero-G Breech Loading |
| `shipModules\[2\].effect` | Orbital stratagem cooldown time reduced by 10%. |
| `shipModules\[3\].department` | orbital_cannons |
| `shipModules\[3\].module` | High-Density Explosives |
| `shipModules\[3\].effect` | Increases damage radius on explosions caused by orbital Stratagems by 10%. |
| `shipModules\[4\].department` | bridge |
| `shipModules\[4\].module` | Targeting Software Upgrade |
| `shipModules\[4\].effect` | 1-second reduction in call-in time for all Orbital Stratagems. |
| `shipModules\[5\].department` | bridge |
| `shipModules\[5\].module` | Morale Augmentation |
| `shipModules\[5\].effect` | Reduces cooldown time for all Stratagems by 5%. |


## 攻击模式、伤害与穿甲

### 1. S P15（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 300 |
| `damage.durable` | 300 |
| `damage.type` | Ballistic |
| `penetration.direct` | anti_tank_iii |
| `penetration.slightAngle` | anti_tank_iii |
| `penetration.largeAngle` | anti_tank_ii |
| `penetration.extremeAngle` | anti_tank_ii |
| `projectile.pellets` | — |
| `projectile.massG` | 5000 |
| `projectile.initialVelocityMps` | 400 |
| `projectile.dragFactorPct` | 0 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 50 |
| `forces.stagger` | 60 |
| `forces.push` | 15 |


### 2. S P15 IE（explosion）

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
| `area.innerRadiusM` | 0.200000003 |
| `area.outerRadiusM` | 0.5 |
| `area.shockwaveRadiusM` | 4 |
| `forces.demolition` | 30 |
| `forces.stagger` | 50 |
| `forces.push` | 40 |


### 3. P14（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 300 |
| `damage.durable` | 150 |
| `damage.type` | Ballistic |
| `penetration.direct` | medium |
| `penetration.slightAngle` | medium |
| `penetration.largeAngle` | medium |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | — |
| `projectile.massG` | 2 |
| `projectile.initialVelocityMps` | 300 |
| `projectile.dragFactorPct` | 50 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 10 |
| `forces.stagger` | 10 |
| `forces.push` | 20 |


### 4. P14 IE（explosion）

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
| `area.shockwaveRadiusM` | 8 |
| `forces.demolition` | 30 |
| `forces.stagger` | 50 |
| `forces.push` | 40 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | requisition |
| `label` | Orbital Cannons |
| 战争债券 ID (`warbondId`) | — |
| `page` | — |
| `cost.currency` | requisition |
| `cost.amount` | 4000 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/orbital-airburst-strike.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/Orbital_Airburst_Strike
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

