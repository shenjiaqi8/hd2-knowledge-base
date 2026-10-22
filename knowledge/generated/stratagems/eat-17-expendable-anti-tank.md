---
id: "eat-17-expendable-anti-tank"
name: "EAT-17 Expendable Anti-Tank"
collection: "stratagems"
aliases: ["EAT"]
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/EAT-17_Expendable_Anti-Tank"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/eat-17-expendable-anti-tank.json"
---

# EAT-17 Expendable Anti-Tank

**分类：** 战略配备 (`stratagems`) · **ID：** `eat-17-expendable-anti-tank`

**别名：** EAT

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/EAT-17_Expendable_Anti-Tank

## 简介

The EAT-17 Expendable Anti-Tank (abbreviated as EAT) is a Stratagem that calls down a pair of disposable anti-tank Support Weapons.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | supply |
| `availability` | loadout |
| 类别 (`category`) | patriotic_administration_center |
| 类型 (`kind`) | support_weapon |
| 特性 ID (`traitIds`) | support-weapon, anti-tank, expendable |
| 输入指令 (`code`) | down, down, left, up, right |
| 冷却时间（秒） (`cooldownS`) | 70 |
| `cooldownVariants\[1\].label` | With Morale Augmentation |
| `cooldownVariants\[1\].seconds` | 66.5 |
| 呼叫时间（秒） (`callInTimeS`) | 6.75 |
| `callInTimeUpgradedS` | 3.75 |
| 使用次数 (`uses`) | unlimited |
| `unlockLevel` | 3 |
| `shipModules\[1\].department` | patriotic_administration_center |
| `shipModules\[1\].module` | Streamlined Request Process |
| `shipModules\[1\].effect` | Decreases Support Weapon stratagem cooldown by 10%. |
| `shipModules\[2\].department` | bridge |
| `shipModules\[2\].module` | Morale Augmentation |
| `shipModules\[2\].effect` | Reduces cooldown time for all Stratagems by 5%. |
| `shipModules\[3\].department` | engineering_bay |
| `shipModules\[3\].module` | Streamlined Launch Process |
| `shipModules\[3\].effect` | All Support Weapon stratagems launch immediately once called in, reducing overall deployment time. |


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


### 2. EAT-17 P（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 2000 |
| `damage.durable` | 2000 |
| `damage.type` | Ballistic |
| `penetration.direct` | anti_tank_ii |
| `penetration.slightAngle` | anti_tank_ii |
| `penetration.largeAngle` | anti_tank_ii |
| `penetration.extremeAngle` | medium |
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


### 3. EAT-17 P IE（explosion）

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
| `cost.amount` | 3000 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/eat-17-expendable-anti-tank.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/EAT-17_Expendable_Anti-Tank
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

