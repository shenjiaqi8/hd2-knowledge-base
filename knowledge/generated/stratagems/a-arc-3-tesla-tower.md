---
id: "a-arc-3-tesla-tower"
name: "A/ARC-3 Tesla Tower"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/A/ARC-3_Tesla_Tower"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/a-arc-3-tesla-tower.json"
---

# A/ARC-3 Tesla Tower

**分类：** 战略配备 (`stratagems`) · **ID：** `a-arc-3-tesla-tower`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/A/ARC-3_Tesla_Tower

## 简介

The A/ARC-3 Tesla Tower is a Sentry that sends electric arcs toward all entities within 20 meters.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | defensive |
| `availability` | loadout |
| 类别 (`category`) | bridge |
| 类型 (`kind`) | sentry |
| 特性 ID (`traitIds`) | hellpod, sentry, arc |
| 输入指令 (`code`) | down, up, right, up, left, right |
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
| `unlockLevel` | 15 |
| `shipModules\[1\].department` | bridge |
| `shipModules\[1\].module` | Morale Augmentation |
| `shipModules\[1\].effect` | Reduces cooldown time for all Stratagems by 5%. |
| `shipModules\[2\].department` | engineering_bay |
| `shipModules\[2\].module` | Synthetic Supplementation |
| `shipModules\[2\].effect` | Reduces cooldown time for Sentry, Emplacement, and Resupply stratagems by 10%. |
| `shipModules\[3\].department` | engineering_bay |
| `shipModules\[3\].module` | Advanced Construction |
| `shipModules\[3\].effect` | Increases health of Sentry stratagems by 50%. |
| `shipModules\[4\].department` | engineering_bay |
| `shipModules\[4\].module` | Rapid Launch System |
| `shipModules\[4\].effect` | Removes deployment time for Emplacement stratagems. |
| `shipModules\[5\].department` | engineering_bay |
| `shipModules\[5\].module` | Circuit Expansion |
| `shipModules\[5\].effect` | Lightning arcs, fired from weapons and turrets, jump to two additional enemies. |
| `shipModules\[6\].department` | robotics_workshop |
| `shipModules\[6\].module` | Blast Absorption |
| `shipModules\[6\].effect` | Sentries take 50% less damage from explosions. |


## 攻击模式、伤害与穿甲

### 1. Tesla Turret Arc（arc）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 600 |
| `damage.durable` | 600 |
| `damage.type` | Arc |
| `penetration.direct` | heavy |
| `penetration.slightAngle` | heavy |
| `penetration.largeAngle` | heavy |
| `penetration.extremeAngle` | unarmored |
| `projectile` | — |
| `area` | — |
| `forces.demolition` | 20 |
| `forces.stagger` | 20 |
| `forces.push` | 10 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | requisition |
| `label` | Bridge |
| 战争债券 ID (`warbondId`) | — |
| `page` | — |
| `cost.currency` | requisition |
| `cost.amount` | 8000 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/a-arc-3-tesla-tower.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/A/ARC-3_Tesla_Tower
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

