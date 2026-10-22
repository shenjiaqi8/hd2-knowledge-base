---
id: "eagle-cluster-bomb"
name: "Eagle Cluster Bomb"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/Eagle_Cluster_Bomb"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/eagle-cluster-bomb.json"
---

# Eagle Cluster Bomb

**分类：** 战略配备 (`stratagems`) · **ID：** `eagle-cluster-bomb`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/Eagle_Cluster_Bomb

## 简介

The Eagle Cluster Bomb is an offensive stratagem that calls in a carpet bomb on the area.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | offensive |
| `availability` | loadout |
| 类别 (`category`) | hangar |
| 类型 (`kind`) | eagle |
| 特性 ID (`traitIds`) | explosive, eagle, medium-armor-penetrating |
| 输入指令 (`code`) | up, right, down, down, right |
| 冷却时间（秒） (`cooldownS`) | 15 |
| `cooldownVariants\[1\].label` | With Morale Augmentation |
| `cooldownVariants\[1\].seconds` | 14.25 |
| `cooldownVariants\[2\].label` | With Liquid-Ventilated Cockpit |
| `cooldownVariants\[2\].seconds` | 7.5 |
| `cooldownVariants\[3\].label` | With All Upgrades |
| `cooldownVariants\[3\].seconds` | 6.75 |
| 呼叫时间（秒） (`callInTimeS`) | 4.1 |
| 使用次数 (`uses`) | 4 |
| `unlockLevel` | 3 |
| `shipModules\[1\].department` | hangar |
| `shipModules\[1\].module` | Liquid-Ventilated Cockpit |
| `shipModules\[1\].effect` | Eagle stratagem cooldown reduced by 50%. |
| `shipModules\[2\].department` | hangar |
| `shipModules\[2\].module` | Pit Crew Hazard Pay |
| `shipModules\[2\].effect` | Reduces Eagle Rearm time by 20%. |
| `shipModules\[3\].department` | hangar |
| `shipModules\[3\].module` | Expanded Weapons Bay |
| `shipModules\[3\].effect` | Increases the number of Eagle uses per Rearm by 1. |
| `shipModules\[4\].department` | hangar |
| `shipModules\[4\].module` | XXL Weapons Bay |
| `shipModules\[4\].effect` | Eagle Stratagems that drop multiple drop will drop 1 additional bomb(s). |
| `shipModules\[5\].department` | hangar |
| `shipModules\[5\].module` | Advanced Crew Training |
| `shipModules\[5\].effect` | Eagle Rearm cooldown further reduced by 10% if called in while Eagle uses still remain. |
| `shipModules\[6\].department` | bridge |
| `shipModules\[6\].module` | Morale Augmentation |
| `shipModules\[6\].effect` | Reduces cooldown time for all Stratagems by 5%. |


## 攻击模式、伤害与穿甲

### 1. S P4（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 1500 |
| `damage.durable` | 1500 |
| `damage.type` | Ballistic |
| `penetration.direct` | anti_tank_iii |
| `penetration.slightAngle` | anti_tank_iii |
| `penetration.largeAngle` | anti_tank_iii |
| `penetration.extremeAngle` | anti_tank_iii |
| `projectile.pellets` | — |
| `projectile.massG` | 100 |
| `projectile.initialVelocityMps` | 300 |
| `projectile.dragFactorPct` | 50 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 40 |
| `forces.stagger` | 20 |
| `forces.push` | 15 |


### 2. S P4 E（explosion）

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
| `area.innerRadiusM` | 1 |
| `area.outerRadiusM` | 2 |
| `area.shockwaveRadiusM` | 10 |
| `forces.demolition` | 30 |
| `forces.stagger` | 50 |
| `forces.push` | 40 |


### 3. P13（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 20 |
| `damage.durable` | 2 |
| `damage.type` | Ballistic |
| `penetration.direct` | unarmored |
| `penetration.slightAngle` | unarmored |
| `penetration.largeAngle` | unarmored |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | — |
| `projectile.massG` | 50 |
| `projectile.initialVelocityMps` | 30 |
| `projectile.dragFactorPct` | 50 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 10 |
| `forces.stagger` | 30 |
| `forces.push` | 10 |


### 4. P13 IE（explosion）

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
| `label` | Hangar |
| 战争债券 ID (`warbondId`) | — |
| `page` | — |
| `cost.currency` | requisition |
| `cost.amount` | 4000 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/eagle-cluster-bomb.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/Eagle_Cluster_Bomb
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

