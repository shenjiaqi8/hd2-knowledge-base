---
id: "tx-41-sterilizer"
name: "TX-41 Sterilizer"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated", "broken_file_links"]
wiki_url: "https://helldivers.wiki.gg/wiki/TX-41_Sterilizer"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/tx-41-sterilizer.json"
---

# TX-41 Sterilizer

**分类：** 战略配备 (`stratagems`) · **ID：** `tx-41-sterilizer`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/TX-41_Sterilizer

## 简介

The Sterilizer is a Support Weapon Stratagem that sprays a caustic gas which slows and blinds enemies.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | supply |
| `availability` | loadout |
| 类型 (`kind`) | support_weapon |
| 特性 ID (`traitIds`) | support-weapon, caustic |
| 输入指令 (`code`) | down, left, up, down, left |
| 冷却时间（秒） (`cooldownS`) | 480 |
| `cooldownVariants\[1\].label` | With Morale Augmentation |
| `cooldownVariants\[1\].seconds` | 456 |
| 呼叫时间（秒） (`callInTimeS`) | 7.75 |
| `callInTimeUpgradedS` | 4.75 |
| 使用次数 (`uses`) | unlimited |
| `shipModules\[1\].department` | patriotic_administration_center |
| `shipModules\[1\].module` | Donation Access Licence |
| `shipModules\[1\].effect` | Support Weapons deploy with the maximum number of carriable magazines. |
| `shipModules\[2\].department` | patriotic_administration_center |
| `shipModules\[2\].module` | Streamlined Request Process |
| `shipModules\[2\].effect` | Decreases Support Weapon stratagem cooldown by 10%. |
| `shipModules\[3\].department` | patriotic_administration_center |
| `shipModules\[3\].module` | Superior Packing Methodology |
| `shipModules\[3\].effect` | Resupply stratagem boxes refill Support Weapons with the maximum number of carriable magazines. |
| `shipModules\[4\].department` | patriotic_administration_center |
| `shipModules\[4\].module` | Payroll Management System |
| `shipModules\[4\].effect` | Reduces reload time for all support weapons by 10%. |
| `shipModules\[5\].department` | bridge |
| `shipModules\[5\].module` | Morale Augmentation |
| `shipModules\[5\].effect` | Reduces cooldown time for all stratagems by 5%. |
| `shipModules\[6\].department` | engineering_bay |
| `shipModules\[6\].module` | Streamlined Launch Process |
| `shipModules\[6\].effect` | All Support Weapons launch immediately once called in, reducing overall deployment time. |


## 攻击模式、伤害与穿甲

### 1. TX-41 STERILIZER S（spray）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 1 |
| `damage.durable` | 1 |
| `damage.type` | Gas |
| `penetration.direct` | anti_tank_i |
| `penetration.slightAngle` | anti_tank_i |
| `penetration.largeAngle` | anti_tank_i |
| `penetration.extremeAngle` | unarmored |
| `projectile` | — |
| `area` | — |
| `forces.demolition` | 5 |
| `forces.stagger` | 10 |
| `forces.push` | 5 |


### 2. Gas Confusion Var2（status）

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


### 3. Gas Var2（status）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 25 |
| `damage.durable` | 25 |
| `damage.type` | Gas |
| `penetration.direct` | anti_tank_ii |
| `penetration.slightAngle` | anti_tank_ii |
| `penetration.largeAngle` | anti_tank_ii |
| `penetration.extremeAngle` | unarmored |
| `projectile` | — |
| `area` | — |
| `forces.demolition` | 0 |
| `forces.stagger` | 0 |
| `forces.push` | 0 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | warbond |
| `label` | Chemical Agents P2 |
| 战争债券 ID (`warbondId`) | chemical-agents |
| `page` | 2 |
| `cost.currency` | medals |
| `cost.amount` | 85 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/tx-41-sterilizer.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/TX-41_Sterilizer
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

