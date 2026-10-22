---
id: "m-103-supply-frv"
name: "M-103 Supply FRV"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["broken_file_links"]
wiki_url: "https://helldivers.wiki.gg/wiki/M-103_Supply_FRV"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/m-103-supply-frv.json"
---

# M-103 Supply FRV

**分类：** 战略配备 (`stratagems`) · **ID：** `m-103-supply-frv`

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/M-103_Supply_FRV

## 简介

The M-103 Supply FRV is a Stratagem that deploys a four-wheeled ground vehicle, equipped with supplies and an automatic turret.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | supply |
| `availability` | loadout |
| 类别 (`category`) | hangar |
| 类型 (`kind`) | vehicle |
| 特性 ID (`traitIds`) | vehicle, medium-armor-penetrating |
| 输入指令 (`code`) | left, down, left, left, down, up, right |
| 冷却时间（秒） (`cooldownS`) | 480 |
| `cooldownVariants\[1\].label` | With Morale Augmentation |
| `cooldownVariants\[1\].seconds` | 456 |
| 呼叫时间（秒） (`callInTimeS`) | 10.5 |
| 使用次数 (`uses`) | unlimited |
| `shipModules\[1\].department` | bridge |
| `shipModules\[1\].module` | Morale Augmentation |
| `shipModules\[1\].effect` | Reduces cooldown time for all stratagems by 5%. |


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
| `label` | Hanger |
| 战争债券 ID (`warbondId`) | — |
| `page` | — |
| `cost.currency` | requisition |
| `cost.amount` | 25000 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/m-103-supply-frv.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/M-103_Supply_FRV
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

