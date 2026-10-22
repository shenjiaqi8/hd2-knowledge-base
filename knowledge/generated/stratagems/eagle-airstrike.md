---
id: "eagle-airstrike"
name: "Eagle Airstrike"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/Eagle_Airstrike"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/eagle-airstrike.json"
---

# Eagle Airstrike

**分类：** 战略配备 (`stratagems`) · **ID：** `eagle-airstrike`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/Eagle_Airstrike

## 简介

The Eagle Airstrike is an offensive stratagem that unleashes a powerful bombardment of six bombs in a straight line.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | offensive |
| `availability` | loadout |
| 类别 (`category`) | hangar |
| 类型 (`kind`) | eagle |
| 特性 ID (`traitIds`) | explosive, eagle, anti-tank |
| 输入指令 (`code`) | up, right, down, right |
| 冷却时间（秒） (`cooldownS`) | 15 |
| `cooldownVariants\[1\].label` | With Morale Augmentation |
| `cooldownVariants\[1\].seconds` | 8 |
| `cooldownVariants\[2\].label` | With Liquid-Ventilated Cockpit |
| `cooldownVariants\[2\].seconds` | 7 |
| `cooldownVariants\[3\].label` | With All Upgrades |
| `cooldownVariants\[3\].seconds` | 7 |
| 呼叫时间（秒） (`callInTimeS`) | 0 |
| 使用次数 (`uses`) | 2 |
| `unlockLevel` | 1 |
| `shipModules\[1\].department` | hangar |
| `shipModules\[1\].module` | Liquid-Ventilated Cockpit |
| `shipModules\[1\].effect` | Eagle stratagem cooldown reduced by 50%. |
| `shipModules\[2\].department` | hangar |
| `shipModules\[2\].module` | Pit Crew Hazard Pay |
| `shipModules\[2\].effect` | Reduces Eagle Rearm time by 20%. |
| `shipModules\[3\].department` | hangar |
| `shipModules\[3\].module` | Expanded Weapons Bay |
| `shipModules\[3\].effect` | Increases the number of Eagle stratagem uses per Rearm by 1. |
| `shipModules\[4\].department` | hangar |
| `shipModules\[4\].module` | XXL Weapons Bay |
| `shipModules\[4\].effect` | Eagle stratagems that drop multiple bombs will drop 1 additional bomb(s). |
| `shipModules\[5\].department` | hangar |
| `shipModules\[5\].module` | Advanced Crew Training |
| `shipModules\[5\].effect` | Eagle Rearm cooldown further reduced by 10% if called in while Eagle uses still remain. |
| `shipModules\[6\].department` | bridge |
| `shipModules\[6\].module` | Morale Augmentation |
| `shipModules\[6\].effect` | Reduces cooldown time for all Stratagems by 5%. |


## 攻击模式、伤害与穿甲

### 1. Bomb 100kg（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 1500 |
| `damage.durable` | 1500 |
| `damage.type` | Damage |
| `penetration.direct` | anti_tank_iii |
| `penetration.slightAngle` | anti_tank_iii |
| `penetration.largeAngle` | anti_tank_iii |
| `penetration.extremeAngle` | anti_tank_iii |
| `projectile.pellets` | — |
| `projectile.massG` | 100 |
| `projectile.initialVelocityMps` | 500 |
| `projectile.dragFactorPct` | 50 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 40 |
| `forces.stagger` | 20 |
| `forces.push` | 15 |


### 2. Eagle Bomb 100kg（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 800 |
| `damage.durable` | 800 |
| `damage.type` | Explosion |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 5 |
| `area.outerRadiusM` | 10 |
| `area.shockwaveRadiusM` | 14 |
| `forces.demolition` | 40 |
| `forces.stagger` | 50 |
| `forces.push` | 40 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | requisition |
| `label` | Hangar |
| 战争债券 ID (`warbondId`) | — |
| `page` | — |
| `cost.currency` | requisition |
| `cost.amount` | 4000 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/eagle-airstrike.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/Eagle_Airstrike
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

