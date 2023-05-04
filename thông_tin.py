from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.fitimage import FitImage
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton,MDFillRoundFlatIconButton ,MDFloatingActionButtonSpeedDial
from kivy.core.window import Window
from kivymd.uix.label import MDLabel
from kivymd.uix.gridlayout import MDGridLayout
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDIconButton
from kivy.uix.scrollview import ScrollView
from kivymd.uix.textfield import MDTextField
from kivymd.uix.textfield import MDTextFieldRect
from kivymd.uix.behaviors.magic_behavior import MagicBehavior
from kivymd.uix.button import MDRaisedButton

from kivymd.uix.selectioncontrol import MDCheckbox
Window.size=(399, 844)

checkboxs = '''
MDFloatLayout : 
    MDCheckbox : 
        # group: "group"
        pos_hint: {"check_x": 0.9,"center_y": 0.327}
        size_hint: 0.1,0.1
        on_active: app.check(*args) 
    MDCheckbox : 
        # group: "group"
        pos_hint: {"check_x": 0.6,"center_y": 0.6}
        size_hint: 0.1 , 0.1
        on_active: app.check1(*args) 
'''
magicbutton = """
MDFloatLayout:
    canvas:
        Color:
            rgba: app.theme_cls.primary_color
    MagicButton: 
        text : " <<<" 
        icon : "step-backward"
        pos_hint: {"center_x":0.05, "center_y":0.975}
        on_release: self.grow()
        size_hint : (0.01, 0.01)
"""    
class MagicButton (MagicBehavior, MDRaisedButton):
    pass
class MainApp(MDApp):
      
    def build(self):
        
        
        self.theme_cls.theme_style = "Light"
        # màu chữ
        self.theme_cls.primary_palette = "Brown"
        # màu nút bấm sau khi nhấn vào
        self.theme_cls.accent_palette = "Lime"


        screen = MDScreen(md_bg_color= [1,1,1,1])
        k1 = MDCard(size_hint=(2 , 0.1),
                       size=(270, 150),
                       pos_hint={"center_x": 0.9, "center_y": 1},
                       padding="16dp",
                       md_bg_color="#DEAC70",
                       line_color=[0,0,0],
                       orientation="vertical")
      
        screen.add_widget(k1)

        MagicButton = Builder.load_string(magicbutton)
        screen.add_widget(MagicButton)
        # return MagicButton

        # icon_back = MDIconButton(icon = "step-backward", 
        #                         pos_hint= {"center_x":0.07, "center_y":0.975},
        #                          )
        # screen.add_widget(icon_back)

        ten = MDLabel(text="Trang thông tin cá nhân",
                    pos_hint={"center_x":0.65, "center_y":0.9745},
		            theme_text_color="Custom",
		            text_color=(0, 0, 0),
                    font_size = "90" ,
                    color = "#DEAC70",
					font_style='H6')
        screen.add_widget(ten) 

        
        k2 = MDCard(size_hint=(0.9 , 0.25),
                       size=(0.9 , 0.25),
                       pos_hint={"center_x": 0.5, "center_y": 0.8},
                       padding="16dp",
                       md_bg_color="#FFE6A7",
                       line_color=[0,0,0],
                       orientation="vertical")
        
        screen.add_widget(k2)

        ten2 = MDLabel(text="Thẻ thành viên nhà Meow Meow",
                    pos_hint={"center_x":0.72, "center_y":0.91},
		            theme_text_color="Custom",
		            text_color=(0, 0, 0),
                    font_size = "90" ,
                    color = "#DEAC70",
					font_style='Subtitle1')
        screen.add_widget(ten2) 

        ten3 = MDLabel(text="Tích lũy càng nhiều, nhận ngay ưu đãi",
                    pos_hint={"center_x":0.72, "center_y":0.89},
		            theme_text_color="Custom",
		            # text_color=(0, 0, 0),
                    
                    text_color = "#CC6600",
					font_style='Body2')
        screen.add_widget(ten3) 

        icon_medal = MDIconButton(icon = "medal-outline", 
                                pos_hint= {"center_x":0.09, "center_y":0.85},
                                 )
        screen.add_widget(icon_medal)

        ten4 = MDLabel(text="TIEN RIEFLE",
                    pos_hint={"center_x":0.63, "center_y":0.85},
		            theme_text_color="Custom",
		            text_color=(0, 0, 0),
                    
    
					font_style='Subtitle1')
        screen.add_widget(ten4) 
        
        icon_trophy = MDIconButton(icon = "trophy-outline", 
                                pos_hint= {"center_x":0.65  , "center_y":0.85},
                                 )
        screen.add_widget(icon_trophy)

        ten5 = MDLabel(text="Thành viên đồng",
                    pos_hint={"center_x":1.2, "center_y":0.85},
		            theme_text_color="Custom",
		            text_color=(0, 0, 0),
                    
    
					font_style='Caption')
        screen.add_widget(ten5) 
 
        ten6 = MDLabel(text="< 0 0 0 1 1 0 9 9 2 4 >",
                    pos_hint={"center_x":0.63 , "center_y":0.83},
		            theme_text_color="Custom",
		            text_color=(0, 0, 0),
                    
    
					font_style='Overline')
        screen.add_widget(ten6) 

        

        k3 = MDCard(size_hint=(0.85, 0.13 ),
                       
                       pos_hint={"center_x": 0.5, "center_y": 0.75},
                       padding="16dp",
                       md_bg_color="#faedcd",
                       line_color=[0,0,0],
                       orientation="vertical")
        
        screen.add_widget(k3)

        ten7 = MDLabel(text="Để nâng cấp thành viên",
                    pos_hint={"center_x":0.615 , "center_y":0.8},
		            theme_text_color="Custom",
		            text_color="red",
					font_style='Subtitle2')
        screen.add_widget(ten7)

        

        ten8 = MDLabel(text="Điểm thưởng",
                    pos_hint={"center_x":0.62 , "center_y":0.78},
		            theme_text_color="Custom",
		            text_color="black",
					font_style='Caption')
        screen.add_widget(ten8)

        ten9 = MDLabel(text="đ700.000",
                    pos_hint={"center_x":0.62 , "center_y":0.76},
		            theme_text_color="Custom",
		            text_color="brown",
					font_style='Caption')
        screen.add_widget(ten9)

        ten10 = MDLabel(text="/1.000.000",
                    pos_hint={"center_x":0.755 , "center_y":0.76},
		            theme_text_color="Custom",
		            text_color="black",
					font_style='Caption')
        screen.add_widget(ten10)

        rank = MDLabel(text="Thứ hạng sẽ được cập nhật sau 30 ngày",
                    pos_hint={"center_x":0.62 , "center_y":0.74},
		            theme_text_color="Custom",
		            text_color="#6c757d",
					font_style='Caption')
        screen.add_widget(rank)

        icon_start = MDIconButton(icon = "emoticon-excited-outline", 
                                pos_hint= {"center_x":0.5  , "center_y":0.705},
                                 )
        screen.add_widget(icon_start)
        icon_start1 = MDIconButton(icon = "emoticon-excited-outline", 
                                pos_hint= {"center_x":0.3  , "center_y":0.705},
                                 )
        screen.add_widget(icon_start1)

        icon_start2 = MDIconButton(icon = "emoticon-excited-outline", 
                                pos_hint= {"center_x":0.7  , "center_y":0.705},
                                 )
        screen.add_widget(icon_start2)

        ten11 = MDLabel(text="Quản lý tài khoản",
                    pos_hint={"center_x":0.55 , "center_y":0.65},
		            theme_text_color="Custom",
		            text_color="black",
					font_style='H6')
        screen.add_widget(ten11)
        

        k4 = MDCard(size_hint=(0.9 , 0.33 ),
                       
                       pos_hint={"center_x": 0.5, "center_y": 0.46},
                       padding="16dp",
                       md_bg_color="#FFE6A7",
                       line_color=[0,0,0],
                       orientation="vertical")
        
        screen.add_widget(k4)

        ten12 = MDLabel(text="Thông tin của tôi",
                    pos_hint={"center_x":0.57 , "center_y":0.6},
		            theme_text_color="Custom",
		            text_color="black",
					font_style='Subtitle1')
        screen.add_widget(ten12)

        icon_plus3 = MDIconButton(icon = "plus-circle-outline", 
                                pos_hint= {"center_x":0.89  , "center_y":0.6},
                                 )
        screen.add_widget(icon_plus3)

        ten111 = MDLabel(text="-------------------------------------------------------------------",
                    pos_hint={"center_x":0.58 , "center_y":0.58},
		            theme_text_color="Custom",
		            text_color="brown",
					font_style='Button')
        screen.add_widget(ten111)

        ten13 = MDLabel(text="Tien Riefle",
                    pos_hint={"center_x":0.57 , "center_y":0.565},
		            theme_text_color="Custom",
		            text_color="black",
					font_style='Body2')
        screen.add_widget(ten13)

        

        ten14 = MDLabel(text="Tien Riefle",
                    pos_hint={"center_x":0.57 , "center_y":0.565},
		            theme_text_color="Custom",
		            text_color="black",
					font_style='Body2')
        screen.add_widget(ten14 )

        
        icon_phone = MDIconButton(icon = "phone-outline", 
                                pos_hint= {"center_x":0.15  , "center_y":0.535},
                                 )
        screen.add_widget(icon_phone)

        phone = MDTextField(text="",
		                background_color = "#FFD581",
                        # line_color =(0.5, 0, 0.5, 1),
                        # hint_text = line_color_normal,
                        # line_color_normal = app.theme_cls.accent_color,
                        pos_hint={
						'center_x': 0.515, 'center_y': 0.54},
						size_hint_x=None, width=240)
        
        screen.add_widget(phone)

        icon_pen1 = MDIconButton(icon = "pencil-outline", 
                                pos_hint= {"center_x":0.85  , "center_y":0.535},
                                 )
        screen.add_widget(icon_pen1)

        icon_cake = MDIconButton(icon = "cake-variant-outline", 
                                pos_hint= {"center_x":0.15  , "center_y":0.5},
                                 )
        screen.add_widget(icon_cake)

        cake = MDTextField(text="",
		                background_color = "#FFD581",
                        # line_color =(0.5, 0, 0.5, 1),
                        # hint_text = line_color_normal,
                        # line_color_normal = app.theme_cls.accent_color,
                        pos_hint={
						'center_x': 0.515, 'center_y': 0.501},
						size_hint_x=None, width=240)
        
        screen.add_widget(cake)


        icon_pen2 = MDIconButton(icon = "pencil-outline", 
                                pos_hint= {"center_x":0.85  , "center_y":0.5},
                                 )
        screen.add_widget(icon_pen2)

        icon_mail = MDIconButton(icon = "email-outline", 
                                pos_hint= {"center_x":0.15  , "center_y":0.465},
                                 )
        screen.add_widget(icon_mail)

        mail = MDTextField(text="",
		                background_color = "#FFD581",
                        # line_color =(0.5, 0, 0.5, 1),
                        # hint_text = line_color_normal,
                        # line_color_normal = app.theme_cls.accent_color,
                        pos_hint={
						'center_x': 0.515, 'center_y': 0.465},
						size_hint_x=None, width=240)
        
        screen.add_widget(mail)

        icon_pen3 = MDIconButton(icon = "pencil-outline", 
                                pos_hint= {"center_x":0.85  , "center_y":0.465},
                                 )
        screen.add_widget(icon_pen3)

        icon_loc = MDIconButton(icon = "crosshairs-gps", 
                                pos_hint= {"center_x":0.15  , "center_y":0.425},
                                 )
        screen.add_widget(icon_loc)

        loc = MDTextField(text="",
		                background_color = "#FFD581",
                        # line_color =(0.5, 0, 0.5, 1),
                        # hint_text = line_color_normal,
                        # line_color_normal = app.theme_cls.accent_color,
                        pos_hint={
						'center_x': 0.515, 'center_y': 0.43},
						size_hint_x=None, width=240)
        
        screen.add_widget(loc)

        icon_pen4 = MDIconButton(icon = "pencil-outline", 
                                pos_hint= {"center_x":0.85  , "center_y":0.43},
                                 )
        screen.add_widget(icon_pen4)

        ten15 = MDLabel(text="-------------------------------------------------------------------",
                    pos_hint={"center_x":0.58 , "center_y":0.37},
		            theme_text_color="Custom",
		            text_color="brown",
					font_style='Button')
        screen.add_widget(ten15)

        ten16 = MDLabel(text="Ngôn ngữ ",
                    pos_hint={"center_x":0.58 , "center_y":0.35},
		            theme_text_color="Custom",
		            text_color="black",
					font_style='Subtitle2')
        screen.add_widget(ten16)

        ten17 = MDLabel(text="Tiếng Việt ",
                    pos_hint={"center_x":0.85 , "center_y":0.35},
		            theme_text_color="Custom",
		            text_color="grey",
					font_style='Subtitle2')
        screen.add_widget(ten17)

        

        checkbox1 = MDCheckbox(size_hint=(None, None),
                              size=("45dp", "45dp"),
                              pos_hint={"x": 0.5, "y": 0.295 } )

        screen.add_widget(checkbox1)

        ten17 = MDLabel(text="Tiếng Anh ",
                    pos_hint={"center_x":0.85 , "center_y":0.325},
		            theme_text_color="Custom",
		            text_color="grey",
					font_style='Subtitle2')
        screen.add_widget(ten17)

        checkbox = MDCheckbox(size_hint=(None, None),
                              size=("45dp", "45dp"),
                              pos_hint={"x": 0.5, "y": 0.325})

        screen.add_widget(checkbox)

        ten18 = MDLabel(text="Khác",
                    pos_hint={"center_x":0.55 , "center_y":0.27},
		            theme_text_color="Custom",
		            text_color="black",
					font_style='H6')
        screen.add_widget(ten18)

        

        k5 = MDCard(size_hint=(0.9 , 0.17 ),
                       
                       pos_hint={"center_x": 0.5, "center_y": 0.16},
                       padding="16dp",
                       md_bg_color="#FFE6A7",
                       line_color=[0,0,0],
                       orientation="vertical")
        
        screen.add_widget(k5)

        ten19 = MDLabel(text="Giới thiệu về Meow Meow Coffee",
                    pos_hint={"center_x":0.58 , "center_y":0.22},
		            theme_text_color="Custom",
		            text_color="black",
					font_style='Body1')
        screen.add_widget(ten19)

        icon_plus1 = MDIconButton(icon = "plus-circle-outline", 
                                pos_hint= {"center_x":0.89  , "center_y":0.22},
                                 )
        screen.add_widget(icon_plus1)

        ten20 = MDLabel(text="-------------------------------------------------------------------",
                    pos_hint={"center_x":0.58 , "center_y":0.20},
		            theme_text_color="Custom",
		            text_color="brown",
					font_style='Button')
        screen.add_widget(ten20)

        ten21 = MDLabel(text="Điều khoản",
                    pos_hint={"center_x":0.58 , "center_y":0.17},
		            theme_text_color="Custom",
		            text_color="black",
					font_style='Body1')
        screen.add_widget(ten21)
        icon_plus2 = MDIconButton(icon = "plus-circle-outline", 
                                pos_hint= {"center_x":0.89  , "center_y":0.17},
                                 )
        screen.add_widget(icon_plus2)

        ten22 = MDLabel(text="-------------------------------------------------------------------",
                    pos_hint={"center_x":0.58 , "center_y":0.15},
		            theme_text_color="Custom",
		            text_color="brown",
					font_style='Button')
        screen.add_widget(ten22)

        ten23 = MDLabel(text="Liên hệ chúng tôi",
                    pos_hint={"center_x":0.58 , "center_y":0.12},
		            theme_text_color="Custom",
		            text_color="black",
					font_style='Body1')
        screen.add_widget(ten23)

        icon_plus4 = MDIconButton(icon = "plus-circle-outline", 
                                pos_hint= {"center_x":0.89  , "center_y":0.12},
                                 )
        screen.add_widget(icon_plus4)

        ten24 = MDLabel(text="-------------------------------------------------------------------",
                    pos_hint={"center_x":0.58 , "center_y":0.1},
		            theme_text_color="Custom",
		            text_color="brown",
					font_style='Button')
        screen.add_widget(ten24)


        btn6 = MDFillRoundFlatIconButton(
                text="Đăng xuất  ",
                text_color= "black" , 
                font_style = 'H6',
                md_bg_color = "#DEAC70", 
                pos_hint={"center_x": 0.5, "center_y": 0.03},
                line_color = (0,0,0),
                size_hint = (0.7 , 0.04)   
            )
        screen.add_widget(btn6)

        

        return screen

        
        
        


MainApp().run()