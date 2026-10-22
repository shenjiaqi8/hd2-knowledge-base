---
id: "rl-77-airburst-rocket-launcher"
name: "RL-77 Airburst Rocket Launcher"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/RL-77_Airburst_Rocket_Launcher"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/rl-77-airburst-rocket-launcher.json"
---

# RL-77 Airburst Rocket Launcher

**分类：** 战略配备 (`stratagems`) · **ID：** `rl-77-airburst-rocket-launcher`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/RL-77_Airburst_Rocket_Launcher

## 简介

The RL-77 Airburst Rocket Launcher, also known as the ABRL, is a Support Weapon that fires a cluster rocket designed for neutralizing several light-medium enemies with a single shot.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | supply |
| `availability` | loadout |
| 类别 (`category`) | patriotic_administration_center |
| 类型 (`kind`) | support_weapon |
| 特性 ID (`traitIds`) | support-weapon, backpack, medium-armor-penetrating, stationary-reload |
| 输入指令 (`code`) | down, up, up, left, right |
| 冷却时间（秒） (`cooldownS`) | 480 |
| `cooldownVariants\[1\].label` | With Morale Augmentation |
| `cooldownVariants\[1\].seconds` | 456 |
| 呼叫时间（秒） (`callInTimeS`) | 7.75 |
| `callInTimeUpgradedS` | 4.75 |
| 使用次数 (`uses`) | unlimited |
| `unlockLevel` | 15 |
| `shipModules\[1\].department` | patriotic_administration_center |
| `shipModules\[1\].module` | Streamlined Request Process |
| `shipModules\[1\].effect` | Decreases Support Weapon stratagem cooldown by 10%. |
| `shipModules\[2\].department` | patriotic_administration_center |
| `shipModules\[2\].module` | Superior Packing Methodology |
| `shipModules\[2\].effect` | Resupply stratagem boxes refill Support Weapons with the maximum number of carriable magazines. |
| `shipModules\[3\].department` | patriotic_administration_center |
| `shipModules\[3\].module` | Payroll Management System |
| `shipModules\[3\].effect` | Reduces reload time for all support weapons by 10%. |
| `shipModules\[4\].department` | bridge |
| `shipModules\[4\].module` | Morale Augmentation |
| `shipModules\[4\].effect` | Reduces cooldown time for all Stratagems by 5%. |
| `shipModules\[5\].department` | engineering_bay |
| `shipModules\[5\].module` | Streamlined Launch Process |
| `shipModules\[5\].effect` | All Support Weapons launch immediately once called in, reducing overall deployment time. |


## 攻击模式、伤害与穿甲

### 1. GR-8 BACKBLAST E（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 20 |
| `damage.durable` | 20 |
| `damage.type` | Explosion |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 1 |
| `area.outerRadiusM` | 8 |
| `area.shockwaveRadiusM` | 9 |
| `forces.demolition` | 10 |
| `forces.stagger` | 30 |
| `forces.push` | 20 |


### 2. RL-77 P（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 350 |
| `damage.durable` | 350 |
| `damage.type` | Ballistic |
| `penetration.direct` | medium |
| `penetration.slightAngle` | medium |
| `penetration.largeAngle` | medium |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | — |
| `projectile.massG` | 3300 |
| `projectile.initialVelocityMps` | 250 |
| `projectile.dragFactorPct` | 30 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 30 |
| `forces.stagger` | 50 |
| `forces.push` | 40 |


### 3. RL-77 P IE（explosion）

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
| `area.innerRadiusM` | 3 |
| `area.outerRadiusM` | 5 |
| `area.shockwaveRadiusM` | 7 |
| `forces.demolition` | 25 |
| `forces.stagger` | 25 |
| `forces.push` | 40 |


### 4. RL-77 P1（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 150 |
| `damage.durable` | 150 |
| `damage.type` | Ballistic |
| `penetration.direct` | medium |
| `penetration.slightAngle` | medium |
| `penetration.largeAngle` | medium |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | — |
| `projectile.massG` | 100 |
| `projectile.initialVelocityMps` | 25 |
| `projectile.dragFactorPct` | 50 |
| `projectile.gravityFactorPct` | 400 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 25 |
| `forces.stagger` | 25 |
| `forces.push` | 40 |


### 5. RL-77 P1 IE（explosion）

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
| `area.innerRadiusM` | 4 |
| `area.outerRadiusM` | 6 |
| `area.shockwaveRadiusM` | 8 |
| `forces.demolition` | 20 |
| `forces.stagger` | 25 |
| `forces.push` | 40 |


### 6. RL-77 P2（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 350 |
| `damage.durable` | 350 |
| `damage.type` | Ballistic |
| `penetration.direct` | medium |
| `penetration.slightAngle` | medium |
| `penetration.largeAngle` | medium |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | — |
| `projectile.massG` | 3300 |
| `projectile.initialVelocityMps` | 250 |
| `projectile.dragFactorPct` | 30 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 30 |
| `forces.stagger` | 50 |
| `forces.push` | 40 |


### 7. RL-77 P2 IE（explosion）

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
| `area.innerRadiusM` | 3 |
| `area.outerRadiusM` | 5 |
| `area.shockwaveRadiusM` | 7 |
| `forces.demolition` | 25 |
| `forces.stagger` | 25 |
| `forces.push` | 40 |


### 8. RL-77 P3（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 150 |
| `damage.durable` | 150 |
| `damage.type` | Ballistic |
| `penetration.direct` | medium |
| `penetration.slightAngle` | medium |
| `penetration.largeAngle` | medium |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | — |
| `projectile.massG` | 100 |
| `projectile.initialVelocityMps` | 25 |
| `projectile.dragFactorPct` | 50 |
| `projectile.gravityFactorPct` | 400 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 25 |
| `forces.stagger` | 25 |
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
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/rl-77-airburst-rocket-launcher.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/RL-77_Airburst_Rocket_Launcher
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

