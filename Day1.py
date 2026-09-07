'''
email_id="saketh@codegnan.com"
print(email_id[7:15])

email_id=["saketh@codegnan.com","lokeshwar25112004@gmail.com",
          "lokiloki25112004@gmail.com","lokiroxx@gmail.com"]
#print(email_id[-2:-1])
a=["abc@gmail.com","bcd@gmail.com","efg@gmail.com"]
email_id.extend(["abc@gmail.com","bcd@gmail.com","efg@gmail.com"])
#print(email_id)
users={}
for i in range(len(email_id)):
    users.update({i:email_id[i]})
print(users)
'''
email_id=["saketh@codegnan.com","lokeshwar25112004@gmail.com",
          "lokiloki25112004@gmail.com","lokiroxx@gmail.com"]
users=dict(enumerate(email_id,1))
print(users)
