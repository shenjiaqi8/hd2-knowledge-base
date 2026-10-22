---
id: "orbital-laser"
name: "Orbital Laser"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/Orbital_Laser"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/orbital-laser.json"
---

# Orbital Laser

**分类：** 战略配备 (`stratagems`) · **ID：** `orbital-laser`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/Orbital_Laser

## 简介

The Orbital Laser also known as Laser is an offensive stratagem that fires a single, continuous laser beam attack that lasts for 25 seconds.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | offensive |
| `availability` | loadout |
| 类别 (`category`) | orbital_cannons |
| 类型 (`kind`) | orbital |
| 特性 ID (`traitIds`) | orbital, anti-tank, beam |
| 输入指令 (`code`) | right, down, up, right, down |
| 冷却时间（秒） (`cooldownS`) | 300 |
| `cooldownVariants\[1\].label` | With Morale Augmentation |
| `cooldownVariants\[1\].seconds` | 285 |
| `cooldownVariants\[2\].label` | With Zero-G Breech Loading |
| `cooldownVariants\[2\].seconds` | 270 |
| `cooldownVariants\[3\].label` | With All Upgrades |
| `cooldownVariants\[3\].seconds` | 256.5 |
| 呼叫时间（秒） (`callInTimeS`) | 2 |
| `callInTimeUpgradedS` | 1 |
| 使用次数 (`uses`) | 3 |
| `unlockLevel` | 15 |
| `shipModules\[1\].department` | orbital_cannons |
| `shipModules\[1\].module` | Zero-G Breech Loading |
| `shipModules\[1\].effect` | Orbital stratagem cooldown time reduced by 10%. |
| `shipModules\[2\].department` | bridge |
| `shipModules\[2\].module` | Targeting Software Upgrade |
| `shipModules\[2\].effect` | 1-second reduction in call-in time for all Orbital Stratagems. |
| `shipModules\[3\].department` | bridge |
| `shipModules\[3\].module` | Morale Augmentation |
| `shipModules\[3\].effect` | Reduces cooldown time for all Stratagems by 5%. |


## 攻击模式、伤害与穿甲

### 1. ORBITAL LASER_DPS（spray）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 599.999994 |
| `damage.durable` | 599.999994 |
| `damage.type` | Damage |
| `penetration.direct` | anti_tank_ii |
| `penetration.slightAngle` | anti_tank_ii |
| `penetration.largeAngle` | anti_tank_ii |
| `penetration.extremeAngle` | unarmored |
| `projectile` | — |
| `area` | — |
| `forces.demolition` | 50 |
| `forces.stagger` | 30 |
| `forces.push` | 30 |


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
| `type` | requisition |
| `label` | Orbital Cannons |
| 战争债券 ID (`warbondId`) | — |
| `page` | — |
| `cost.currency` | requisition |
| `cost.amount` | 10000 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/orbital-laser.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/Orbital_Laser
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

