---
id: "eagle-110mm-rocket-pods"
name: "Eagle 110mm Rocket Pods"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/Eagle_110mm_Rocket_Pods"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/eagle-110mm-rocket-pods.json"
---

# Eagle 110mm Rocket Pods

**分类：** 战略配备 (`stratagems`) · **ID：** `eagle-110mm-rocket-pods`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/Eagle_110mm_Rocket_Pods

## 简介

The Eagle 110mm Rocket Pods is an offensive stratagem that sends out 3 volleys of 2 rockets into the largest target near the beacon.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | offensive |
| `availability` | loadout |
| 类别 (`category`) | hangar |
| 类型 (`kind`) | eagle |
| 特性 ID (`traitIds`) | explosive, eagle, anti-tank |
| 输入指令 (`code`) | up, right, up, left |
| 冷却时间（秒） (`cooldownS`) | 15 |
| `cooldownVariants\[1\].label` | With Morale Augmentation |
| `cooldownVariants\[1\].seconds` | 14.25 |
| `cooldownVariants\[2\].label` | With Liquid-Ventilated Cockpit |
| `cooldownVariants\[2\].seconds` | 7.5 |
| `cooldownVariants\[3\].label` | With All Upgrades |
| `cooldownVariants\[3\].seconds` | 6.75 |
| 呼叫时间（秒） (`callInTimeS`) | 3.4 |
| 使用次数 (`uses`) | 3 |
| `unlockLevel` | 10 |
| `shipModules\[1\].department` | hangar |
| `shipModules\[1\].module` | Liquid-Ventilated Cockpit |
| `shipModules\[1\].effect` | Eagle stratagem cooldown reduced by 50%. |
| `shipModules\[2\].department` | hangar |
| `shipModules\[2\].module` | Pit Crew Hazard Pay |
| `shipModules\[2\].effect` | Reduces Eagle rearm time by 20%. |
| `shipModules\[3\].department` | hangar |
| `shipModules\[3\].module` | Expanded Weapons Bay |
| `shipModules\[3\].effect` | Increases the number of Eagle stratagem uses per Rearm by 1. |
| `shipModules\[4\].department` | bridge |
| `shipModules\[4\].module` | Morale Augmentation |
| `shipModules\[4\].effect` | Reduces cooldown time for all Stratagems by 5%. |


## 攻击模式、伤害与穿甲

### 1. S P1（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 600 |
| `damage.durable` | 600 |
| `damage.type` | Ballistic |
| `penetration.direct` | anti_tank_iii |
| `penetration.slightAngle` | anti_tank_iii |
| `penetration.largeAngle` | anti_tank_iii |
| `penetration.extremeAngle` | anti_tank_iii |
| `projectile.pellets` | — |
| `projectile.massG` | 3300 |
| `projectile.initialVelocityMps` | 700 |
| `projectile.dragFactorPct` | 0 |
| `projectile.gravityFactorPct` | 210 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 40 |
| `forces.stagger` | 40 |
| `forces.push` | 15 |


### 2. S P1 IE（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 300 |
| `damage.durable` | 300 |
| `damage.type` | Explosion |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 1.60000002 |
| `area.outerRadiusM` | 5 |
| `area.shockwaveRadiusM` | 8 |
| `forces.demolition` | 30 |
| `forces.stagger` | 30 |
| `forces.push` | 10 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | requisition |
| `label` | Hangar |
| 战争债券 ID (`warbondId`) | — |
| `page` | — |
| `cost.currency` | requisition |
| `cost.amount` | 7500 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/eagle-110mm-rocket-pods.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/Eagle_110mm_Rocket_Pods
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

