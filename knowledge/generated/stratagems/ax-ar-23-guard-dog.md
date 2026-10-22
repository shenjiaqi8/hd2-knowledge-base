---
id: "ax-ar-23-guard-dog"
name: "AX/AR-23 Guard Dog"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated", "broken_file_links"]
wiki_url: "https://helldivers.wiki.gg/wiki/AX/AR-23_Guard_Dog"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/ax-ar-23-guard-dog.json"
---

# AX/AR-23 Guard Dog

**分类：** 战略配备 (`stratagems`) · **ID：** `ax-ar-23-guard-dog`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/AX/AR-23_Guard_Dog

## 简介

The AX/AR-23 Guard Dog is a Stratagem that calls down a defensive drone that is equipped in the backpack slot.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | supply |
| `availability` | loadout |
| 类别 (`category`) | engineering_bay |
| 类型 (`kind`) | backpack |
| 特性 ID (`traitIds`) | hellpod, backpack, medium-armor-penetrating |
| 输入指令 (`code`) | down, up, left, up, right, down |
| 冷却时间（秒） (`cooldownS`) | 480 |
| `cooldownVariants\[1\].label` | With Morale Augmentation |
| `cooldownVariants\[1\].seconds` | 456 |
| `cooldownVariants\[2\].label` | With Hand Carts |
| `cooldownVariants\[2\].seconds` | 432 |
| `cooldownVariants\[3\].label` | With All Upgrades |
| `cooldownVariants\[3\].seconds` | 410.4 |
| 呼叫时间（秒） (`callInTimeS`) | 9.75 |
| 使用次数 (`uses`) | unlimited |
| `unlockLevel` | 10 |
| `shipModules\[1\].department` | patriotic_administration_center |
| `shipModules\[1\].module` | Hand Carts |
| `shipModules\[1\].effect` | Decreases cooldown for all Backpack stratagems by 10%. |
| `shipModules\[2\].department` | bridge |
| `shipModules\[2\].module` | Morale Augmentation |
| `shipModules\[2\].effect` | Reduces cooldown time for all Stratagems by 5%. |
| `backpack.health` | 100 |
| `backpack.armor` | very_light |
| `backpack.capacity` | — |


## 攻击模式、伤害与穿甲

### 1. AR-23P P（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 65 |
| `damage.durable` | 15 |
| `damage.type` | Ballistic |
| `penetration.direct` | medium |
| `penetration.slightAngle` | medium |
| `penetration.largeAngle` | medium |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | — |
| `projectile.massG` | 4.5 |
| `projectile.initialVelocityMps` | 1000 |
| `projectile.dragFactorPct` | 30 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 10 |
| `forces.stagger` | 10 |
| `forces.push` | 10 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | requisition |
| `label` | Engineering Bay |
| 战争债券 ID (`warbondId`) | — |
| `page` | — |
| `cost.currency` | requisition |
| `cost.amount` | 7500 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/ax-ar-23-guard-dog.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/AX/AR-23_Guard_Dog
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

