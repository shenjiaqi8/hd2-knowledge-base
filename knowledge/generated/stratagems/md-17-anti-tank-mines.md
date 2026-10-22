---
id: "md-17-anti-tank-mines"
name: "MD-17 Anti-Tank Mines"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/MD-17_Anti-Tank_Mines"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/md-17-anti-tank-mines.json"
---

# MD-17 Anti-Tank Mines

**分类：** 战略配备 (`stratagems`) · **ID：** `md-17-anti-tank-mines`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/MD-17_Anti-Tank_Mines

## 简介

The MD-17 Anti-Tank Mines (simply known as AT Mines) are a defensive Stratagem which deploys a minefield of armor penetrating mines.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | defensive |
| `availability` | loadout |
| 类别 (`category`) | engineering_bay |
| 类型 (`kind`) | emplacement |
| 特性 ID (`traitIds`) | hellpod, explosive, anti-tank |
| 输入指令 (`code`) | down, left, up, up |
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
| `shipModules\[3\].module` | Rapid Launch System |
| `shipModules\[3\].effect` | Removes deployment time for Emplacement stratagems. |


## 攻击模式、伤害与穿甲

### 1. Anti Tank Mine（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 2000 |
| `damage.durable` | 2000 |
| `damage.type` | Explosion |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 3 |
| `area.outerRadiusM` | 7 |
| `area.shockwaveRadiusM` | 14 |
| `forces.demolition` | 40 |
| `forces.stagger` | 30 |
| `forces.push` | 40 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | requisition |
| `label` | Engineering Bay |
| 战争债券 ID (`warbondId`) | — |
| `page` | — |
| `cost.currency` | requisition |
| `cost.amount` | 7000 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/md-17-anti-tank-mines.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/MD-17_Anti-Tank_Mines
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

