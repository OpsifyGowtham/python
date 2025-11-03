#list -> data structure which can hold multiple values of mutliple types
#array -> data structure which can hold multiple values of same type
list_of_cloud = ["aws", "gcp", "azure", "digitalocean", "utho", "alibaba", "oracle"]

print(list_of_cloud)

#add a new cloud Salesforce

list_of_cloud.append("salesforce")

#add a new cloud IBM

list_of_cloud.append("ibm")  #adds at the end of the list

print("Updated list of clouds:", list_of_cloud)

list_of_cloud.insert(2, "Heroku") #inserts at index 2

print("After inserting Heroku at index 2:", list_of_cloud)

print(len(list_of_cloud)) #length of the list

#insert "Hello CLoud" at index 0
list_of_cloud.insert(0, "Hello Cloud")  

print("After inserting Hello Cloud at index 0:", list_of_cloud)

#Iterartion of a List
for cloud in list_of_cloud:
    print(cloud) 
    
for i in range(1,11): #1 to 10
    print(i)