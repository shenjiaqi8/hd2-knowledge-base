---
id: "ms-11-solo-silo"
name: "MS-11 Solo Silo"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/MS-11_Solo_Silo"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/ms-11-solo-silo.json"
---

# MS-11 Solo Silo

**分类：** 战略配备 (`stratagems`) · **ID：** `ms-11-solo-silo`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/MS-11_Solo_Silo

## 简介

The MS-11 Solo Silo, shortened to Solo Silo or MS-11, is an expendable Support weapon that embeds itself into the ground, extends a targeting system to be picked up, and launches the embedded missile when used.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | supply |
| `availability` | loadout |
| 类型 (`kind`) | support_weapon |
| 特性 ID (`traitIds`) | support-weapon, explosive, anti-tank, expendable |
| 输入指令 (`code`) | down, up, right, down, down |
| 冷却时间（秒） (`cooldownS`) | 180 |
| `cooldownVariants\[1\].label` | With Morale Augmentation |
| `cooldownVariants\[1\].seconds` | 171 |
| 呼叫时间（秒） (`callInTimeS`) | 7.75 |
| `callInTimeUpgradedS` | 4.75 |
| 使用次数 (`uses`) | unlimited |
| `shipModules\[1\].department` | patriotic_administration_center |
| `shipModules\[1\].module` | Streamlined Request Process |
| `shipModules\[1\].effect` | Decreases Support Weapon stratagem cooldown by 10%. |
| `shipModules\[2\].department` | bridge |
| `shipModules\[2\].module` | Morale Augmentation |
| `shipModules\[2\].effect` | Reduces cooldown time for all stratagems by 5%. |
| `shipModules\[3\].department` | engineering_bay |
| `shipModules\[3\].module` | Streamlined Launch Process |
| `shipModules\[3\].effect` | All Support Weapon stratagems launch immediately once called in, reducing overall deployment time. |


## 攻击模式、伤害与穿甲

### 1. SOLO SILO E（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 2500 |
| `damage.durable` | 2500 |
| `damage.type` | Explosion |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 10 |
| `area.outerRadiusM` | 25 |
| `area.shockwaveRadiusM` | 35 |
| `forces.demolition` | 40 |
| `forces.stagger` | 100 |
| `forces.push` | 40 |


### 2. SOLO SILO EImpact（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 1500 |
| `damage.durable` | 1500 |
| `damage.type` | Explosion |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 3 |
| `area.outerRadiusM` | 6 |
| `area.shockwaveRadiusM` | 6 |
| `forces.demolition` | 40 |
| `forces.stagger` | 100 |
| `forces.push` | 40 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | warbond |
| `label` | Dust Devils P3 |
| 战争债券 ID (`warbondId`) | dust-devils |
| `page` | 3 |
| `cost.currency` | medals |
| `cost.amount` | 110 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/ms-11-solo-silo.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/MS-11_Solo_Silo
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

