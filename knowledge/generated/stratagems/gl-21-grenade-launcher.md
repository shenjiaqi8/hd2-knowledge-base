---
id: "gl-21-grenade-launcher"
name: "GL-21 Grenade Launcher"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/GL-21_Grenade_Launcher"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/gl-21-grenade-launcher.json"
---

# GL-21 Grenade Launcher

**分类：** 战略配备 (`stratagems`) · **ID：** `gl-21-grenade-launcher`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/GL-21_Grenade_Launcher

## 简介

The Grenade Launcher is a Stratagem that calls down a Support Weapon capable of rapidly firing grenades, inflicting large amounts of splash damage.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | supply |
| `availability` | loadout |
| 类别 (`category`) | engineering_bay |
| 类型 (`kind`) | support_weapon |
| 特性 ID (`traitIds`) | support-weapon, explosive, medium-armor-penetrating |
| 输入指令 (`code`) | down, left, up, left, down |
| 冷却时间（秒） (`cooldownS`) | 480 |
| `cooldownVariants\[1\].label` | With Morale Augmentation |
| `cooldownVariants\[1\].seconds` | 456 |
| 呼叫时间（秒） (`callInTimeS`) | 7.75 |
| `callInTimeUpgradedS` | 4.75 |
| 使用次数 (`uses`) | unlimited |
| `unlockLevel` | 5 |
| `shipModules\[1\].department` | patriotic_administration_center |
| `shipModules\[1\].module` | Donation Access Licence |
| `shipModules\[1\].effect` | Support Weapons deploy with the maximum number of carriable magazines. |
| `shipModules\[2\].department` | patriotic_administration_center |
| `shipModules\[2\].module` | Streamlined Request Process |
| `shipModules\[2\].effect` | Support Weapon stratagem cooldown reduced by 10%. |
| `shipModules\[3\].department` | patriotic_administration_center |
| `shipModules\[3\].module` | Superior Packing Methodology |
| `shipModules\[3\].effect` | Resupply stratagem boxes refill Support Weapons with the maximum number of carriable magazines. |
| `shipModules\[4\].department` | patriotic_administration_center |
| `shipModules\[4\].module` | Payroll Management System |
| `shipModules\[4\].effect` | Reduces reload time for all support weapons by 10%. |
| `shipModules\[5\].department` | bridge |
| `shipModules\[5\].module` | Morale Augmentation |
| `shipModules\[5\].effect` | Reduces cooldown time for all Stratagems by 5%. |
| `shipModules\[6\].department` | engineering_bay |
| `shipModules\[6\].module` | Streamlined Launch Process |
| `shipModules\[6\].effect` | All Support Weapon stratagems launch immediately once when called in, reducing overall deployment time. |


## 攻击模式、伤害与穿甲

### 1. GL-21 P（projectile）

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
| `projectile.initialVelocityMps` | 100 |
| `projectile.dragFactorPct` | 120 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 10 |
| `forces.stagger` | 30 |
| `forces.push` | 10 |


### 2. GL-21 P IE（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 400 |
| `damage.durable` | 400 |
| `damage.type` | Explosion |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 3.5 |
| `area.outerRadiusM` | 7.5 |
| `area.shockwaveRadiusM` | 8 |
| `forces.demolition` | 30 |
| `forces.stagger` | 25 |
| `forces.push` | 30 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | requisition |
| `label` | Engineering Bay |
| 战争债券 ID (`warbondId`) | — |
| `page` | — |
| `cost.currency` | requisition |
| `cost.amount` | 6000 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/gl-21-grenade-launcher.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/GL-21_Grenade_Launcher
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

