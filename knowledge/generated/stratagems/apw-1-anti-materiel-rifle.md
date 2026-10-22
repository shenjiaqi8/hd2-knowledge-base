---
id: "apw-1-anti-materiel-rifle"
name: "APW-1 Anti-Materiel Rifle"
collection: "stratagems"
aliases: ["AMR"]
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/APW-1_Anti-Materiel_Rifle"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/apw-1-anti-materiel-rifle.json"
---

# APW-1 Anti-Materiel Rifle

**分类：** 战略配备 (`stratagems`) · **ID：** `apw-1-anti-materiel-rifle`

**别名：** AMR

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/APW-1_Anti-Materiel_Rifle

## 简介

The Anti-Materiel Rifle (abbreviated as AMR) is a precision Support Weapon able to penetrate light vehicle armor.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | supply |
| `availability` | loadout |
| 类别 (`category`) | patriotic_administration_center |
| 类型 (`kind`) | support_weapon |
| 特性 ID (`traitIds`) | support-weapon, heavy-armor-penetrating |
| 输入指令 (`code`) | down, left, right, up, down |
| 冷却时间（秒） (`cooldownS`) | 480 |
| `cooldownVariants\[1\].label` | With Morale Augmentation |
| `cooldownVariants\[1\].seconds` | 456 |
| 呼叫时间（秒） (`callInTimeS`) | 7.75 |
| `callInTimeUpgradedS` | 4.75 |
| 使用次数 (`uses`) | unlimited |
| `unlockLevel` | 1 |
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
| `shipModules\[6\].effect` | All Support Weapon stratagems launch immediately once called in, reducing overall deployment time. |


## 攻击模式、伤害与穿甲

### 1. APW-1 P（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 450 |
| `damage.durable` | 225 |
| `damage.type` | Ballistic |
| `penetration.direct` | heavy |
| `penetration.slightAngle` | heavy |
| `penetration.largeAngle` | heavy |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | — |
| `projectile.massG` | 52 |
| `projectile.initialVelocityMps` | 880 |
| `projectile.dragFactorPct` | 30 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 20 |
| `forces.stagger` | 25 |
| `forces.push` | 25 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | requisition |
| `label` | Patriotic Administration Center |
| 战争债券 ID (`warbondId`) | — |
| `page` | — |
| `cost.currency` | requisition |
| `cost.amount` | 5000 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/apw-1-anti-materiel-rifle.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/APW-1_Anti-Materiel_Rifle
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

