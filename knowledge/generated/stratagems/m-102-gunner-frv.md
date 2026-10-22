---
id: "m-102-gunner-frv"
name: "M-102 Gunner FRV"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/M-102_Gunner_FRV"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/m-102-gunner-frv.json"
---

# M-102 Gunner FRV

**分类：** 战略配备 (`stratagems`) · **ID：** `m-102-gunner-frv`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/M-102_Gunner_FRV

## 简介

The M-102 Gunner FRV is a Stratagem that deploys a four-wheeled ground vehicle with a mounted MG-206 Heavy Machine Gun.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | supply |
| `availability` | loadout |
| 类别 (`category`) | hangar |
| 类型 (`kind`) | vehicle |
| 特性 ID (`traitIds`) | vehicle, heavy-armor-penetrating |
| 输入指令 (`code`) | left, down, right, down, right, down, up |
| 冷却时间（秒） (`cooldownS`) | 480 |
| `cooldownVariants\[1\].label` | With Morale Augmentation |
| `cooldownVariants\[1\].seconds` | 456 |
| 呼叫时间（秒） (`callInTimeS`) | 10.5 |
| 使用次数 (`uses`) | unlimited |
| `unlockLevel` | 25 |
| `shipModules\[1\].department` | bridge |
| `shipModules\[1\].module` | Morale Augmentation |
| `shipModules\[1\].effect` | Reduces cooldown time for all stratagems by 5%. |


## 攻击模式、伤害与穿甲

### 1. MG-206 P（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 150 |
| `damage.durable` | 35 |
| `damage.type` | Ballistic |
| `penetration.direct` | heavy |
| `penetration.slightAngle` | heavy |
| `penetration.largeAngle` | heavy |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | — |
| `projectile.massG` | 52 |
| `projectile.initialVelocityMps` | 980 |
| `projectile.dragFactorPct` | 30 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 15 |
| `forces.stagger` | 25 |
| `forces.push` | 20 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | requisition |
| `label` | Hangar |
| 战争债券 ID (`warbondId`) | — |
| `page` | — |
| `cost.currency` | requisition |
| `cost.amount` | 25000 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/m-102-gunner-frv.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/M-102_Gunner_FRV
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

