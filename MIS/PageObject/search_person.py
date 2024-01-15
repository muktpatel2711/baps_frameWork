from MIS.PageObject.login_page_qa import login_mis

class serach_person():
    def serach(self):
        serach = login_mis()
        serach.signin()

if __name__ == '__main__':
    serach = serach_person()
    serach.serach()



