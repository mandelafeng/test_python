import redis

r = redis.Redis(host='localhost', port=6379, db=0, password=123456)

def increment_counter(key):
    r.incr(key)

def get_counter(key):
    return int(r.get(key))

# 假设我们要统计一个文章的访问次数
article_id = 'article:1'
increment_counter(article_id)
print(f"Article {article_id} has been viewed {get_counter(article_id)} times.")