from flet import *
import time
import threading
def main(page: Page):
    page.window.height=700
    page.window.width=400
    page.bgcolor=colors.BLUE
    def getTime():
        return (str(stoptime[0]) if len(str(stoptime[0]))>1 else '0'+str(stoptime[0]))+":"+(str(stoptime[1]) if len(str(stoptime[1]))>1 else '0'+str(stoptime[1]))+":"+(str(stoptime[2]) if len(str(stoptime[2]))>1 else '0'+str(stoptime[2]))
    def addsecond():
        stoptime[2]+=1
        if stoptime[2]==60:
            stoptime[1]+=1
        if stoptime[1]==60:
            stoptime[0]+=1
    def start():
        global running
        if running==False:
            running=True
    def stop():
        global running 
        if running==True:
            running=False
    def reset():
        global running
        if running==True:
            stop()
        global stoptime
        stoptime=[0,0,0]
        page.update()
    def infii():
        global running
        while(1):
            time.sleep(1)
            if running:
                addsecond()
            print(stoptime)
            stoptext.value=getTime()
            page.update()
    global stoptime
    stoptime = [0,0,0] 
    stoptext = Text(value=getTime(),size=50)
    global running
    running=False
    thread1 = threading.Thread(target=infii)
    thread1.daemon=True
    thread1.start()
    container = Container(
        width=380,
        height=650,
        bgcolor=colors.WHITE,
        border_radius=border_radius.all(25),
        content=Column(controls=[
            Container(
                height=500,
                width=350,
                margin=margin.all(10),
                alignment=alignment.center,
                content=stoptext
                
            ),
            Row(controls=[
                ElevatedButton(content=Text('Start'),height=100,width=120,on_click=lambda _:start()),
                ElevatedButton(content=Text('Stop'),height=100,width=120,on_click=lambda _:stop()),
                ElevatedButton(content=Text('Reset'),height=100,width=120,on_click=lambda _:reset())
            ],alignment=MainAxisAlignment.SPACE_BETWEEN)

        ])
    )
    page.add(container)
app(target=main)