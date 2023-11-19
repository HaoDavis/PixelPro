# Git 使用规范

## commit message 编写规范
格式：**type(scope):subject**
### type
- feat：新功能（feature）
- fix：修补bug
- docs：文档（documentation）
- style：格式（不影响代码运行的改动）
- refactor：重构（既不是新增功能，也不是修改bug的代码改动）
- test：增加测试
- chore：辅助工具的变动
### scope
用于说明 commit 影响的范围，比如数据层、控制层、视图层等等，视项目不同而不同。
### subject
commit 目的的简短描述，不超过50个字符。
- 以动词开头，使用第一人称现在时，比如`change`，而不是`changed`或`changes`
- 第一个字母小写
- 结尾不加句号（`.`）

## branch 规范
- main ：用于管理对外发布版本，一般由 dev 以及 hotfix 分支合并
- dev： 用于作为日常开发汇总
- feat： 新功能的开发，一般以 dev 为基础创建，命名以 feat/ 开头
- hotfix： 用于正式发布之后，出现 bug，需要基于 main 创建一个以 hotfix/ 开头的分支，进行 bug 修补，修补后合并入 dev 或 main
- release： 用于发布正式版本之前测试，测试无误后合并入 main 分支
