---
id: "td-220-bastion-mk-xvi"
name: "TD-220 Bastion MK XVI"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/TD-220_Bastion_MK_XVI"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/td-220-bastion-mk-xvi.json"
---

# TD-220 Bastion MK XVI

**分类：** 战略配备 (`stratagems`) · **ID：** `td-220-bastion-mk-xvi`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/TD-220_Bastion_MK_XVI

## 简介

The TD-220 Bastion MK XVI is a Stratagem that deploys a tracked ground vehicle armed with a 120mm HV cannon and a heavy coaxial MG.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | supply |
| `availability` | loadout |
| 类别 (`category`) | hangar |
| 类型 (`kind`) | vehicle |
| 特性 ID (`traitIds`) | vehicle, explosive, anti-tank, heavy-armor-penetrating |
| 输入指令 (`code`) | left, down, right, down, left, down, up, down, up |
| 冷却时间（秒） (`cooldownS`) | 780 |
| `cooldownVariants\[1\].label` | With Morale Augmentation |
| `cooldownVariants\[1\].seconds` | 741 |
| 呼叫时间（秒） (`callInTimeS`) | 10.5 |
| 使用次数 (`uses`) | unlimited |
| `unlockLevel` | 30 |
| `shipModules\[1\].department` | bridge |
| `shipModules\[1\].module` | Morale Augmentation |
| `shipModules\[1\].effect` | Reduces cooldown time for all stratagems by 5%. |


## 攻击模式、伤害与穿甲

### 1. P10（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 3500 |
| `damage.durable` | 3500 |
| `damage.type` | Ballistic |
| `penetration.direct` | anti_tank_iv |
| `penetration.slightAngle` | anti_tank_iii |
| `penetration.largeAngle` | anti_tank_ii |
| `penetration.extremeAngle` | anti_tank_ii |
| `projectile.pellets` | — |
| `projectile.massG` | 5000 |
| `projectile.initialVelocityMps` | 400 |
| `projectile.dragFactorPct` | 0 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 40 |
| `forces.stagger` | 50 |
| `forces.push` | 20 |


### 2. P10 IE（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 750 |
| `damage.durable` | 750 |
| `damage.type` | Explosion |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 3.29999995 |
| `area.outerRadiusM` | 10 |
| `area.shockwaveRadiusM` | 11 |
| `forces.demolition` | 40 |
| `forces.stagger` | 70 |
| `forces.push` | 40 |


### 3. MG-206 P（projectile）

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
| `cost.amount` | 35000 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/td-220-bastion-mk-xvi.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/TD-220_Bastion_MK_XVI
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

