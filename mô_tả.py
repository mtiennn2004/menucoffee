from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.fitimage import FitImage
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton,MDFillRoundFlatIconButton 
from kivy.core.window import Window
from kivymd.uix.label import MDLabel
from kivymd.uix.gridlayout import MDGridLayout
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDIconButton
from kivy.uix.scrollview import ScrollView
from kivymd.uix.textfield import MDTextField
from kivymd.uix.textfield import MDTextFieldRect

Window.size=(399, 844)
   


class MainApp(MDApp):
    
    
    def build(self):
        
        # 
        self.theme_cls.theme_style = "Light"
        # màu chữ
        self.theme_cls.primary_palette = "Brown"
        # màu nút bấm sau khi nhấn vào
        self.theme_cls.accent_palette = "Lime"

        
        
        screen = MDScreen(md_bg_color= [1,1,1,1])
        
        

        logo = MDCard(FitImage(source="1234.jpg",
                        size_hint_y=1.2,
                        size_hint_x=1.2,
                       
                        pos_hint={"center_x": 0.5, "center_y": 0.454},
        ))
        screen.add_widget(logo)
        
        k2 = MDCard(size_hint=(2 , 0.2),
                       size=(0.9 , 0.25),
                       pos_hint={"center_x": 0.9, "center_y": 1},
                       padding="16dp",
                       md_bg_color="#DEAC70",
                       line_color=[0,0,0],
                       orientation="vertical")
        
        screen.add_widget(k2)

        

        btn_mota = MDFillRoundFlatIconButton(
                text="Mô tả   ",
                font_style = 'H6',
                md_bg_color = "#DEAC70", 
                pos_hint={"center_x": 0.5, "center_y": 0.43},
                line_color = (0,0,0,0),
                size_hint = (0.5 , 0.05)   
            )
        screen.add_widget(btn_mota)

        ten = MDLabel(text="Trà Thạch Đào - 45.000 VNĐ",
                    pos_hint={"center_x":0.6, "center_y":0.5},
		            theme_text_color="Custom",
		            text_color=(0, 0, 0),
                    font_size = "100" ,
                    color = "#DEAC70",
					font_style='H5')
        screen.add_widget(ten) 

        mota1 = MDLabel(text="Với hương thơm dịu nhẹ của trà, kết hợp với vị \nngọt dịu của hạt sen, món trà sen vàng mang \nlại cảm giác thư giãn và sảng khoái cho người\nthưởng thức.",
                    pos_hint={"center_x":0.6, "center_y":0.33},
		            theme_text_color="Custom",
                    # halign = "center",
                    # valign = "center",
		            text_color=(0, 0, 0),
                    font_size = "100" ,
                    color = "#DEAC70",
					font_style='Subtitle1')
        screen.add_widget(mota1)

        icon_cart = MDIconButton(icon = "cart", 
                                pos_hint= {"center_x":0.933, "center_y":0.973} )
        screen.add_widget(icon_cart)

        
        btn_1 = MDRectangleFlatButton(
                text="Tất cả",
                font_style = 'Button',
                text_color = "black",
                md_bg_color = "#DEAC70", 
                pos_hint={"center_x": 0.13, "center_y": 0.925},
                line_color = (0,0,0,0),
                size_hint = (0.19 , 0.05 )   
            )
        screen.add_widget(btn_1)
        
       

        btn_2 = MDRectangleFlatButton(
                text="Siêu Sales",
                font_style = 'Button',
                text_color = "black",
                md_bg_color = "#DEAC70", 
                pos_hint={"center_x": 0.37, "center_y": 0.925},
                line_color = (0,0,0,0),
                size_hint = (0.19 , 0.05 )   
            )
        screen.add_widget(btn_2)

        

        btn_3 = MDRectangleFlatButton(
                text="Yêu thích",
                font_style = 'Button',
                text_color = "black",
                md_bg_color = "#DEAC70", 
                pos_hint={"center_x": 0.61, "center_y": 0.925},
                line_color = (0,0,0,0),
                size_hint = (0.19 , 0.05 )   
            )
        screen.add_widget(btn_3)

        

        btn_4 = MDRectangleFlatButton(
                text="Bán chạy",
                text_color = "black",
                font_style = 'Button',
                md_bg_color = "#DEAC70", 
                pos_hint={"center_x": 0.85, "center_y": 0.925},
                line_color = (0,0,0,0),
                size_hint = (0.19 , 0.05 )   
            )
        screen.add_widget(btn_4)

        k3 = MDCard(size_hint=(1 , 0.07),
                       
                       pos_hint={"center_x": 0.5, "center_y": 0.05},
                       padding="16dp",
                       md_bg_color="#DEAC70",
                       line_color=[0,0,0],
                       orientation="vertical")
        screen.add_widget(k3)
        
        
        icon_home = MDIconButton(icon = "home-outline", 
                                pos_hint= {"center_x":0.2, "center_y":0.05},
                                 )
        screen.add_widget(icon_home)

        icon_mess = MDIconButton(icon = "message-outline", 
                                pos_hint= {"center_x":0.4, "center_y":0.05},
                                 )
        screen.add_widget(icon_mess)

        icon_text = MDIconButton(icon = "clipboard-text-outline", 
                                pos_hint= {"center_x":0.6, "center_y":0.05},
                                 )
        screen.add_widget(icon_text)

        icon_clock = MDIconButton(icon = "clock-edit-outline", 
                                pos_hint= {"center_x":0.8, "center_y":0.05},
                                 )
        screen.add_widget(icon_clock)

        l1 = MDLabel ( text="Số lượng: " , 
                        font_style = "H6",
                        text_color = (0,0,0),
                        pos_hint={"center_x": 0.6, "center_y": 0.23}
                        )
        screen.add_widget(l1)

        slg = MDTextField(text="",
		                background_color = "#FFD581",
                        # line_color =(0.5, 0, 0.5, 1),
                        # hint_text = line_color_normal,
                        # line_color_normal = app.theme_cls.accent_color,
                        pos_hint={
						'center_x': 0.4, 'center_y': 0.23},
						size_hint_x=None, width=40)
        
        screen.add_widget(slg)

        btn6 = MDFillRoundFlatIconButton(
                text="Thêm vào giỏ hàng ",
                text_color= "black" , 
                font_style = 'H6',
                md_bg_color = "#DEAC70", 
                pos_hint={"center_x": 0.5, "center_y": 0.137},
                line_color = (0,0,0,0),
                size_hint = (0.4 , 0.04)   
            )
        screen.add_widget(btn6)

        return screen

        
        
        


MainApp().run()
