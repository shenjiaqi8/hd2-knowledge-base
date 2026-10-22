---
id: "eat-700-expendable-napalm"
name: "EAT-700 Expendable Napalm"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated", "broken_file_links"]
wiki_url: "https://helldivers.wiki.gg/wiki/EAT-700_Expendable_Napalm"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/eat-700-expendable-napalm.json"
---

# EAT-700 Expendable Napalm

**分类：** 战略配备 (`stratagems`) · **ID：** `eat-700-expendable-napalm`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/EAT-700_Expendable_Napalm

## 简介

The EAT-700 Expendable Napalm or NEAT for short is a Stratagem that calls down 2 disposable napalm cluster Support Weapons.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | supply |
| `availability` | loadout |
| 类型 (`kind`) | support_weapon |
| 特性 ID (`traitIds`) | support-weapon, incendiary, expendable |
| 输入指令 (`code`) | down, down, left, up, left |
| 冷却时间（秒） (`cooldownS`) | 140 |
| `cooldownVariants\[1\].label` | With Morale Augmentation |
| `cooldownVariants\[1\].seconds` | 133 |
| 呼叫时间（秒） (`callInTimeS`) | 7.75 |
| `callInTimeUpgradedS` | 4.75 |
| 使用次数 (`uses`) | unlimited |
| `shipModules\[1\].department` | patriotic_administration_center |
| `shipModules\[1\].module` | Streamlined Request Process |
| `shipModules\[1\].effect` | Decreases Support Weapon stratagem cooldown by 10%. |
| `shipModules\[2\].department` | bridge |
| `shipModules\[2\].module` | Enhanced Combustion |
| `shipModules\[2\].effect` | Fire damage from Stratagems increased by 25%. |
| `shipModules\[3\].department` | bridge |
| `shipModules\[3\].module` | Morale Augmentation |
| `shipModules\[3\].effect` | Reduces cooldown time for all Stratagems by 5%. |


## 攻击模式、伤害与穿甲

### 1. EAT-17 BACKBLAST E（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 15 |
| `damage.durable` | 15 |
| `damage.type` | Explosion |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 1 |
| `area.outerRadiusM` | 6 |
| `area.shockwaveRadiusM` | 7 |
| `forces.demolition` | 10 |
| `forces.stagger` | 30 |
| `forces.push` | 15 |


### 2. EAT-700 P（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 500 |
| `damage.durable` | 500 |
| `damage.type` | Ballistic |
| `penetration.direct` | medium |
| `penetration.slightAngle` | medium |
| `penetration.largeAngle` | medium |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | — |
| `projectile.massG` | 2500 |
| `projectile.initialVelocityMps` | 200 |
| `projectile.dragFactorPct` | 0 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 85 |
| `area` | — |
| `forces.demolition` | 30 |
| `forces.stagger` | 50 |
| `forces.push` | 25 |


### 3. BurningHeavy（status）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 200 |
| `damage.durable` | 200 |
| `damage.type` | Fire |
| `penetration.direct` | heavy |
| `penetration.slightAngle` | heavy |
| `penetration.largeAngle` | heavy |
| `penetration.extremeAngle` | unarmored |
| `projectile` | — |
| `area` | — |
| `forces.demolition` | 0 |
| `forces.stagger` | 0 |
| `forces.push` | 0 |


### 4. EAT-700 P IE（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 250 |
| `damage.durable` | 250 |
| `damage.type` | Explosion |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 1.60000002 |
| `area.outerRadiusM` | 8 |
| `area.shockwaveRadiusM` | 10 |
| `forces.demolition` | 30 |
| `forces.stagger` | 50 |
| `forces.push` | 40 |


### 5. EAT-700 P1（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 200 |
| `damage.durable` | 200 |
| `damage.type` | Ballistic |
| `penetration.direct` | unarmored |
| `penetration.slightAngle` | unarmored |
| `penetration.largeAngle` | unarmored |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | — |
| `projectile.massG` | 3000 |
| `projectile.initialVelocityMps` | 15 |
| `projectile.dragFactorPct` | 1500 |
| `projectile.gravityFactorPct` | 400 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 30 |
| `forces.stagger` | 50 |
| `forces.push` | 25 |


### 6. EAT-700 P1 IE（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 50 |
| `damage.durable` | 50 |
| `damage.type` | Explosion |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 1.60000002 |
| `area.outerRadiusM` | 5 |
| `area.shockwaveRadiusM` | 5 |
| `forces.demolition` | 30 |
| `forces.stagger` | 50 |
| `forces.push` | 25 |


### 7. Fire（status）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 100 |
| `damage.durable` | 100 |
| `damage.type` | Fire |
| `penetration.direct` | heavy |
| `penetration.slightAngle` | heavy |
| `penetration.largeAngle` | heavy |
| `penetration.extremeAngle` | unarmored |
| `projectile` | — |
| `area` | — |
| `forces.demolition` | 0 |
| `forces.stagger` | 0 |
| `forces.push` | 0 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | warbond |
| `label` | Dust Devils P2 |
| 战争债券 ID (`warbondId`) | dust-devils |
| `page` | 2 |
| `cost.currency` | medals |
| `cost.amount` | 85 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/eat-700-expendable-napalm.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/EAT-700_Expendable_Napalm
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

