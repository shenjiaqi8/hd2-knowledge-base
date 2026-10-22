---
id: "eagle-strafing-run"
name: "Eagle Strafing Run"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/Eagle_Strafing_Run"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/eagle-strafing-run.json"
---

# Eagle Strafing Run

**分类：** 战略配备 (`stratagems`) · **ID：** `eagle-strafing-run`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/Eagle_Strafing_Run

## 简介

The Eagle Strafing Run is an offensive stratagem that calls the Eagle in to fire a barrage of anti-tank, high-explosive shells, parallel to the player.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | offensive |
| `availability` | loadout |
| 类别 (`category`) | hangar |
| 类型 (`kind`) | eagle |
| 特性 ID (`traitIds`) | eagle, anti-tank |
| 输入指令 (`code`) | up, right, right |
| 冷却时间（秒） (`cooldownS`) | 15 |
| `cooldownVariants\[1\].label` | With Morale Augmentation |
| `cooldownVariants\[1\].seconds` | 14.25 |
| `cooldownVariants\[2\].label` | With Liquid-Ventilated Cockpit |
| `cooldownVariants\[2\].seconds` | 7.5 |
| `cooldownVariants\[3\].label` | With All Upgrades |
| `cooldownVariants\[3\].seconds` | 6.75 |
| 呼叫时间（秒） (`callInTimeS`) | 2.4 |
| 使用次数 (`uses`) | 4 |
| `unlockLevel` | 1 |
| `shipModules\[1\].department` | hangar |
| `shipModules\[1\].module` | Liquid-Ventilated Cockpit |
| `shipModules\[1\].effect` | Reduces Eagle stratagem cooldown time by 50%. |
| `shipModules\[2\].department` | hangar |
| `shipModules\[2\].module` | Pit Crew Hazard Pay |
| `shipModules\[2\].effect` | Reduces Eagle Rearm time by 20%. |
| `shipModules\[3\].department` | hangar |
| `shipModules\[3\].module` | Expanded Weapons Bay |
| `shipModules\[3\].effect` | Increases the number of Eagle stratagem uses per Rearm by 1. |
| `shipModules\[4\].department` | hangar |
| `shipModules\[4\].module` | Advanced Crew Training |
| `shipModules\[4\].effect` | Eagle Rearm further reduced by 10% if called in while Eagle uses still remain. |
| `shipModules\[5\].department` | bridge |
| `shipModules\[5\].module` | Morale Augmentation |
| `shipModules\[5\].effect` | Reduces cooldown time for all Stratagems by 5%. |


## 攻击模式、伤害与穿甲

### 1. P5（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 350 |
| `damage.durable` | 200 |
| `damage.type` | Ballistic |
| `penetration.direct` | anti_tank_i |
| `penetration.slightAngle` | anti_tank_i |
| `penetration.largeAngle` | heavy |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | — |
| `projectile.massG` | 400 |
| `projectile.initialVelocityMps` | 1050 |
| `projectile.dragFactorPct` | 30 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 30 |
| `forces.stagger` | 35 |
| `forces.push` | 3 |


### 2. P5 IE（explosion）

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
| `area.innerRadiusM` | 2.5 |
| `area.outerRadiusM` | 5 |
| `area.shockwaveRadiusM` | 6.5 |
| `forces.demolition` | 30 |
| `forces.stagger` | 35 |
| `forces.push` | 5 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | requisition |
| `label` | Hangar |
| 战争债券 ID (`warbondId`) | — |
| `page` | — |
| `cost.currency` | requisition |
| `cost.amount` | 1500 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/eagle-strafing-run.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/Eagle_Strafing_Run
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

