class human:
        def __init__(self,name):
            print("Human creation")
            self.name=name
            self.head=self.head()
        def info(self,name):
            print("hello ", name)
            print("I am busy with")
            self.head.talk()
            self.head.brain.think()

        class head:
            def __init__(self):
                print("Head creation")
                self.brain=self.brain()
            def talk(self):
                print("ralking..")

            class brain:
                
                def __init__(self):
                    print("Brain creation")
                def think(self):
                    print("Thinking..")
                    

human=human("Durga")
human.info("durga")
