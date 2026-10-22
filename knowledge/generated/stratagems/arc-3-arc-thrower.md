---
id: "arc-3-arc-thrower"
name: "ARC-3 Arc Thrower"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/ARC-3_Arc_Thrower"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/arc-3-arc-thrower.json"
---

# ARC-3 Arc Thrower

**分类：** 战略配备 (`stratagems`) · **ID：** `arc-3-arc-thrower`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/ARC-3_Arc_Thrower

## 简介

The Arc Thrower is a support weapon that projects an arc of lightning that can chain between multiple targets.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | supply |
| `availability` | loadout |
| 类别 (`category`) | engineering_bay |
| 类型 (`kind`) | support_weapon |
| 特性 ID (`traitIds`) | support-weapon, anti-tank, chargeup, arc |
| 输入指令 (`code`) | down, right, down, up, left, left |
| 冷却时间（秒） (`cooldownS`) | 480 |
| `cooldownVariants\[1\].label` | With Morale Augmentation |
| `cooldownVariants\[1\].seconds` | 456 |
| 呼叫时间（秒） (`callInTimeS`) | 7.75 |
| `callInTimeUpgradedS` | 4.75 |
| 使用次数 (`uses`) | unlimited |
| `unlockLevel` | 15 |
| `shipModules\[1\].department` | patriotic_administration_center |
| `shipModules\[1\].module` | Streamlined Request Process |
| `shipModules\[1\].effect` | Decreases Support Weapon stratagem cooldown by 10%. |
| `shipModules\[2\].department` | bridge |
| `shipModules\[2\].module` | Morale Augmentation |
| `shipModules\[2\].effect` | Reduces cooldown time for all Stratagems by 5%. |
| `shipModules\[3\].department` | engineering_bay |
| `shipModules\[3\].module` | Circuit Expansion |
| `shipModules\[3\].effect` | Lightning arcs, fired from weapons and turrets, jump to two additional enemies. |
| `shipModules\[4\].department` | engineering_bay |
| `shipModules\[4\].module` | Streamlined Launch Process |
| `shipModules\[4\].effect` | All Support Weapons launch immediately once called in, reducing overall deployment time. |


## 攻击模式、伤害与穿甲

### 1. ARC-3 ARC THROWER A（arc）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 250 |
| `damage.durable` | 100 |
| `damage.type` | Arc |
| `penetration.direct` | anti_tank_iii |
| `penetration.slightAngle` | anti_tank_iii |
| `penetration.largeAngle` | anti_tank_iii |
| `penetration.extremeAngle` | unarmored |
| `projectile` | — |
| `area` | — |
| `forces.demolition` | 20 |
| `forces.stagger` | 35 |
| `forces.push` | 10 |


### 2. Stun Small（status）

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
| `type` | requisition |
| `label` | Engineering Bay |
| 战争债券 ID (`warbondId`) | — |
| `page` | — |
| `cost.currency` | requisition |
| `cost.amount` | 7000 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/arc-3-arc-thrower.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/ARC-3_Arc_Thrower
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

