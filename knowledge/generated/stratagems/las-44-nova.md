---
id: "las-44-nova"
name: "LAS-44 Nova"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["broken_file_links"]
wiki_url: "https://helldivers.wiki.gg/wiki/LAS-44_Nova"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/las-44-nova.json"
---

# LAS-44 Nova

**分类：** 战略配备 (`stratagems`) · **ID：** `las-44-nova`

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/LAS-44_Nova

## 简介

The LAS-44 Nova is a Support Weapon that deploys a high-powered, energy-based sniper rifle. It does not require ammunition, but must cool down between shots.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | supply |
| `availability` | loadout |
| 类型 (`kind`) | support_weapon |
| 特性 ID (`traitIds`) | support-weapon, heavy-armor-penetrating, heat |
| 输入指令 (`code`) | down, left, right, down, down |
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
| `shipModules\[2\].effect` | Resupply Stratagem boxes refill Support Weapons with the maximum number of carriable magazines. |
| `shipModules\[3\].department` | patriotic_administration_center |
| `shipModules\[3\].module` | Payroll Management System |
| `shipModules\[3\].effect` | Reduces reload time for all support weapons by 10%. |
| `shipModules\[4\].department` | bridge |
| `shipModules\[4\].module` | Morale Augmentation |
| `shipModules\[4\].effect` | Reduces cooldown time for all Stratagems by 5%. |
| `shipModules\[5\].department` | engineering_bay |
| `shipModules\[5\].module` | Streamlined Launch Process |
| `shipModules\[5\].effect` | All Support Weapon stratagems launch immediately once called in, reducing overall deployment time. |


## 攻击模式、伤害与穿甲

### 1. LAS-44 P（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 880 |
| `damage.durable` | 880 |
| `damage.type` | Ballistic |
| `penetration.direct` | anti_tank_i |
| `penetration.slightAngle` | anti_tank_i |
| `penetration.largeAngle` | anti_tank_i |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | — |
| `projectile.massG` | 8 |
| `projectile.initialVelocityMps` | 1500 |
| `projectile.dragFactorPct` | 0 |
| `projectile.gravityFactorPct` | 0 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 17 |
| `forces.stagger` | 20 |
| `forces.push` | 20 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | warbond |
| `label` | Scope of Authority P3 |
| 战争债券 ID (`warbondId`) | scope-of-authority |
| `page` | 3 |
| `cost.currency` | medals |
| `cost.amount` | 110 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/las-44-nova.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/LAS-44_Nova
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

