---
id: "mls-4x-commando"
name: "MLS-4X Commando"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/MLS-4X_Commando"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/mls-4x-commando.json"
---

# MLS-4X Commando

**分类：** 战略配备 (`stratagems`) · **ID：** `mls-4x-commando`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/MLS-4X_Commando

## 简介

The Commando is a disposable four-barrel anti-tank rocket launcher Support Weapon that can be fired with or without laser-guidance.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | supply |
| `availability` | loadout |
| 类别 (`category`) | patriotic_administration_center |
| 类型 (`kind`) | support_weapon |
| 特性 ID (`traitIds`) | support-weapon, anti-tank, expendable |
| 输入指令 (`code`) | down, left, up, down, right |
| 冷却时间（秒） (`cooldownS`) | 120 |
| `cooldownVariants\[1\].label` | With Morale Augmentation |
| `cooldownVariants\[1\].seconds` | 114 |
| 呼叫时间（秒） (`callInTimeS`) | 7.75 |
| `callInTimeUpgradedS` | 4.75 |
| 使用次数 (`uses`) | unlimited |
| `unlockLevel` | 15 |
| `shipModules\[1\].department` | patriotic_administration_center |
| `shipModules\[1\].module` | Streamlined Request Process |
| `shipModules\[1\].effect` | Decreases Support Weapon stratagem cooldown by 10%. |
| `shipModules\[2\].department` | bridge |
| `shipModules\[2\].module` | Morale Augmentation |
| `shipModules\[2\].effect` | Reduces cooldown time for all Stratagems by 5%. |
| `shipModules\[3\].department` | engineering_bay |
| `shipModules\[3\].module` | Streamlined Launch Process |
| `shipModules\[3\].effect` | All Support Weapons launch once called in, reducing overall deployment time. |


## 攻击模式、伤害与穿甲

### 1. MLS-4X BACKBLAST E（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 5 |
| `damage.durable` | 5 |
| `damage.type` | Explosion |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 1 |
| `area.outerRadiusM` | 2 |
| `area.shockwaveRadiusM` | 3 |
| `forces.demolition` | 10 |
| `forces.stagger` | 20 |
| `forces.push` | 10 |


### 2. MLS-4X P（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 1100 |
| `damage.durable` | 1100 |
| `damage.type` | Ballistic |
| `penetration.direct` | anti_tank_ii |
| `penetration.slightAngle` | anti_tank_ii |
| `penetration.largeAngle` | anti_tank_ii |
| `penetration.extremeAngle` | medium |
| `projectile.pellets` | — |
| `projectile.massG` | 350 |
| `projectile.initialVelocityMps` | 70 |
| `projectile.dragFactorPct` | 0 |
| `projectile.gravityFactorPct` | 0 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 30 |
| `forces.stagger` | 40 |
| `forces.push` | 25 |


### 3. MLS-4X P IE（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 150 |
| `damage.durable` | 150 |
| `damage.type` | Explosion |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 1 |
| `area.outerRadiusM` | 2 |
| `area.shockwaveRadiusM` | 4 |
| `forces.demolition` | 30 |
| `forces.stagger` | 40 |
| `forces.push` | 40 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | requisition |
| `label` | Patriotic Administration Center |
| 战争债券 ID (`warbondId`) | — |
| `page` | — |
| `cost.currency` | requisition |
| `cost.amount` | 8000 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/mls-4x-commando.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/MLS-4X_Commando
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

