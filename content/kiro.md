---
title: "规范驱动 Kiro AI 编程"
keywords:
  - AI
  - Kiro
  - 提问的智慧
  - 提示词工程师
description: ""
created: 2025-11-26 12:47:29
updated: 2025-11-26 15:00:13
---

ChatGPT、Claude、DeepSeek、Gork、Gemini 等等模型轮番使用，IDE 工具也换着尝试 Cline、GitHub Copilot... 幻觉、降智...

爆火的提示词工程师，关于这个，如果「提示词」（文本意义）都需要达到「专业」的地步，那么是不是一定程度上代表着 AI 模型水平不行？或者说还未达到普遍理解中的“智能”水平？提示词？如果说专业，在编程领域，那是不是就是产品和开发团队一直习惯的需求文档、开发设计文档、测试用例文档？还有提问的智慧？

对于 AI 开发，除了“鼓吹”的，有开发者说构造方式没有变；Jake Wharton 的价值观中：No AI（...or forced “AI” usage for development.）；有的开源创作者因合并了 AI 的代码被批...

我的习惯上，聚焦某个功能，简要描述问题（查漏补缺、最佳实践是什么），把问题发送给多个模型，然后看各自的回答。

偶然的机会了解到 Kiro - Kiro helps you do your best work by bringing structure to AI coding with spec-driven development. 这个让我眼前一亮。再本次之前，简单接触过一次，这次趁着新项目的启动，就深入体验下。就是暂停了原计划完善 [FastAPI 构建 API 项目教程](https://chrisding.xyz/posts/tutorial-building-api-projects-with-python-fastapi) 博文和其它新文章的撰写。

## Kiro

Kiro 官网 [kiro.dev](https://kiro.dev/)

总结提炼，就是 Kiro 除了提供常规的 Vibe 方式外。另外还提供一种 Spec 的方式，对于想要实现的功能，创建需求、设计、任务列表文件。

### 目录结构

项目根目录下创建 `.kiro` 目录，目录结构：

```
.kiro/
├── steering/                 # 指导文件目录，无论任何交互方式，都会读取
│   ├── product.md            # 项目产品说明
│   ├── structure.md          # 项目组织方式
│   └── tech.md               # 技术栈。详细说明所使用的技术、框架细节信息
│   └── code-conventions.md   # 代码规范
│   └── ...
├── hooks/                    # Agent 钩子配置目录。可用来运行测试、格式化、创建翻译的字符串国际化，支持多种出发条件
│   ├── lint.json             # 可以定义文件保存时，触发代码格式化命令
│   └── ...
└── specs/                    # 功能规格文档目录，每个功能一个文件夹
    ├── feature-name-1/
    │   ├── requirements.md   # 表述需求和验收标准
    │   ├── design.md         # 设计文档（正确性属性）
    │   └── tasks.md          # 实现任务列表
    └── feature-name-2/
        ├── requirements.md
        ├── design.md
        └── tasks.md
    └── ...
```

#### `steering` 目录

`hooks` 和 `specs` 目录的作用在结构图中很清楚了，这里着重说一下 `steering` 目录：

`steering` 定义的就是项目的基础总纲，并且无论你是用 Vibe 还是 Spec，和 AI 交互时，会优先读取这个目录下的所有文件，作为前置了解，赶时髦的专业词就说保持「上下文」吧。

定义的文件名称，创建多少个文件，看你自己的需求，这个就不多谈了，建议单一职责。

另外，如果项目的根目录下有 `agents.md` 文件，Kiro 交互时也会自动加载。

还要提一下包含模式，也就是在文件内，可以写包含其它文件的语句。包含支持总是包含、条件包含、手动包含。文件引用的写法为：

```md
#[[file:.env.example]]
```

这种结构化的方式让复杂功能的开发变得可控，支持增量开发和迭代反馈。

### 注意

- 记得持续优化、完善创建的文档
- 无论时创建钩子文件、指导文件还是规格文件等，你可以自己手动编写也可以通过与 AI 交互生成，也可以在 Kiro 的 IDE 内的 Kiro 资源面板里面输入文本内容来生成

因项目还未结束，等项目开发完成，我在回头完善此博文。以目前我和 AI 交互的结果来看，质量的规范性上有一些提升。当前槽点的话，感觉钩子的官方文档举例不好。规格开发的结果。还有前后端分离问题。后续整体的统一反馈。
