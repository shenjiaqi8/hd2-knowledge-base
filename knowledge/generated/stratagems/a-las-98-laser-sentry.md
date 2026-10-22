---
id: "a-las-98-laser-sentry"
name: "A/LAS-98 Laser Sentry"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/A/LAS-98_Laser_Sentry"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/a-las-98-laser-sentry.json"
---

# A/LAS-98 Laser Sentry

**分类：** 战略配备 (`stratagems`) · **ID：** `a-las-98-laser-sentry`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/A/LAS-98_Laser_Sentry

## 简介

The Laser Sentry is a close-range incendiary sentry stratagem from the Control Group Warbond.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | defensive |
| `availability` | loadout |
| 类型 (`kind`) | sentry |
| 特性 ID (`traitIds`) | hellpod, sentry, heavy-armor-penetrating, heat, beam |
| 输入指令 (`code`) | down, up, right, down, up, right |
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
| `shipModules\[5\].module` | High-Quality Lubricant |
| `shipModules\[5\].effect` | Increases the rotation speed of the Sentry stratagems. |
| `shipModules\[6\].department` | robotics_workshop |
| `shipModules\[6\].module` | Blast Absorption |
| `shipModules\[6\].effect` | Sentries takes 50% less damage from explosions. |


## 攻击模式、伤害与穿甲

### 1. LASER SENTRY B（beam）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 350 |
| `damage.durable` | 200 |
| `damage.type` | Laser |
| `penetration.direct` | heavy |
| `penetration.slightAngle` | heavy |
| `penetration.largeAngle` | heavy |
| `penetration.extremeAngle` | heavy |
| `projectile` | — |
| `area` | — |
| `forces.demolition` | 20 |
| `forces.stagger` | 0 |
| `forces.push` | 0 |


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


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | warbond |
| `label` | Control Group P2 |
| 战争债券 ID (`warbondId`) | control-group |
| `page` | 2 |
| `cost.currency` | medals |
| `cost.amount` | 85 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/a-las-98-laser-sentry.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/A/LAS-98_Laser_Sentry
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

