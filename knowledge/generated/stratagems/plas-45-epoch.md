---
id: "plas-45-epoch"
name: "PLAS-45 Epoch"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/PLAS-45_Epoch"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/plas-45-epoch.json"
---

# PLAS-45 Epoch

**分类：** 战略配备 (`stratagems`) · **ID：** `plas-45-epoch`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/PLAS-45_Epoch

## 简介

The PLAS-45 Epoch is an energy-based plasma Support Weapon Stratagem with Heavy armor penetration that scales armor penetration and damage.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | supply |
| `availability` | loadout |
| 类型 (`kind`) | support_weapon |
| 特性 ID (`traitIds`) | support-weapon, explosive, heavy-armor-penetrating, stationary-reload, chargeup |
| 输入指令 (`code`) | down, left, up, left, right |
| 冷却时间（秒） (`cooldownS`) | 480 |
| `cooldownVariants\[1\].label` | With Morale Augmentation |
| `cooldownVariants\[1\].seconds` | 456 |
| 呼叫时间（秒） (`callInTimeS`) | 7.75 |
| `callInTimeUpgradedS` | 4.75 |
| 使用次数 (`uses`) | unlimited |
| `shipModules\[1\].department` | patriotic_administration_center |
| `shipModules\[1\].module` | Donation Access License |
| `shipModules\[1\].effect` | Support Weapons deploy with the maximum number of carriable magazines. |
| `shipModules\[2\].department` | patriotic_administration_center |
| `shipModules\[2\].module` | Streamlined Request Process |
| `shipModules\[2\].effect` | Decreases Support Weapon stratagem cooldown by 10%. |
| `shipModules\[3\].department` | patriotic_administration_center |
| `shipModules\[3\].module` | Superior Packing Methodology |
| `shipModules\[3\].effect` | Resupply stratagem boxes refill Support Weapons with the maximum number of carriable magazines. |
| `shipModules\[4\].department` | patriotic_administration_center |
| `shipModules\[4\].module` | Payroll Management System |
| `shipModules\[4\].effect` | Reduce reload time for all support weapons by 10%. |
| `shipModules\[5\].department` | bridge |
| `shipModules\[5\].module` | Morale Augmentation |
| `shipModules\[5\].effect` | Reduces cooldown time for all Stratagems by 5%. |
| `shipModules\[6\].department` | engineering_bay |
| `shipModules\[6\].module` | Streamlined Launch Process |
| `shipModules\[6\].effect` | All Support Weapon stratagems launch immediately once called in, reducing overall deployment time. |


## 攻击模式、伤害与穿甲

### 1. P3（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 400 |
| `damage.durable` | 200 |
| `damage.type` | Ballistic |
| `penetration.direct` | anti_tank_i |
| `penetration.slightAngle` | anti_tank_i |
| `penetration.largeAngle` | anti_tank_i |
| `penetration.extremeAngle` | anti_tank_i |
| `projectile.pellets` | — |
| `projectile.massG` | 100 |
| `projectile.initialVelocityMps` | 250 |
| `projectile.dragFactorPct` | 10 |
| `projectile.gravityFactorPct` | 200 |
| `projectile.penetrationSlowdownPct` | 35 |
| `area` | — |
| `forces.demolition` | 10 |
| `forces.stagger` | 30 |
| `forces.push` | 15 |


### 2. P3 IE（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 800 |
| `damage.durable` | 800 |
| `damage.type` | Explosion |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 3 |
| `area.outerRadiusM` | 4 |
| `area.shockwaveRadiusM` | 5 |
| `forces.demolition` | 30 |
| `forces.stagger` | 35 |
| `forces.push` | 30 |


### 3. PLAS-45 P（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 400 |
| `damage.durable` | 200 |
| `damage.type` | Ballistic |
| `penetration.direct` | heavy |
| `penetration.slightAngle` | heavy |
| `penetration.largeAngle` | heavy |
| `penetration.extremeAngle` | heavy |
| `projectile.pellets` | — |
| `projectile.massG` | 100 |
| `projectile.initialVelocityMps` | 250 |
| `projectile.dragFactorPct` | 10 |
| `projectile.gravityFactorPct` | 200 |
| `projectile.penetrationSlowdownPct` | 35 |
| `area` | — |
| `forces.demolition` | 10 |
| `forces.stagger` | 30 |
| `forces.push` | 15 |


### 4. PLAS-45 P IE（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 500 |
| `damage.durable` | 500 |
| `damage.type` | Explosion |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 2.29999995 |
| `area.outerRadiusM` | 3 |
| `area.shockwaveRadiusM` | 4 |
| `forces.demolition` | 10 |
| `forces.stagger` | 20 |
| `forces.push` | 7 |


### 5. PLAS-45 EPOCH Overcharge E（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 800 |
| `damage.durable` | 800 |
| `damage.type` | Explosion |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 3 |
| `area.outerRadiusM` | 4 |
| `area.shockwaveRadiusM` | 5 |
| `forces.demolition` | 30 |
| `forces.stagger` | 35 |
| `forces.push` | 30 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | warbond |
| `label` | Control Group P1 |
| 战争债券 ID (`warbondId`) | control-group |
| `page` | 1 |
| `cost.currency` | medals |
| `cost.amount` | 75 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/plas-45-epoch.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/PLAS-45_Epoch
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

