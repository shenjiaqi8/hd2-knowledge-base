---
id: "a-ac-8-autocannon-sentry"
name: "A/AC-8 Autocannon Sentry"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/A/AC-8_Autocannon_Sentry"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/a-ac-8-autocannon-sentry.json"
---

# A/AC-8 Autocannon Sentry

**分类：** 战略配备 (`stratagems`) · **ID：** `a-ac-8-autocannon-sentry`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/A/AC-8_Autocannon_Sentry

## 简介

The A/AC-8 Autocannon Sentry is a powerful defensive stratagem firing armor-piercing, high-explosive shells. It fires in 3 round bursts and has the slowest turning speed of all the automatic sentries. Unlike the AC-8 Autocannon support weapon, the rounds that the sentry fires do not bounce, have higher armor penetration, and will always explode on impact.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | defensive |
| `availability` | loadout |
| 类别 (`category`) | robotics_workshop |
| 类型 (`kind`) | sentry |
| 特性 ID (`traitIds`) | hellpod, sentry, anti-tank |
| 输入指令 (`code`) | down, up, right, up, left, up |
| 冷却时间（秒） (`cooldownS`) | 150 |
| `cooldownVariants\[1\].label` | With Morale Augmentation |
| `cooldownVariants\[1\].seconds` | 142.5 |
| `cooldownVariants\[2\].label` | With Synthetic Supplementation |
| `cooldownVariants\[2\].seconds` | 135 |
| `cooldownVariants\[3\].label` | With All Upgrades |
| `cooldownVariants\[3\].seconds` | 128.25 |
| 呼叫时间（秒） (`callInTimeS`) | 7.75 |
| `callInTimeUpgradedS` | 4.75 |
| 使用次数 (`uses`) | unlimited |
| `unlockLevel` | 13 |
| `shipModules\[1\].department` | bridge |
| `shipModules\[1\].module` | Morale Augmentation |
| `shipModules\[1\].effect` | Reduces cooldown time for all Stratagems by 5%. |
| `shipModules\[2\].department` | engineering_bay |
| `shipModules\[2\].module` | Synthetic Supplementation |
| `shipModules\[2\].effect` | Reduces cooldown time for Sentry, Emplacement, and Resupply stratagems by 10%. |
| `shipModules\[3\].department` | engineering_bay |
| `shipModules\[3\].module` | Advanced Construction |
| `shipModules\[3\].effect` | Increases health of Sentry stratagems by 50%. |
| `shipModules\[4\].department` | robotics_workshop |
| `shipModules\[4\].module` | Dynamic Tracking |
| `shipModules\[4\].effect` | Removes deployment time for Sentry stratagems. |
| `shipModules\[5\].department` | robotics_workshop |
| `shipModules\[5\].module` | Shock Absorption Gel |
| `shipModules\[5\].effect` | Increases ammo for Sentry stratagems by 50%. |
| `shipModules\[6\].department` | robotics_workshop |
| `shipModules\[6\].module` | High-Quality Lubricant |
| `shipModules\[6\].effect` | Increases the rotation speed for Sentry stratagems. |
| `shipModules\[7\].department` | robotics_workshop |
| `shipModules\[7\].module` | Blast Absorption |
| `shipModules\[7\].effect` | Sentries take 50% less damage from explosions. |


## 攻击模式、伤害与穿甲

### 1. A/AC-8 P（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 450 |
| `damage.durable` | 450 |
| `damage.type` | Ballistic |
| `penetration.direct` | anti_tank_i |
| `penetration.slightAngle` | anti_tank_i |
| `penetration.largeAngle` | anti_tank_i |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | — |
| `projectile.massG` | 900 |
| `projectile.initialVelocityMps` | 1021 |
| `projectile.dragFactorPct` | 30 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 30 |
| `forces.stagger` | 40 |
| `forces.push` | 10 |


### 2. A/AC-8 P IE（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 150 |
| `damage.durable` | 150 |
| `damage.type` | Explosion |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 2 |
| `area.outerRadiusM` | 6 |
| `area.shockwaveRadiusM` | 8 |
| `forces.demolition` | 30 |
| `forces.stagger` | 30 |
| `forces.push` | 30 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | requisition |
| `label` | Robotics Workshop |
| 战争债券 ID (`warbondId`) | — |
| `page` | — |
| `cost.currency` | requisition |
| `cost.amount` | 6000 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/a-ac-8-autocannon-sentry.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/A/AC-8_Autocannon_Sentry
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

