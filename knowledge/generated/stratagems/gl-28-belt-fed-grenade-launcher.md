---
id: "gl-28-belt-fed-grenade-launcher"
name: "GL-28 Belt-Fed Grenade Launcher"
collection: "stratagems"
aliases: ["BFGL"]
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/GL-28_Belt-Fed_Grenade_Launcher"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/gl-28-belt-fed-grenade-launcher.json"
---

# GL-28 Belt-Fed Grenade Launcher

**分类：** 战略配备 (`stratagems`) · **ID：** `gl-28-belt-fed-grenade-launcher`

**别名：** BFGL

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/GL-28_Belt-Fed_Grenade_Launcher

## 简介

The GL-28 Belt-Fed Grenade Launcher (BFGL) is a Stratagem that calls down a Support Weapon consisting of a belt-fed grenade launcher and ammo backpack. It can fire continuously without the need to reload.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | supply |
| `availability` | loadout |
| 类型 (`kind`) | support_weapon |
| 特性 ID (`traitIds`) | support-weapon, backpack, heavy-armor-penetrating, explosive |
| 输入指令 (`code`) | down, left, up, left, up, up |
| 冷却时间（秒） (`cooldownS`) | 480 |
| `cooldownVariants\[1\].label` | With Morale Augmentation |
| `cooldownVariants\[1\].seconds` | 456 |
| 呼叫时间（秒） (`callInTimeS`) | 7.75 |
| `callInTimeUpgradedS` | 4.75 |
| 使用次数 (`uses`) | unlimited |
| `shipModules\[1\].department` | patriotic_administration_center |
| `shipModules\[1\].module` | Streamlined Request Process |
| `shipModules\[1\].effect` | Decreases Support Weapon stratagem cooldown by 10%. |
| `shipModules\[2\].department` | patriotic_administration_center |
| `shipModules\[2\].module` | Superior Packing Methodology |
| `shipModules\[2\].effect` | Resupply stratagem boxes refill Support Weapons with the maximum number of carriable magazines. |
| `shipModules\[3\].department` | bridge |
| `shipModules\[3\].module` | Morale Augmentation |
| `shipModules\[3\].effect` | Reduces cooldown time for all stratagems by 5%. |
| `shipModules\[4\].department` | engineering_bay |
| `shipModules\[4\].module` | Streamlined Launch Process |
| `shipModules\[4\].effect` | All Support Weapon stratagems launch immediately once called in, reducing overall deployment time. |


## 攻击模式、伤害与穿甲

### 1. GL-28 P（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 0 |
| `damage.durable` | 0 |
| `damage.type` | Ballistic |
| `penetration.direct` | heavy |
| `penetration.slightAngle` | heavy |
| `penetration.largeAngle` | heavy |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | — |
| `projectile.massG` | 50 |
| `projectile.initialVelocityMps` | 100 |
| `projectile.dragFactorPct` | 120 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 10 |
| `forces.stagger` | 30 |
| `forces.push` | 10 |


### 2. GL-28 P IE（explosion）

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
| `area.innerRadiusM` | 2 |
| `area.outerRadiusM` | 4 |
| `area.shockwaveRadiusM` | 5.5 |
| `forces.demolition` | 30 |
| `forces.stagger` | 20 |
| `forces.push` | 20 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | warbond |
| `label` | Siege Breakers P3 |
| 战争债券 ID (`warbondId`) | siege-breakers |
| `page` | 3 |
| `cost.currency` | medals |
| `cost.amount` | 110 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/gl-28-belt-fed-grenade-launcher.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/GL-28_Belt-Fed_Grenade_Launcher
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

