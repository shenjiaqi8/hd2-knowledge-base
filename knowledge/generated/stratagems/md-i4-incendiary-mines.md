---
id: "md-i4-incendiary-mines"
name: "MD-I4 Incendiary Mines"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/MD-I4_Incendiary_Mines"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/md-i4-incendiary-mines.json"
---

# MD-I4 Incendiary Mines

**分类：** 战略配备 (`stratagems`) · **ID：** `md-i4-incendiary-mines`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/MD-I4_Incendiary_Mines

## 简介

The MD-I4 Incendiary Mines are a defensive stratagem that blankets a roughly 25-30 meter diameter area around itself with incendiary mines.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | defensive |
| `availability` | loadout |
| 类别 (`category`) | engineering_bay |
| 类型 (`kind`) | emplacement |
| 特性 ID (`traitIds`) | hellpod, explosive, incendiary |
| 输入指令 (`code`) | down, left, left, down |
| 冷却时间（秒） (`cooldownS`) | 120 |
| `cooldownVariants\[1\].label` | With Morale Augmentation |
| `cooldownVariants\[1\].seconds` | 114 |
| `cooldownVariants\[2\].label` | With Synthetic Supplementation |
| `cooldownVariants\[2\].seconds` | 108 |
| `cooldownVariants\[3\].label` | With All Upgrades |
| `cooldownVariants\[3\].seconds` | 102.6 |
| 呼叫时间（秒） (`callInTimeS`) | 3 |
| `callInTimeUpgradedS` | 4.75 |
| 使用次数 (`uses`) | unlimited |
| `unlockLevel` | 8 |
| `shipModules\[1\].department` | bridge |
| `shipModules\[1\].module` | Enhanced Combustion |
| `shipModules\[1\].effect` | Fire damage from Stratagems increased by 25%. |
| `shipModules\[2\].department` | bridge |
| `shipModules\[2\].module` | Morale Augmentation |
| `shipModules\[2\].effect` | Reduces cooldown time for all Stratagems by 5%. |
| `shipModules\[3\].department` | engineering_bay |
| `shipModules\[3\].module` | Synthetic Supplementation |
| `shipModules\[3\].effect` | Reduces cooldown time for Sentry, Emplacement, and Resupply stratagems by 10%. |
| `shipModules\[4\].department` | engineering_bay |
| `shipModules\[4\].module` | Rapid Launch System |
| `shipModules\[4\].effect` | Removes deployment time for Emplacement stratagems. |


## 攻击模式、伤害与穿甲

### 1. Incendiary Mine（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 300 |
| `damage.durable` | 300 |
| `damage.type` | Explosion |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 1.2 |
| `area.outerRadiusM` | 4 |
| `area.shockwaveRadiusM` | 7 |
| `forces.demolition` | 30 |
| `forces.stagger` | 30 |
| `forces.push` | 30 |


### 2. DPS Fire（other）

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


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | requisition |
| `label` | Engineering Bay |
| 战争债券 ID (`warbondId`) | — |
| `page` | — |
| `cost.currency` | requisition |
| `cost.amount` | 4000 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/md-i4-incendiary-mines.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/MD-I4_Incendiary_Mines
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

