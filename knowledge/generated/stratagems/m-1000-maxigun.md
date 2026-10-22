---
id: "m-1000-maxigun"
name: "M-1000 Maxigun"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: []
wiki_url: "https://helldivers.wiki.gg/wiki/M-1000_Maxigun"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/m-1000-maxigun.json"
---

# M-1000 Maxigun

**分类：** 战略配备 (`stratagems`) · **ID：** `m-1000-maxigun`

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/M-1000_Maxigun

## 简介

The M-1000 Maxigun is a Stratagem that calls down a Support Weapon, consisting of a belt-fed minigun and ammo backpack. It can fire continuously without the need to reload.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | supply |
| `availability` | loadout |
| 类型 (`kind`) | support_weapon |
| 特性 ID (`traitIds`) | support-weapon, medium-armor-penetrating, backpack |
| 输入指令 (`code`) | down, left, right, down, up, up |
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
| `shipModules\[3\].department` | bridge |
| `shipModules\[3\].module` | Morale Augmentation |
| `shipModules\[3\].effect` | Reduces cooldown time for all Stratagems by 5%. |
| `shipModules\[4\].department` | engineering_bay |
| `shipModules\[4\].module` | Streamlined Launch Process |
| `shipModules\[4\].effect` | All Support Weapon stratagems launch immediately once called in, reducing overall deployment time. |


## 攻击模式、伤害与穿甲

### 1. M-1000 P（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 80 |
| `damage.durable` | 18 |
| `damage.type` | Ballistic |
| `penetration.direct` | medium |
| `penetration.slightAngle` | medium |
| `penetration.largeAngle` | medium |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | — |
| `projectile.massG` | 11 |
| `projectile.initialVelocityMps` | 920 |
| `projectile.dragFactorPct` | 30 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 10 |
| `forces.stagger` | 20 |
| `forces.push` | 24 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | warbond |
| `label` | Python Commandos P3 |
| 战争债券 ID (`warbondId`) | python-commandos |
| `page` | 3 |
| `cost.currency` | medals |
| `cost.amount` | 110 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/m-1000-maxigun.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/M-1000_Maxigun
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

