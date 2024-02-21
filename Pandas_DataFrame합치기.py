# 실습
import pandas as pd
import numpy as np

# 1. data/customer.csv, data/order.csv, data/qna.csv를 DataFrame으로 읽으시오
customer = pd.read_csv('data/customer.csv')
order = pd.read_csv('data/order.csv')
qna = pd.read_csv('data/qna.csv')

# 2. 세개의 데이터셋의 정보를 확인하시오
print(customer)
print(order)
print(qna)

# 3. customer DataFrame과 order DataFrame을 고객정보는 모두 나오도록 join 하세요
print(customer.set_index('id').join(order.set_index('cust_id')))

# 4. customer DataFrame의 index를 id컬럼으로 변경
customer2 = customer.set_index('id')
print(customer2)

# 5. customer DataFrame과 qna DataFrame을 inner join 하세요
print(customer2.join(qna.set_index('cust_id'), how = 'inner'))

# 6. 세개의 DataFrame을 고객정보는 모두 나오도록 join하세요
order2 = order.set_index('cust_id')
qna2 = qna.set_index('cust_id')
print(customer2.join([order2, qna2]))