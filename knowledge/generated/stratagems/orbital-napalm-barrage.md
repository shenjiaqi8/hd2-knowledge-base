---
id: "orbital-napalm-barrage"
name: "Orbital Napalm Barrage"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/Orbital_Napalm_Barrage"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/orbital-napalm-barrage.json"
---

# Orbital Napalm Barrage

**分类：** 战略配备 (`stratagems`) · **ID：** `orbital-napalm-barrage`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/Orbital_Napalm_Barrage

## 简介

The Orbital Napalm Barrage, also known as the ONB, is an offensive orbital Stratagem that launches 5 salvos of 5 120mm shells that explode into pools of fire on impact.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | offensive |
| `availability` | loadout |
| 类别 (`category`) | orbital_cannons |
| 类型 (`kind`) | orbital |
| 特性 ID (`traitIds`) | explosive, orbital, incendiary |
| 输入指令 (`code`) | right, right, down, left, right, up |
| 冷却时间（秒） (`cooldownS`) | 240 |
| `cooldownVariants\[1\].label` | With Morale Augmentation |
| `cooldownVariants\[1\].seconds` | 228 |
| `cooldownVariants\[2\].label` | With Zero-G Breech Loading |
| `cooldownVariants\[2\].seconds` | 216 |
| `cooldownVariants\[3\].label` | With All Upgrades |
| `cooldownVariants\[3\].seconds` | 205.2 |
| 呼叫时间（秒） (`callInTimeS`) | 7.45 |
| `callInTimeUpgradedS` | 6.45 |
| 使用次数 (`uses`) | unlimited |
| `unlockLevel` | 18 |
| `shipModules\[1\].department` | orbital_cannons |
| `shipModules\[1\].module` | Exploding Shrapnel |
| `shipModules\[1\].effect` | Reduces damage falloff from center of explosions caused by orbital Stratagems. |
| `shipModules\[2\].department` | orbital_cannons |
| `shipModules\[2\].module` | More Guns |
| `shipModules\[2\].effect` | Barrage orbitals fire 1 additional salvo(s) per barrage. |
| `shipModules\[3\].department` | orbital_cannons |
| `shipModules\[3\].module` | Zero-G Breech Loading |
| `shipModules\[3\].effect` | Orbital stratagem cooldown time reduced by 10%. |
| `shipModules\[4\].department` | orbital_cannons |
| `shipModules\[4\].module` | High-Density Explosives |
| `shipModules\[4\].effect` | Increases the damage radius on explosions caused by orbital Stratagems by 10%. |
| `shipModules\[5\].department` | bridge |
| `shipModules\[5\].module` | Targeting Software Upgrade |
| `shipModules\[5\].effect` | 1-second reduction in call-in time for all Orbital Stratagems. |
| `shipModules\[6\].department` | bridge |
| `shipModules\[6\].module` | Enhanced Combustion |
| `shipModules\[6\].effect` | Fire damage from Stratagems increased by 25%. |
| `shipModules\[7\].department` | bridge |
| `shipModules\[7\].module` | Morale Augmentation |
| `shipModules\[7\].effect` | Reduces cooldown time for all Stratagems by 5%. |


## 攻击模式、伤害与穿甲

### 1. S P20（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 500 |
| `damage.durable` | 500 |
| `damage.type` | Ballistic |
| `penetration.direct` | anti_tank_i |
| `penetration.slightAngle` | anti_tank_i |
| `penetration.largeAngle` | anti_tank_i |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | — |
| `projectile.massG` | 5000 |
| `projectile.initialVelocityMps` | 400 |
| `projectile.dragFactorPct` | 0 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 30 |
| `forces.stagger` | 20 |
| `forces.push` | 15 |


### 2. S P20 IE（explosion）

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
| `area.innerRadiusM` | 3.29999995 |
| `area.outerRadiusM` | 10 |
| `area.shockwaveRadiusM` | 11 |
| `forces.demolition` | 30 |
| `forces.stagger` | 50 |
| `forces.push` | 40 |


### 3. BurningHeavy（status）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 200 |
| `damage.durable` | 200 |
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


### 4. Fire（status）

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
| `type` | requisition |
| `label` | Orbital Cannons |
| 战争债券 ID (`warbondId`) | — |
| `page` | — |
| `cost.currency` | requisition |
| `cost.amount` | 10000 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/orbital-napalm-barrage.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/Orbital_Napalm_Barrage
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

