---
id: "gr-8-recoilless-rifle"
name: "GR-8 Recoilless Rifle"
collection: "stratagems"
aliases: ["RR"]
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/GR-8_Recoilless_Rifle"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/gr-8-recoilless-rifle.json"
---

# GR-8 Recoilless Rifle

**分类：** 战略配备 (`stratagems`) · **ID：** `gr-8-recoilless-rifle`

**别名：** RR

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/GR-8_Recoilless_Rifle

## 简介

The GR-8 Recoilless Rifle (abbreviated as RR) is a reloadable anti-tank Support Weapon Stratagem with a programmable anti-personnel HE shell option.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | supply |
| `availability` | loadout |
| 类别 (`category`) | patriotic_administration_center |
| 类型 (`kind`) | support_weapon |
| 特性 ID (`traitIds`) | support-weapon, backpack, anti-tank, stationary-reload |
| 输入指令 (`code`) | down, left, right, right, left |
| 冷却时间（秒） (`cooldownS`) | 480 |
| `cooldownVariants\[1\].label` | With Morale Augmentation |
| `cooldownVariants\[1\].seconds` | 456 |
| 呼叫时间（秒） (`callInTimeS`) | 7.75 |
| `callInTimeUpgradedS` | 4.75 |
| 使用次数 (`uses`) | unlimited |
| `unlockLevel` | 5 |
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
| `shipModules\[4\].effect` | Reduces cooldown time for all stratagems by 5%. |
| `shipModules\[5\].department` | engineering_bay |
| `shipModules\[5\].module` | Streamlined Launch Process |
| `shipModules\[5\].effect` | All Support Weapon stratagems launch immediately once called in, reducing overall deployment time. |


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


### 2. GR-8 P（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 3200 |
| `damage.durable` | 3200 |
| `damage.type` | Ballistic |
| `penetration.direct` | anti_tank_ii |
| `penetration.slightAngle` | anti_tank_ii |
| `penetration.largeAngle` | anti_tank_ii |
| `penetration.extremeAngle` | medium |
| `projectile.pellets` | — |
| `projectile.massG` | 3300 |
| `projectile.initialVelocityMps` | 250 |
| `projectile.dragFactorPct` | 30 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 30 |
| `forces.stagger` | 50 |
| `forces.push` | 25 |


### 3. GR-8 P IE（explosion）

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
| `area.innerRadiusM` | 1.5 |
| `area.outerRadiusM` | 3 |
| `area.shockwaveRadiusM` | 6 |
| `forces.demolition` | 30 |
| `forces.stagger` | 50 |
| `forces.push` | 40 |


### 4. GR-8 P1（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 750 |
| `damage.durable` | 750 |
| `damage.type` | Ballistic |
| `penetration.direct` | anti_tank_i |
| `penetration.slightAngle` | anti_tank_i |
| `penetration.largeAngle` | anti_tank_i |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | — |
| `projectile.massG` | 3300 |
| `projectile.initialVelocityMps` | 250 |
| `projectile.dragFactorPct` | 0 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 85 |
| `area` | — |
| `forces.demolition` | 30 |
| `forces.stagger` | 50 |
| `forces.push` | 25 |


### 5. GR-8 P1 IE（explosion）

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
| `area.outerRadiusM` | 7.5 |
| `area.shockwaveRadiusM` | 12 |
| `forces.demolition` | 30 |
| `forces.stagger` | 60 |
| `forces.push` | 40 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | requisition |
| `label` | Patriotic Administration Center |
| 战争债券 ID (`warbondId`) | — |
| `page` | — |
| `cost.currency` | requisition |
| `cost.amount` | 6000 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/gr-8-recoilless-rifle.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/GR-8_Recoilless_Rifle
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

