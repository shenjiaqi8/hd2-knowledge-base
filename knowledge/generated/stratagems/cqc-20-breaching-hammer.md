---
id: "cqc-20-breaching-hammer"
name: "CQC-20 Breaching Hammer"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: []
wiki_url: "https://helldivers.wiki.gg/wiki/CQC-20_Breaching_Hammer"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/cqc-20-breaching-hammer.json"
---

# CQC-20 Breaching Hammer

**分类：** 战略配备 (`stratagems`) · **ID：** `cqc-20-breaching-hammer`

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/CQC-20_Breaching_Hammer

## 简介

The CQC-20 Breaching Hammer is a Melee Support Weapon, which is capable of dealing explosive damage by striking enemies.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | supply |
| `availability` | loadout |
| 类型 (`kind`) | support_weapon |
| 特性 ID (`traitIds`) | support-weapon, explosive, anti-tank, melee |
| 输入指令 (`code`) | down, left, right, left, up |
| 冷却时间（秒） (`cooldownS`) | 480 |
| `cooldownVariants\[1\].label` | With Morale Augmentation |
| `cooldownVariants\[1\].seconds` | 456 |
| 呼叫时间（秒） (`callInTimeS`) | 7.75 |
| `callInTimeUpgradedS` | 4.75 |
| 使用次数 (`uses`) | unlimited |
| `shipModules\[1\].department` | patriotic_administration_center |
| `shipModules\[1\].module` | Streamlined Request Process |
| `shipModules\[1\].effect` | Decreases Support Weapon stratagem cooldown by 10%. |
| `shipModules\[2\].department` | patriotic_administration_center |
| `shipModules\[2\].module` | Superior Packing Methodology |
| `shipModules\[2\].effect` | Resupply stratagem boxes refill Support Weapons with the maximum number of carriable magazines. |
| `shipModules\[3\].department` | patriotic_administration_center |
| `shipModules\[3\].module` | Payroll Management System |
| `shipModules\[3\].effect` | Reduces reload time for all support weapons by 10%. |
| `shipModules\[4\].department` | bridge |
| `shipModules\[4\].module` | Morale Augmentation |
| `shipModules\[4\].effect` | Reduces cooldown time for all stratagems by 5%. |
| `shipModules\[5\].department` | engineering_bay |
| `shipModules\[5\].module` | Streamlined Launch Process |
| `shipModules\[5\].effect` | All Support Weapon stratagems launch immediately once called in, reducing overall deployment time. |


## 攻击模式、伤害与穿甲

### 1. CQC-20 BREACHING HAMMER_dm（other）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 300 |
| `damage.durable` | 150 |
| `damage.type` | Melee |
| `penetration.direct` | medium |
| `penetration.slightAngle` | unarmored |
| `penetration.largeAngle` | unarmored |
| `penetration.extremeAngle` | unarmored |
| `projectile` | — |
| `area` | — |
| `forces.demolition` | 30 |
| `forces.stagger` | 40 |
| `forces.push` | 10 |


### 2. CQC-20 BREACHING HAMMER IE（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 2200 |
| `damage.durable` | 2200 |
| `damage.type` | Explosion |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 0.5 |
| `area.outerRadiusM` | 3 |
| `area.shockwaveRadiusM` | 12 |
| `forces.demolition` | 30 |
| `forces.stagger` | 50 |
| `forces.push` | 40 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | warbond |
| `label` | Siege Breakers P1 |
| 战争债券 ID (`warbondId`) | siege-breakers |
| `page` | 1 |
| `cost.currency` | medals |
| `cost.amount` | 75 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/cqc-20-breaching-hammer.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/CQC-20_Breaching_Hammer
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

