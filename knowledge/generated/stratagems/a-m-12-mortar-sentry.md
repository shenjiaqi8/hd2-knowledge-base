---
id: "a-m-12-mortar-sentry"
name: "A/M-12 Mortar Sentry"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/A/M-12_Mortar_Sentry"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/a-m-12-mortar-sentry.json"
---

# A/M-12 Mortar Sentry

**分类：** 战略配备 (`stratagems`) · **ID：** `a-m-12-mortar-sentry`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/A/M-12_Mortar_Sentry

## 简介

The A/M-12 Mortar Sentry is a very powerful defensive stratagem able to destroy enemies from range, and behind cover.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | defensive |
| `availability` | loadout |
| 类别 (`category`) | robotics_workshop |
| 类型 (`kind`) | sentry |
| 特性 ID (`traitIds`) | hellpod, explosive, sentry, medium-armor-penetrating |
| 输入指令 (`code`) | down, up, right, right, down |
| 冷却时间（秒） (`cooldownS`) | 180 |
| `cooldownVariants\[1\].label` | With Morale Augmentation |
| `cooldownVariants\[1\].seconds` | 171 |
| `cooldownVariants\[2\].label` | With Synthetic Supplementation |
| `cooldownVariants\[2\].seconds` | 162 |
| `cooldownVariants\[3\].label` | With All Upgrades |
| `cooldownVariants\[3\].seconds` | 153.9 |
| 呼叫时间（秒） (`callInTimeS`) | 7.75 |
| `callInTimeUpgradedS` | 4.75 |
| 使用次数 (`uses`) | unlimited |
| `unlockLevel` | 8 |
| `shipModules\[1\].department` | bridge |
| `shipModules\[1\].module` | Morale Augmentation |
| `shipModules\[1\].effect` | Reduces cooldown time for all Stratagems by 5%. |
| `shipModules\[2\].department` | engineering_bay |
| `shipModules\[2\].module` | Synthetic Supplementation |
| `shipModules\[2\].effect` | Reduces cooldown time for Sentry stratagems by 10%. |
| `shipModules\[3\].department` | engineering_bay |
| `shipModules\[3\].module` | Advanced Construction |
| `shipModules\[3\].effect` | Increases the health of the Sentry stratagems by 50%. |
| `shipModules\[4\].department` | robotics_workshop |
| `shipModules\[4\].module` | Dynamic Tracking |
| `shipModules\[4\].effect` | Removes deployment time for Sentry stratagems. |
| `shipModules\[5\].department` | robotics_workshop |
| `shipModules\[5\].module` | Shock Absorption Gel |
| `shipModules\[5\].effect` | Increases ammo for all Sentry stratagems by 50%. |
| `shipModules\[6\].department` | robotics_workshop |
| `shipModules\[6\].module` | High-Quality Lubricant |
| `shipModules\[6\].effect` | Increases the rotation speed of the Sentry stratagems. |
| `shipModules\[7\].department` | robotics_workshop |
| `shipModules\[7\].module` | Blast Absorption |
| `shipModules\[7\].effect` | Sentries takes 50% less damage from explosions. |
| `shipModules\[8\].department` | robotics_workshop |
| `shipModules\[8\].module` | Cross-Platform Compatibility |
| `shipModules\[8\].effect` | Mortar Sentries prioritize fire at marked targets. |


## 攻击模式、伤害与穿甲

### 1. A/M-12 P（projectile）

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
| `projectile.massG` | 70000 |
| `projectile.initialVelocityMps` | 100 |
| `projectile.dragFactorPct` | 25 |
| `projectile.gravityFactorPct` | 600 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 10 |
| `forces.stagger` | 30 |
| `forces.push` | 10 |


### 2. A/M-12 P IE（explosion）

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
| `area.innerRadiusM` | 3 |
| `area.outerRadiusM` | 9 |
| `area.shockwaveRadiusM` | 13 |
| `forces.demolition` | 30 |
| `forces.stagger` | 35 |
| `forces.push` | 40 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | requisition |
| `label` | Robotics Workshop |
| 战争债券 ID (`warbondId`) | — |
| `page` | — |
| `cost.currency` | requisition |
| `cost.amount` | 7000 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/a-m-12-mortar-sentry.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/A/M-12_Mortar_Sentry
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

