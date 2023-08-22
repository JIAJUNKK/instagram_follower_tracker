
class File:
    def __init__(self):
        try:
            self.file = open("followerList.txt", "x")
        except FileExistsError:
            pass

        try:
            self.file = open("followingList.txt", "x")
        except FileExistsError:
            pass

    def writeFollowers(self, followerList):
        self.file = open("followerList.txt", "w")
        for names in followerList:
            self.file.write(names + "\n")
        self.file.close()

    def writeFollowing(self, followingList):
        self.file = open("followingList.txt", "w")
        for names in followingList:
            self.file.write(names + "\n")
        self.file.close()

