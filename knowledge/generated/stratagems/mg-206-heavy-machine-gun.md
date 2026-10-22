---
id: "mg-206-heavy-machine-gun"
name: "MG-206 Heavy Machine Gun"
collection: "stratagems"
aliases: ["HMG"]
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/MG-206_Heavy_Machine_Gun"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/mg-206-heavy-machine-gun.json"
---

# MG-206 Heavy Machine Gun

**分类：** 战略配备 (`stratagems`) · **ID：** `mg-206-heavy-machine-gun`

**别名：** HMG

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/MG-206_Heavy_Machine_Gun

## 简介

The MG-206 Heavy Machine Gun (abbreviated as HMG) is a Stratagem which calls a Support Weapon capable of firing heavy armor-penetrating rounds.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | supply |
| `availability` | loadout |
| 类别 (`category`) | patriotic_administration_center |
| 类型 (`kind`) | support_weapon |
| 特性 ID (`traitIds`) | support-weapon, heavy-armor-penetrating, stationary-reload |
| 输入指令 (`code`) | down, left, up, down, down |
| 冷却时间（秒） (`cooldownS`) | 480 |
| `cooldownVariants\[1\].label` | With Morale Augmentation |
| `cooldownVariants\[1\].seconds` | 456 |
| 呼叫时间（秒） (`callInTimeS`) | 7.75 |
| `callInTimeUpgradedS` | 4.75 |
| 使用次数 (`uses`) | unlimited |
| `unlockLevel` | 12 |
| `shipModules\[1\].department` | patriotic_administration_center |
| `shipModules\[1\].module` | Donation Access License |
| `shipModules\[1\].effect` | Support Weapons deploy with the maximum number of carriable magazines. |
| `shipModules\[2\].department` | patriotic_administration_center |
| `shipModules\[2\].module` | Streamlined Request Process |
| `shipModules\[2\].effect` | Decreases Support Weapon stratagem cooldown by 10%. |
| `shipModules\[3\].department` | patriotic_administration_center |
| `shipModules\[3\].module` | Payroll Management System |
| `shipModules\[3\].effect` | Reduces reload time for all support weapons by 10%. |
| `shipModules\[4\].department` | bridge |
| `shipModules\[4\].module` | Morale Augmentation |
| `shipModules\[4\].effect` | Reduces cooldown time for all Stratagems by 5%. |
| `shipModules\[5\].department` | engineering_bay |
| `shipModules\[5\].module` | Streamlined Launch Process |
| `shipModules\[5\].effect` | All Support Weapons launch immediately once called in, reducing overall deployment time. |


## 攻击模式、伤害与穿甲

### 1. MG-206 P（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 150 |
| `damage.durable` | 35 |
| `damage.type` | Ballistic |
| `penetration.direct` | heavy |
| `penetration.slightAngle` | heavy |
| `penetration.largeAngle` | heavy |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | — |
| `projectile.massG` | 52 |
| `projectile.initialVelocityMps` | 980 |
| `projectile.dragFactorPct` | 30 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 15 |
| `forces.stagger` | 25 |
| `forces.push` | 20 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | requisition |
| `label` | Patriotic Administration Center |
| 战争债券 ID (`warbondId`) | — |
| `page` | — |
| `cost.currency` | requisition |
| `cost.amount` | 6000 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/mg-206-heavy-machine-gun.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/MG-206_Heavy_Machine_Gun
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

