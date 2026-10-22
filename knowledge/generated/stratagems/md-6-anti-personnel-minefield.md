---
id: "md-6-anti-personnel-minefield"
name: "MD-6 Anti-Personnel Minefield"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/MD-6_Anti-Personnel_Minefield"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/md-6-anti-personnel-minefield.json"
---

# MD-6 Anti-Personnel Minefield

**分类：** 战略配备 (`stratagems`) · **ID：** `md-6-anti-personnel-minefield`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/MD-6_Anti-Personnel_Minefield

## 简介

The MD-6 Anti-Personnel Minefield is a defensive stratagem that blankets a roughly 25-30 meter diameter area around itself with mines.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | defensive |
| `availability` | loadout |
| 类别 (`category`) | engineering_bay |
| 类型 (`kind`) | emplacement |
| 特性 ID (`traitIds`) | hellpod, explosive, medium-armor-penetrating |
| 输入指令 (`code`) | down, left, up, right |
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
| `unlockLevel` | 1 |
| `shipModules\[1\].department` | bridge |
| `shipModules\[1\].module` | Morale Augmentation |
| `shipModules\[1\].effect` | Reduces cooldown time for all Stratagems by 5%. |
| `shipModules\[2\].department` | engineering_bay |
| `shipModules\[2\].module` | Synthetic Supplementation |
| `shipModules\[2\].effect` | Reduces cooldown time for Sentry, Emplacement, and Resupply stratagems by 10%. |
| `shipModules\[3\].department` | engineering_bay |
| `shipModules\[3\].module` | Rapid Launch System |
| `shipModules\[3\].effect` | Removes deployment time for Emplacement stratagems. |


## 攻击模式、伤害与穿甲

### 1. Contact Mine（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 700 |
| `damage.durable` | 700 |
| `damage.type` | Explosion |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 1.2 |
| `area.outerRadiusM` | 5 |
| `area.shockwaveRadiusM` | 7 |
| `forces.demolition` | 30 |
| `forces.stagger` | 30 |
| `forces.push` | 30 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | requisition |
| `label` | Engineering Bay |
| 战争债券 ID (`warbondId`) | — |
| `page` | — |
| `cost.currency` | requisition |
| `cost.amount` | 1500 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/md-6-anti-personnel-minefield.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/MD-6_Anti-Personnel_Minefield
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

