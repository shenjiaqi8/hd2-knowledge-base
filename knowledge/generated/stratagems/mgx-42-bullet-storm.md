---
id: "mgx-42-bullet-storm"
name: "MGX-42 Bullet Storm"
collection: "stratagems"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated", "broken_file_links"]
wiki_url: "https://helldivers.wiki.gg/wiki/MGX-42_Bullet_Storm"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/stratagems/mgx-42-bullet-storm.json"
---

# MGX-42 Bullet Storm

**分类：** 战略配备 (`stratagems`) · **ID：** `mgx-42-bullet-storm`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/MGX-42_Bullet_Storm

## 简介

The MGX-42 Bullet Storm is a Stratagem which calls down a pair of disposable Support Weapons, specializing in disposing of large quantities of lightly armored targets.

## 主要属性

| 字段 | 数值 |
|---|---|
| `permitType` | supply |
| `availability` | loadout |
| 类型 (`kind`) | support_weapon |
| 特性 ID (`traitIds`) | support-weapon, light-armor-penetrating, expendable |
| 输入指令 (`code`) | down, left, down, right, up, left |
| 冷却时间（秒） (`cooldownS`) | 70 |
| `cooldownVariants\[1\].label` | With Morale Augmentation |
| `cooldownVariants\[1\].seconds` | 66.5 |
| 呼叫时间（秒） (`callInTimeS`) | 6.75 |
| `callInTimeUpgradedS` | 3.75 |
| 使用次数 (`uses`) | unlimited |
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

### 1. MGX-42 P（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 100 |
| `damage.durable` | 25 |
| `damage.type` | Ballistic |
| `penetration.direct` | light |
| `penetration.slightAngle` | light |
| `penetration.largeAngle` | light |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | — |
| `projectile.massG` | 4.5 |
| `projectile.initialVelocityMps` | 450 |
| `projectile.dragFactorPct` | 60 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 10 |
| `forces.stagger` | 20 |
| `forces.push` | 10 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | warbond |
| `label` | Exo Experts P1 |
| 战争债券 ID (`warbondId`) | exo-experts |
| `page` | 1 |
| `cost.currency` | medals |
| `cost.amount` | 75 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/stratagems/mgx-42-bullet-storm.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/MGX-42_Bullet_Storm
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

