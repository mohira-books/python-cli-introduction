# その5: p05_実際のCLIに触れてみよう

## GitHub CLI
- [Manual | GitHub CLI](https://cli.github.com/manual/)
- [cli/cli: GitHub’s official command line tool](https://github.com/cli/cli)

### 例
GitHub上にリモートリポジトリを作成し、ブラウザで開く。

```
$ mkdir sample-project
$ cd sample-project
$ echo hello > README.md
$ git init
$ git add README.md
$ git commit -m 'First commit'
[main (root-commit) eaf0e2f] First commit
 1 file changed, 1 insertion(+)
 create mode 100644 README.md
```

```
$ gh repo create
? Repository name sample-project
? Repository description
? Visibility Public
? This will create 'sample-project' in your current directory. Continue?  Yes
✓ Created repository mohira/sample-project on GitHub
✓ Added remote git@github.com:mohira/sample-project.git
```

```
$ git push -u origin main
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 216 bytes | 216.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To github.com:mohira/sample-project.git
 * [new branch]      main -> main
 
$ gh repo view  -w
Opening github.com/mohira/sample-project in your browser.
```

## AWS CLI
- [AWS コマンドラインインターフェイス（CLI: AWSサービスを管理する統合ツール）| AWS](https://aws.amazon.com/jp/cli/)


```
# 演習時の誤爆回避用
$ export AWS_DEFAULT_PROFILE=mohirasub
```

```
$ aws iam create-user --user-name=Bob
{
    "User": {
        "Path": "/",
        "UserName": "Bob",
        "UserId": "AIDA4UWTJLZHXIN4Z3DMV",
        "Arn": "arn:aws:iam::869100248655:user/Bob",
        "CreateDate": "2020-12-14T06:40:37+00:00"
    }
}
```

```
$ aws iam list-users
{
    "Users": [
        {
            "Path": "/",
            "UserName": "Administrator",
            "UserId": "AIDA4UWTJLZHYTE37LWW7",
            "Arn": "arn:aws:iam::869100248655:user/Administrator",
            "CreateDate": "2020-12-08T12:12:50+00:00",
            "PasswordLastUsed": "2020-12-14T06:34:14+00:00"
        },
        {
            "Path": "/",
            "UserName": "Bob",
            "UserId": "AIDA4UWTJLZHXIN4Z3DMV",
            "Arn": "arn:aws:iam::869100248655:user/Bob",
            "CreateDate": "2020-12-14T06:40:37+00:00"
        }
    ]
}
```

```
$ aws iam delete-user --user-name=Bob
```

```
$ aws iam list-users
{
    "Users": [
        {
            "Path": "/",
            "UserName": "Administrator",
            "UserId": "AIDA4UWTJLZHYTE37LWW7",
            "Arn": "arn:aws:iam::869100248655:user/Administrator",
            "CreateDate": "2020-12-08T12:12:50+00:00",
            "PasswordLastUsed": "2020-12-14T06:34:14+00:00"
        }
    ]
}
```