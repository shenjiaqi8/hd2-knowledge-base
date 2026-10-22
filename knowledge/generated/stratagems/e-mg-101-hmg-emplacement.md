---
id: "e-mg-101-hmg-emplacement"
name: "E/MG-101 HMG Emplacement"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/E/MG-101_HMG_Emplacement"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/e-mg-101-hmg-emplacement.json"
---

# E/MG-101 HMG Emplacement

**分类：** 战略配备 (`stratagems`) · **ID：** `e-mg-101-hmg-emplacement`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/E/MG-101_HMG_Emplacement

## 简介

The HMG Emplacement is a Stratagem that deploys a static, manually operated machine gun emplacement.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | defensive |
| `availability` | loadout |
| 类别 (`category`) | bridge |
| 类型 (`kind`) | emplacement |
| 特性 ID (`traitIds`) | hellpod, heavy-armor-penetrating |
| 输入指令 (`code`) | down, up, left, right, right, left |
| 冷却时间（秒） (`cooldownS`) | 180 |
| `cooldownVariants\[1\].label` | With Morale Augmentation |
| `cooldownVariants\[1\].seconds` | 171 |
| `cooldownVariants\[2\].label` | With Synthetic Supplementation |
| `cooldownVariants\[2\].seconds` | 162 |
| `cooldownVariants\[3\].label` | With All Upgrades |
| `cooldownVariants\[3\].seconds` | 153.9 |
| 呼叫时间（秒） (`callInTimeS`) | 3 |
| `callInTimeUpgradedS` | 4.75 |
| 使用次数 (`uses`) | unlimited |
| `unlockLevel` | 10 |
| `shipModules\[1\].department` | bridge |
| `shipModules\[1\].module` | Morale Augmentation |
| `shipModules\[1\].effect` | Reduces cooldown time for all stratagems by 5%. |
| `shipModules\[2\].department` | engineering_bay |
| `shipModules\[2\].module` | Synthetic Supplementation |
| `shipModules\[2\].effect` | Reduces cooldown time for Sentry, Emplacement, and Resupply stratagems by 10%. |
| `shipModules\[3\].department` | engineering_bay |
| `shipModules\[3\].module` | Rapid Launch System |
| `shipModules\[3\].effect` | Removes deployment time for Emplacement stratagems. |


## 攻击模式、伤害与穿甲

### 1. Rifle 12.5x100mm Full Metal Jacket（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 200 |
| `damage.durable` | 40 |
| `damage.type` | Damage |
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
| `forces.push` | 15 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | requisition |
| `label` | Bridge |
| 战争债券 ID (`warbondId`) | — |
| `page` | — |
| `cost.currency` | requisition |
| `cost.amount` | 10000 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/e-mg-101-hmg-emplacement.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/E/MG-101_HMG_Emplacement
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

