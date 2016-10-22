
Skip to content
This repository

    Pull requests
    Issues
    Gist

    @hyhlinux

3
0

    0

Storm-dj/test
Code
Issues 0
Pull requests 0
Projects 0
Wiki
Pulse
Graphs
Settings
test/gitconfig.py
fed1f8d 22 hours ago
@hyhlinux hyhlinux [test][git][config]add git config
46 lines (37 sloc) 1.02 KB
#coding:utf-8
import os

user_config = {
    "email":'2285020853@qq.com', 
    "name":'hyhlinux',
    "template":'.git_template.txt'
}

cmd = [
"git config --global alias.co checkout",
"git config --global alias.ci commit",
"git config --global alias.st status",
"git config --global alias.br branch",
"git config --global core.editor  vim"
]

def gitCmd():
    for c in cmd:
        os.system(c)
        
def gitTemplate():
    proj_git = os.path.abspath('.')
    template_name = os.path.join(proj_git, user_config['template'])
    # print template_name
    os.system("git config --global commit.template {}".format(template_name))

def userConfig():
    os.system("git config --global user.email '{}' ".format(user_config['email']))
    os.system("git config --global user.name '{}' ".format(user_config['name']))

def gitConfigCheck():
    os.system('git config --list')
    pass

def main():
    gitCmd()
    userConfig()
    gitTemplate()
    gitConfigCheck()

if __name__ == '__main__':
    print('*'*10)
    main()
    print('*'*10)

    Contact GitHub API Training Shop Blog About 

    © 2016 GitHub, Inc. Terms Privacy Security Status Help 

