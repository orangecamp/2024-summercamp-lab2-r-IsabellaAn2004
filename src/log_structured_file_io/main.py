import os
import json
import argparse

FILE='data/store.kv'

def load_store():
    store={}
    if not os.path.exists(FILE):
        return store#如果为空则返回空字典
    with open(FILE,'r') as f:
        for line in f:
            dic=json.loads(line.strip())
            store.update(dic)
        #逐行读取json文件，将每一行转化为py字典
    return store
def save_store(store):
    with open(FILE,'a') as f:
        #a表示追加在文件后面
        for key,value in store.items():
            #遍历store字典
            json.dump({key:value},f)
            #写入文件
            f.write('\n')
            # 写入一个换行符，使每个键值对占用文件中的单独一行
def main():
    arg_parser = argparse.ArgumentParser(description='Log structured file I/O')
    #创建子解析器
    subparsers = arg_parser.add_subparsers(dest='command',required=True)

    #创建子命令
    set_parser=subparsers.add_parser('set',help='set a value')
    set_parser.add_argument('key',type=str,help='the key to set')
    set_parser.add_argument('value',type=str,help='the value to set')

    get_parser=subparsers.add_parser('get',help='get a value')
    get_parser.add_argument('key',type=str,help='the key to get')

    del_parser=subparsers.add_parser('del',help='delete a key')
    del_parser.add_argument('key',type=str,help='the key to delete')

    # 解析参数
    args=arg_parser.parse_args()

    #加载数据
    store=load_store()

    if args.command=='set':
        store[args.key]=args.value
        save_store({args.key:args.value})
    elif args.command=='get':
        print(store.get(args.key,'Key not found'))
    elif args.command=='del':
        if args.key in store:
            del store[args.key]
            with open(FILE,'w') as f:
                for key,vlaue in store.items:
                    json.dump({key:value},f)
                    f.write('\n')
        else:
            print('Key not found')

    
if __name__ == '__main__':
    main()