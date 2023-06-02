# InformationSecurity_Homework

dirsearch 工具产生了大量的日志，要过滤这部分日志可以采取以下方法
1. request / response 是分别打印的，可以将 response 中 NOT FOUND 的内容过滤掉，减小审计量
2. dirsearch 的日志是连续的，且按照字母顺序排列，最后一个字母是~，例如ip为26的可以从9088行开始看，前面的都没用