## Scrapy Github Dir
根据目录来爬取github仓库的文件

![scrapy](scrapy.gif)



![result](result.png)

#### 运行

```bash
git clone https://github.com/ditclear/scrapy_github_dir.git
cd scrapy_github_dir
scrapy crawl app -a url= GITHUB_DIR_PATH
## example:scrapy crawl app -a url=https://github.com/ditclear/scrapy_github_dir/tree/master/scrapy_github_dir
```



#### License

[MIT](LiCENSE)