---
id: "s-11-speargun"
name: "S-11 Speargun"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/S-11_Speargun"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/s-11-speargun.json"
---

# S-11 Speargun

**分类：** 战略配备 (`stratagems`) · **ID：** `s-11-speargun`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/S-11_Speargun

## 简介

The S-11 Speargun is a Stratagem which calls down a Support Weapon that fires projectiles with extremely high stagger force and explodes into a cloud of gas.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | supply |
| `availability` | loadout |
| 类型 (`kind`) | support_weapon |
| 特性 ID (`traitIds`) | support-weapon, caustic, anti-tank |
| 输入指令 (`code`) | down, right, down, left, up, right |
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
| `shipModules\[4\].effect` | Reduces reload time all support weapons by 10%. |
| `shipModules\[5\].department` | bridge |
| `shipModules\[5\].module` | Morale Augmentation |
| `shipModules\[5\].effect` | Reduces cooldown time for all Stratagems by 5%. |
| `shipModules\[6\].department` | engineering_bay |
| `shipModules\[6\].module` | Streamlined Launch Process |
| `shipModules\[6\].effect` | All Support Weapons launch immediately once called in, reducing overall deployment time. |


## 攻击模式、伤害与穿甲

### 1. S-11 P（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 650 |
| `damage.durable` | 275 |
| `damage.type` | Ballistic |
| `penetration.direct` | anti_tank_i |
| `penetration.slightAngle` | anti_tank_i |
| `penetration.largeAngle` | anti_tank_i |
| `penetration.extremeAngle` | anti_tank_i |
| `projectile.pellets` | — |
| `projectile.massG` | 100 |
| `projectile.initialVelocityMps` | 300 |
| `projectile.dragFactorPct` | 400 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 0 |
| `area` | — |
| `forces.demolition` | 30 |
| `forces.stagger` | 80 |
| `forces.push` | 35 |


### 2. Gas（status）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 25 |
| `damage.durable` | 25 |
| `damage.type` | Gas |
| `penetration.direct` | anti_tank_ii |
| `penetration.slightAngle` | anti_tank_ii |
| `penetration.largeAngle` | anti_tank_ii |
| `penetration.extremeAngle` | unarmored |
| `projectile` | — |
| `area` | — |
| `forces.demolition` | 0 |
| `forces.stagger` | 0 |
| `forces.push` | 0 |


### 3. Gas Confusion（status）

| 字段 | 数值 |
|---|---|
| `damage.standard` | — |
| `damage.durable` | — |
| `damage.type` | — |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area` | — |
| `forces.demolition` | — |
| `forces.stagger` | — |
| `forces.push` | — |


### 4. S-11 P E（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 3 |
| `damage.durable` | 3 |
| `damage.type` | Gas |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 2 |
| `area.outerRadiusM` | 5 |
| `area.shockwaveRadiusM` | 7 |
| `forces.demolition` | 30 |
| `forces.stagger` | 10 |
| `forces.push` | 10 |


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
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/s-11-speargun.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/S-11_Speargun
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

