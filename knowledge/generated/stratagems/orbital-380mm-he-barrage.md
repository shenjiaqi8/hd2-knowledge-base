---
id: "orbital-380mm-he-barrage"
name: "Orbital 380mm HE Barrage"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/Orbital_380mm_HE_Barrage"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/orbital-380mm-he-barrage.json"
---

# Orbital 380mm HE Barrage

**分类：** 战略配备 (`stratagems`) · **ID：** `orbital-380mm-he-barrage`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/Orbital_380mm_HE_Barrage

## 简介

The Orbital 380mm HE Barrage is an offensive stratagem firing 5-6 salvos of 3 shells. The rate of shells being shot is once per a second, and each salvo has a 2.5-seconds pause in between.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | offensive |
| `availability` | loadout |
| 类别 (`category`) | orbital_cannons |
| 类型 (`kind`) | orbital |
| 特性 ID (`traitIds`) | explosive, orbital, anti-tank |
| 输入指令 (`code`) | right, down, up, up, left, down, down |
| 冷却时间（秒） (`cooldownS`) | 240 |
| `cooldownVariants\[1\].label` | With Morale Augmentation |
| `cooldownVariants\[1\].seconds` | 228 |
| `cooldownVariants\[2\].label` | With Zero-G Breech Loading |
| `cooldownVariants\[2\].seconds` | 216 |
| `cooldownVariants\[3\].label` | With All Upgrades |
| `cooldownVariants\[3\].seconds` | 205.2 |
| 呼叫时间（秒） (`callInTimeS`) | 8.45 |
| `callInTimeUpgradedS` | 7.45 |
| 使用次数 (`uses`) | unlimited |
| `unlockLevel` | 8 |
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
| `shipModules\[4\].module` | Atmospheric Monitoring |
| `shipModules\[4\].effect` | Orbital HE barrage spread reduced by 15%. |
| `shipModules\[5\].department` | orbital_cannons |
| `shipModules\[5\].module` | High-Density Explosives |
| `shipModules\[5\].effect` | Increases the damage radius on explosions caused by orbital Stratagems by 10%. |
| `shipModules\[6\].department` | bridge |
| `shipModules\[6\].module` | Targeting Software Upgrade |
| `shipModules\[6\].effect` | 1-second reduction in call-in time for all Orbital Stratagems. |
| `shipModules\[7\].department` | bridge |
| `shipModules\[7\].module` | Morale Augmentation |
| `shipModules\[7\].effect` | Reduces cooldown time for all Stratagems by 5%. |


## 攻击模式、伤害与穿甲

### 1. S P22（projectile）

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


### 2. S P22 IE（explosion）

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
| `label` | Orbital Cannons |
| 战争债券 ID (`warbondId`) | — |
| `page` | — |
| `cost.currency` | requisition |
| `cost.amount` | 7500 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/orbital-380mm-he-barrage.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/Orbital_380mm_HE_Barrage
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

