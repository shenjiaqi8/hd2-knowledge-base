---
id: "a-flam-40-flame-sentry"
name: "A/FLAM-40 Flame Sentry"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: []
wiki_url: "https://helldivers.wiki.gg/wiki/A/FLAM-40_Flame_Sentry"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/a-flam-40-flame-sentry.json"
---

# A/FLAM-40 Flame Sentry

**分类：** 战略配备 (`stratagems`) · **ID：** `a-flam-40-flame-sentry`

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/A/FLAM-40_Flame_Sentry

## 简介

The Flame Sentry is a close-range incendiary sentry stratagem.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | defensive |
| `availability` | loadout |
| 类型 (`kind`) | sentry |
| 特性 ID (`traitIds`) | hellpod, incendiary, sentry |
| 输入指令 (`code`) | down, up, right, down, up, up |
| 冷却时间（秒） (`cooldownS`) | 100 |
| `cooldownVariants\[1\].label` | With Morale Augmentation |
| `cooldownVariants\[1\].seconds` | 95 |
| `cooldownVariants\[2\].label` | With Synthetic Supplementation |
| `cooldownVariants\[2\].seconds` | 90 |
| `cooldownVariants\[3\].label` | With All Upgrades |
| `cooldownVariants\[3\].seconds` | 85.5 |
| 呼叫时间（秒） (`callInTimeS`) | 7.75 |
| `callInTimeUpgradedS` | 4.75 |
| 使用次数 (`uses`) | unlimited |
| `shipModules\[1\].department` | bridge |
| `shipModules\[1\].module` | Morale Augmentation |
| `shipModules\[1\].effect` | Reduces cooldown time for all Stratagems by 5%. |
| `shipModules\[2\].department` | bridge |
| `shipModules\[2\].module` | Enhanced Combustion |
| `shipModules\[2\].effect` | Fire damage from Stratagems increased by 25%. |
| `shipModules\[3\].department` | engineering_bay |
| `shipModules\[3\].module` | Synthetic Supplementation |
| `shipModules\[3\].effect` | Reduces cooldown time for Sentry stratagems by 10%. |
| `shipModules\[4\].department` | engineering_bay |
| `shipModules\[4\].module` | Advanced Construction |
| `shipModules\[4\].effect` | Increases the health of the Sentry stratagems by 50%. |
| `shipModules\[5\].department` | robotics_workshop |
| `shipModules\[5\].module` | Dynamic Tracking |
| `shipModules\[5\].effect` | Removes deployment time for Sentry stratagems. |
| `shipModules\[6\].department` | robotics_workshop |
| `shipModules\[6\].module` | Shock Absorption Gel |
| `shipModules\[6\].effect` | Increases ammo for all Sentry stratagems by 50%. |
| `shipModules\[7\].department` | robotics_workshop |
| `shipModules\[7\].module` | High-Quality Lubricant |
| `shipModules\[7\].effect` | Increases the rotation speed of the Sentry stratagems. |
| `shipModules\[8\].department` | robotics_workshop |
| `shipModules\[8\].module` | Blast Absorption |
| `shipModules\[8\].effect` | Sentries takes 50% less damage from explosions. |


## 攻击模式、伤害与穿甲

### 1. FLAME SENTRY S（spray）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 8 |
| `damage.durable` | 8 |
| `damage.type` | Fire |
| `penetration.direct` | heavy |
| `penetration.slightAngle` | heavy |
| `penetration.largeAngle` | heavy |
| `penetration.extremeAngle` | heavy |
| `projectile` | — |
| `area` | — |
| `forces.demolition` | 10 |
| `forces.stagger` | 5 |
| `forces.push` | 5 |


### 2. Fire（status）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 100 |
| `damage.durable` | 100 |
| `damage.type` | Fire |
| `penetration.direct` | heavy |
| `penetration.slightAngle` | heavy |
| `penetration.largeAngle` | heavy |
| `penetration.extremeAngle` | unarmored |
| `projectile` | — |
| `area` | — |
| `forces.demolition` | 0 |
| `forces.stagger` | 0 |
| `forces.push` | 0 |


### 3. Fire Panic（status）

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


### 4. FlamerSlowed（status）

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


### 5. Flame Sentry Death Explosion（other）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 400 |
| `damage.durable` | 400 |
| `damage.type` | Fire |
| `penetration.direct` | medium |
| `penetration.slightAngle` | unarmored |
| `penetration.largeAngle` | unarmored |
| `penetration.extremeAngle` | unarmored |
| `projectile` | — |
| `area` | — |
| `forces.demolition` | 30 |
| `forces.stagger` | 20 |
| `forces.push` | 40 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | warbond |
| `label` | Urban Legends P2 |
| 战争债券 ID (`warbondId`) | urban-legends |
| `page` | 2 |
| `cost.currency` | medals |
| `cost.amount` | 85 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/a-flam-40-flame-sentry.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/A/FLAM-40_Flame_Sentry
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

