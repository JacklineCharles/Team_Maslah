class Trackapp():
	appdata={}
	def get_user_info(self,name):
		self.name=name
		self.appdata[name]={"all":[], "done":[]}

	def add_user_skill(self, skill):
		self.appdata[self.name]["all"].append(skill)

	def get_skills(self):
		return self.appdata[self.name]["all"]

	def add_tracked_skill(self, skill):
		self.appdata[self.name]["done"].append(skill)

	def tracked_skills(self):
		return self.appdata[self.name]["done"]

	def untracked_skills(self):
		untracked=[]
		all = self.appdata[self.name]["all"]
		done = self.appdata[self.name]["done"]
		for skill in all:
			if skill not in done:
				untracked.append(skill)
		return untracked				

	
	def view_learning_progress(self):
		return len(self.appdata[self.name]["done"])/len(self.appdata[self.name]["all"])

trackapp = Trackapp()
print(
	'''
	1. add user
	2. edit user
	'''
)
choice = input("Choose an option: ")
if choice == "1":
	name = input("Enter your name: ")
	trackapp.get_user_info(name)
elif choice == "2":
	pass

while True:
	print(
		'''
		1. add skill
		2. get skills
		3. add tracked skill
		4. view tracked skills
		5. view untracked skills
		6. view learning progress
		'''
	)
	choice = input("Choose an option: ")
	if choice == "1":
		skill = input("Enter a skill: ")
		trackapp.add_user_skill(skill)
	elif choice == "2":
		print(trackapp.get_skills())
	elif choice == "3":
		skill = input("Enter a skill: ")
		trackapp.add_tracked_skill(skill)
	elif choice == "4":
		print(trackapp.tracked_skills())
	elif choice == "5":
		print(trackapp.untracked_skills())
	elif choice == "6":
		print(trackapp.view_learning_progress())




