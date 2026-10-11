# Career Gap Navigator

**快速入门：** [两种简单使用方法（英文／中文／芬兰语）](QUICKSTART.md)。


**阅读语言：** [English](README.md) | [简体中文](README.zh-CN.md) | [Suomi](README.fi.md)

**一个以证据为基础的职业与发展机会分析工具，可作为 GitHub Agent Skill 使用，也可直接作为聊天提示词使用。**

Career Gap Navigator 帮助不同职业背景的使用者，将个人简历与**来源可追溯的真实职业机会**进行比较，区分已经证明的能力、简历中尚未说明的经历，以及真正值得学习或积累的技能。工具会提出针对性的核实问题，并在收到回答后给出适当的培训选择和个人 **30/60/90 天发展计划**。

> **当前为试用阶段。** 在同一候选人的不同 CV 版本上进行的小规模对照测试表明，分类规则调整后的一致性有所改善。这**不能证明分类准确率**，也不能证明对所有职业普遍适用。包括研究资助机会与课程推荐在内的完整流程，尚未经过大范围真实用户验证。

## 两种使用方式

**方式一：Agent Skill。** 仓库包含 `.github/skills/career-gap-navigator/SKILL.md` 及相关参考规则。可在支持 Agent Skills 的 AI 工具中使用，例如兼容的 GitHub Copilot 环境。是否自动启用由具体代理环境决定。**仅将仓库上传 GitHub，并不意味着该 Skill 会自动安装到 ChatGPT。** 参见 [GitHub 官方说明](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills)及 [Agent Skills 规范](https://agentskills.io/specification)。

**方式二：独立聊天提示词。** 打开 [`Career Gap Navigator.txt`](Career%20Gap%20Navigator.txt)，在新的聊天中上传已删除不必要个人信息的 CV，然后完整粘贴提示词。该文件**逐字保留**提供给项目的最新提示词，是此 Skill 所遵循的核心规则来源。无需额外的测试提示词或固定职位资料。

## 使用者需要提供什么？

| 必需信息（仅在缺少时询问） | 说明 |
|---|---|
| `CV` | 当前简历，建议匿名化；也可以提供较完整的简历文字 |
| `Target occupation` | 使用者自行选择的目标职业或职业发展方向 |
| `Preferred location` | 目标国家／地区及远程工作范围；涉及资助申请时还应明确相关机构或项目的所在地 |
| `Target level` | 初级／中级／高级／转行者／不确定（entry-level / mid-level / senior / career changer / unsure） |

**可以联网时，使用者不必自行提供招聘广告或项目征集通知。** AI 会按确认的目标主动搜索真实来源。如果无法联网，且没有可读取的真实来源，系统才会要求提供一份实际招聘广告或项目通知，然后等待使用者回复。每周学习时间、预算、语言能力与线上／线下课程偏好均为可选信息。

## 可以分析哪些机会？

默认分析**就业招聘职位**。只有当使用者明确提出时，才加入博士后或其他研究职位的资助项目、研究基金、奖学金以及其他计划。每种机会分别判断其**硬性申请资格**和**竞争性评选标准**；**基金征集通知不等于招聘广告**。系统不会因为 CV 中存在某个关键词，就替使用者选定职业或擅自增加基金申请方向。

## 两阶段工作流程

```text
使用者 CV + 明确选择的职业方向、地点和岗位级别
                      ↓
搜索真实机会（核实来源、日期和开放状态）
                      ↓
初步证据审核（每项要求对应一个 R-ID 和一个分类）
                      ↓
提出 3–5 个关键问题，每题核实一项明确事实
                  停止并等待
                      ↓
使用者回答（未经独立证明的回答标为 SELF-REPORTED）
                      ↓
Change Log：记录分类变化及有理由的不变项
+ 更新最初每个 R-ID 的完整审核结果
                      ↓
最多 3 项优先行动；仅在适当时推荐可核实的课程
                      ↓
30/60/90 天计划 + 未来 3–12 个月方向 + 未来 7 天行动
```

六种分类名称在所有语言中**保持原样**：`ELIGIBILITY_BARRIER`、`STRENGTH`、`CONFIRMED_SKILL_GAP`、`CV_EVIDENCE_GAP`、`POTENTIAL_EXPERIENCE_GAP`、`UNKNOWN`。

**简历没有写某项技能，不代表使用者缺少该技能。** 使用中文、芬兰语或英语交流时，分析依据、解释深度和不确定性处理应保持一致。

## 仓库主要文件

```text
.github/skills/career-gap-navigator/
    SKILL.md
    references/
      opportunity-sourcing.md
      evidence-rules.md
      verification-and-changelog.md
      learning-and-roadmap.md
      output-templates.md
Career Gap Navigator.txt         # 完整独立提示词，保留最新原文
README.md                        # English
README.zh-CN.md                  # 简体中文
README.fi.md                     # Suomi
.github/workflows/validate.yml  # 自动结构与规则检查
examples/acceptance-tests.md    # 人工行为测试方案
examples/fictional-session.md   # 虚构且不含个人身份的示例
examples/source-coverage.md     # 提示词规则与 Skill 的对应关系
examples/CHANGELOG.md           # 修改记录
scripts/check_policy_sync.py    # 规则一致性检查（不联网）
scripts/validate_privacy.py      # 基本公开分享隐私检查
tests/test_skill_structure.py
...
```

## 在本地运行检查

在仓库根目录运行：

```bash
python tests/test_skill_structure.py
python scripts/check_policy_sync.py
python scripts/validate_privacy.py
```

这些脚本检查项目结构、重要规则是否存在、提示词与模块的对应情况，以及基础隐私风险。**它们不能证明 AI 必然遵守规则，也不能证明某门课程真实开班或职业建议一定改善就业结果。** 应按[人工验收测试方案](examples/acceptance-tests.md)，在互相隔离的新对话中使用虚构数据或获得授权的数据进行测试。

## 隐私与负责任使用

- **不要将真实使用者的 CV、原始问答、姓名、联系方式、基金申请书、保密项目材料或雇主数据提交到公开仓库。**
- `examples/` 仅使用虚构示例；实时搜索前应删除不必要的个人标识。
- 除非有独立佐证，否则使用者的补充陈述始终标注为 `SELF-REPORTED`。
- 不要编造岗位开放状态、资助资格、课程费用或申请成功概率。本工具提供职业发展指导，**不替代正式职业资格认定、法律建议或雇主／资助机构的决定**。

## 开发方法与复制使用

参见 [Development Guide](docs/Development%20Guide.md) 了解保护隐私的通用提示词开发方法；参见 [GitHub 发布说明](docs/Publish%20to%20GitHub.md) 了解仓库发布流程。**这两份扩展文档目前为英文。**

## 许可证

本项目采用 **MIT 许可证**发布。完整条款请参阅项目根目录的 [`LICENSE`](LICENSE) 文件。允许使用、修改与再分发，但须按照许可证要求保留版权和许可声明。
