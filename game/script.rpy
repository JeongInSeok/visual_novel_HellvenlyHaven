
define ch_ins = Character("주인공", color = "#00BFB7")
define ch_yeoul = Character("은여울", color ="#6c11ff")
define ch_reimu = Character("겨드랑이 무녀", color ="#ff2017")
define ch_akua = Character("잉여신", color ="#4286f4")
define ch_nanimono = Character("???", color="#3a00ba")
define ch_nanimono2 = Character("누군가", color = "#115b2e")
define ch_nugu = Character("참철수", color ="#5ef235")
define ch_yuyuko = Character("우리 이쁘신 유유코님", color = "#fc8ff7")
define ch_sense = Character("시발국회의원더럽게일안하네", color ="#2a2d33")
define ch_guzun = Character("구준표", color="#ed006a")
define ch_kim = Character("김정동",color = "#ff1000")
define ch_spring = Character("춘전", color = "#fc9802")
define ch_mercy = Character("정신과 의사 메르시", color ="#f9c507")
define ch_rasis = Character("레이시스", color="db557a")

image bg_myroom = "bg/myroom.png"
image bg_asaclassRoom = "bg/asa_classroom.jpg"
image bg_ele = "bg/ele.jpg"
image bg_kyoumu = "bg/kyoumusitu.jpg"
image bg_yaibarann = "bg/yaibarann.jpg"
image bg_springfieldomoide = "bg/springfieldomoide.jpg"
image bg_springfieldomoide2 = "bg/springfieldomoide2.jpg"
image bg_yuuhi = "bg/yuuhi.jpg"
image bg_idw = "bg/idwdanya.jpg"
image bg_trap = "bg/trap.jpg"

image bg_classikumichi = "bg/classgo.jpg"
image bg_conanshot = "bg/conanshot.png"
image bg_reimumori = "bg/reimumori.jpg"
image bg_akuaend = "bg/akua_ending.jpg"
image bg_explosion = "bg/explosionend.jpg"
image bg_tohoend = "bg/toho_ending.jpg"
image bg_anataend = "bg/anata.jpg"

image eileen movie = Movie(channel="eileen",play ="bakuretu.mpg")
image mikami movie = Movie(channel="eileen",play="sakujo.mpg")

image bg_meikai = "bg/meikai.jpg"    
init:
    image bg_reimukuro : #5
        "bg/reimumori.jpg"
        pause 0.05
        "bg/reimumori2.jpg"
        pause 0.05
        "bg/reimumori3.jpg"
        pause 0.05
        "bg/reimumori4.jpg"
        pause 0.05
        "bg/reimumori5.jpg"
        pause 0.05
    image bg_classkuroka : 
        "bg/asa_classroom.jpg"
        pause 0.05
        "bg/asa_classroom2.jpg"
        pause 0.05
        "bg/asa_classroom3.jpg"
        pause 0.05
        "bg/asa_classroom4.jpg"
        pause 0.05
    image bg_yanndereka :
        "bg/yanndere1.jpg"
        pause 0.05
        "bg/yanndere2.jpg"
        pause 0.05
        "bg/yanndere3.jpg"
        pause 0.05
        "bg/yanndere4.jpg"
        pause 0.05
        "bg/yanndere5.jpg"
        pause 0.05
        "bg/yanndere6.jpg"
        pause 0.05
image bg_yanndere = "bg/yanndere1.jpg"
init:
    image scg_yaieki :
        "character/sense/yaieki.png"
        xalign 0.0
        linear 0.5 xalign 0.5
        linear 5.0 zoom 1.2
    image scg_spring_idlekuru:
        "character/spring/springfield_idle1.png"
        xalign 1.0
        linear 0.75 xalign 0.5
    image scg_spring_idlekuru2:
        "character/spring/springfield_idle1.png"
        xalign 0.5
        linear 0.3 xalign 0.5
        linear 1.0 xalign 0.85
    image scg_spring_egaokuru:
        "character/spring/springfield_egao1.png"
        xalign 0.85
        linear 0.8 xalign 0.5
    image scg_spring_hohoemikuru:
        "character/spring/springfield_hohoemi1.png"
        xalign 0.5
    image scg_spring_sagekitouzyo:
        "character/spring/springfield_sageki.png"
        xalign 1.0
        linear 0.75 xalign 0.5
    image scg_spring_yanndere:
        "character/spring/springfield_yann.png"
        xalign 1.0
        linear 0.75 xalign 0.5
    image rasistouzyou:
        "character/spring/rasis.png"
        xalign 1.0
        linear 0.75 xalign 0.45
init:
    image scg_insStand :
        "character/kuroi/kuroi_stand.png"
        linear 0.1 xalign 0.3
image scg_insAware = "character/kuroi/kuroi_aware.png"
image scg_kim = "character/Kim.png"

image zoominsAware:
    "character/kuroi/kuroi_aware.png"
    linear 1.5 zoom 1.2



image scg_kuroiwarai :
    "character/kuroi/kuroi_warai.png"
    linear 0.5 zoom 1.1
image scg_goza = "character/kuroi/kuroi_goza.png"
image scg_yagami = "character/yagami/yagami.png"
image scg_yagami2 = "character/yagami/yagami2.png"
image scg_sibalisu = "character/sense/isukeruna.png"
image scg_sibal = "character/sense/yaisekidura.png"

# 시발아조씨 
image scg_sibaltouzyo :
    "character/sense/yaisekidura.png"
    xalign 1.0
    linear 0.7 xalign 0.5
image scg_sibaltouzyo2 :
    "character/sense/yaisekidura.png"
    xalign 0.0
    linear 1.0 xalign 0.2
image scg_sibaltouzyo3 :
    "character/sense/yaisekidura.png"
    xalign 0.2
    linear 0.25 xalign 0.2
    linear 0.5 xalign 1.0 zoom 0.3 alpha 0.5
    linear 0.5 zoom 0.1 alpha 0.0
image scg_suldesk = "character/setumei/sul_desk.png"
image scg_sulidle = "character/setumei/sul_idle.png"
image scg_sulnonri = "character/setumei/sul_nonri.png"

# 유유코
image scg_yuyuko_idle = "character/yuyuko/yuyuko_idle.png"
image scg_yuyuko_idle2 = "character/yuyuko/yuyuko_idle2.png"
image scg_yuyuko_warai = "character/yuyuko/yuyuko_warai.png"
image scg_yuyuko_yosome = "character/yuyuko/yuyuko_yosome.png"
# 은여울
image scg_yeoul_idle = "character/hiroin/portrait_misaki_01.png"
image scg_yeoul_close = "character/hiroin/portrait_misaki_02.png"
image scg_yeoul_angry = "character/hiroin/portrait_misaki_03.png"
image scg_yeoul_aware = "character/hiroin/portrait_misaki_04.png"
image scg_yeoul_sinpai = "character/hiroin/portrait_misaki_05.png"
image scg_yeoul_damage = "character/hiroin/portrait_misaki_06.png"
image scg_nugu_angry = "character/hiroin/hideyosi_angry.png"
# 히데요시 철수
init:
    image scg_nugu_idle :
        "character/hiroin/hideyosi_idle.png"
        linear 0.1 xalign 1.0
    image scg_nugu_idle2 :
        "character/hiroin/hideyosi_idle2.png"
        linear 0.1 xalign 1.0
    image scg_nugu_metal:
        "character/hiroin/hideyosi_metal.png"
        xalign 0.0
        linear 1.4 xalign 0.80
        linear 0.15 xalign 0.4
        linear 0.15 xalign 0.5
        linear 0.15 xalign 0.4
        linear 0.15 xalign 0.5
        linear 0.15 xalign 0.4
        linear 0.15 xalign 0.5
        linear 0.15 xalign 0.4
        linear 0.15 xalign 0.5
        linear 0.15 xalign 0.4
        linear 0.15 xalign 0.5
        linear 0.15 xalign 0.4
        linear 0.15 xalign 0.5
        linear 0.15 xalign 0.4
        linear 0.15 xalign 0.5
        linear 0.15 xalign 0.4
        linear 0.15 xalign 0.5
        linear 0.15 xalign 0.4
        linear 0.15 xalign 0.5
        linear 0.15 xalign 0.4
        linear 0.15 xalign 0.5
        linear 0.15 xalign 0.4
        linear 0.15 xalign 0.5 
        linear 0.15 xalign 0.4
        linear 0.15 xalign 0.5 
        linear 0.15 xalign 0.4
        linear 0.15 xalign 0.5 
        linear 0.15 xalign 0.4
        linear 0.15 xalign 0.5 
        linear 0.15 xalign 0.4
        linear 0.15 xalign 0.5 
        linear 0.15 xalign 0.4
        linear 0.15 xalign 0.5 
        linear 0.15 xalign 0.4
        linear 0.15 xalign 0.5 
        linear 0.15 xalign 0.4
        linear 0.15 xalign 0.5 
        linear 0.15 xalign 0.4
        linear 0.15 xalign 0.5 
        linear 0.15 xalign 0.4
        linear 0.15 xalign 0.5 
        linear 0.15 xalign 0.4
        linear 0.15 xalign 0.5 
        linear 0.15 xalign 0.4
        linear 0.15 xalign 0.5 
        linear 0.15 xalign 0.4
        linear 0.15 xalign 0.5 
        linear 0.15 xalign 0.4
        linear 0.15 xalign 0.5 
        linear 0.15 xalign 0.4
        linear 0.15 xalign 0.5 
        linear 0.15 xalign 0.4
        linear 0.15 xalign 0.5 
        linear 0.15 xalign 0.4
        linear 0.15 xalign 0.5
        linear 0.15 xalign 0.4
        linear 0.15 xalign 0.5 
        linear 0.15 xalign 0.4
        linear 0.15 xalign 0.5 
        linear 0.15 xalign 0.4
        linear 0.15 xalign 0.5 
        linear 0.15 xalign 0.4
        linear 0.15 xalign 0.5 
        linear 0.15 xalign 0.4
        linear 0.15 xalign 0.5 
        linear 0.15 xalign 0.4
        linear 0.15 xalign 0.5 
        linear 0.15 xalign 0.4
        linear 0.15 xalign 0.5 
        linear 0.15 xalign 0.4
        linear 0.15 xalign 0.5 
        linear 0.15 xalign 0.4
        linear 0.15 xalign 0.5 
        linear 0.15 xalign 0.4
        linear 0.15 xalign 0.5
image scg_guzun1 = "character/guzun.png"       
# 레이무
init:
    image scg_reimu_1 : 
        "character/reimu/reimu_1.png" 
        linear 0.1 xalign 1.0
    image scg_reimu_2 : 
        "character/reimu/reimu_2.png"
        linear 0.1 xalign 1.0
    image scg_reimu_3 :
        "character/reimu/reimu_3.png"
        linear 0.1 xalign 1.0
    image scg_reimu_4 :
        "character/reimu/reimu_4.png"
        linear 0.1 xalign 1.0
    image scg_reimu_angry1 : 
        "character/reimu/reimu_angry1.png"
        linear 0.1 xalign 1.0
    image scg_reimu_idle :
        "character/reimu/reimu_idle.png"
        linear 0.1 xalign 1.0
    image scg_reimu_sinna : 
        "character/reimu/reimu_sinna.png"
        linear 0.1 xalign 1.0

define center = Position(xalign = 0.5)
define left = Position(xalign=0.2)
define right = Position(xalign=0.8)

label start:
    scene bg_myroom with fade
    play music "bgm/Goodmorning.mp3"  fadeout 1.0 fadein 1.0
    $end_point = 0
    $sibal_point = 0
    $otaku_point = 0
    $yann_point = 0
    "Episode 01. 새학기 반장선거"
    "어느 반도의 평범한 남학생 방"
    "상쾌한 아침을 시작하는 소리가 들려오고 난 눈을 떳다."
    
    ch_ins "'5분만 더 잘까?'"
    menu :
        "5분만 더 잔다.":
            stop music fadeout 1.0 
            "알람을 해제하고 다시 눈을 감았다"
            "..."
            "....."
            play music "bgm/gisannapal.mp3" 
            "........"
            "..........."
            ".............."
            "..................!!!"
            ch_ins "xx 왜 이딴 기상송이 있는거야?"
            stop music fadeout 1.0 
            ch_ins "왠지 모르겠지만 본능적으로 싫은 음악이야.."
            play music "bgm/nichizyo.mp3" 
            $end_point = 2
        "일어나 학교갈 준비를 한다.":
            stop music fadeout 1.0 
            "하아...."
            "진짜 학교 가기 싫다.."
            $end_point = 1

            play music "bgm/nichizyo.mp3" fadeout 1.0 fadein 1.0
    "여느때와 다름없이 맞이한 아침\n오늘도 학교를 가기 위해 준비를 했다."
    "거울 앞에 서서 내 얼굴을 체크하는 순간 나는 위화감을 느꼈다."
    show scg_insAware at left with dissolve
    ch_ins "뭐.. 뭐야?..."
    ch_ins "잘 생겼잖아?"
    "몸에 근육도 잘 붙어있고 살도 좀 빠진 것 같고 아무튼 매력적이었다"
   
    ch_ins "'새 학기의 시작과 함께 내 몸도 새롭게 변했나보군. 뭐든지 다 할 수 있을 것 같아..'"
    if(end_point==1):
        scene bg_classikumichi with fade
        "평소보다 일찍 나온 나는 여유가 있었고 상쾌한 기분을 만끽했다."
        "매일 같은 길도 다르게 느껴지고 왠지 새로운 만남이 있을 것만 같은 느낌이다."
        menu:
            "기분 전환겸 옆에 보이는 숲길로 산책을 하며 걸어간다":
                scene bg_reimumori with fade
                "'이런 곳이 있었나 엄청 난데?'"
                "그곳에는 가는 길에 보이는 모든 괴물은 물론이고 인간도 퇴치해버릴 것 같은 소녀가 있었다."
                play music "bgm/th105reimu.mp3" 
                show scg_reimu_1  with dissolve
                "...!?"
                menu:
                    "겁먹지 않고 가던 길을 간다.":
                        hide  scg_reimu_1 
                        show scg_reimu_4 with dissolve
                        ch_reimu "???"
                        "이상한 복장의 소녀는 나를 응시하고 있다."
                        hide  scg_reimu_4 
                        show scg_reimu_2 with dissolve
                        ch_reimu "거기 너 잠깐만 기다려"
                        ch_ins "???"
                        hide  scg_reimu_2 
                        show scg_reimu_idle with dissolve
                        ch_reimu "너 왠지 이번 이변에 대해서 잘 알거 같은데?"
                        ch_ins "이변이라니 무슨소리야?"
                        ch_reimu "너를 중심으로 세계의 시공이 뒤틀려져 가고 있는게 느껴지거든"
                        ch_ins "저기.. 진짜 무슨 소리를 하는지 모르겠거든.."
                        hide  scg_reimu_idle
                        show scg_reimu_angry1 with dissolve
                        ch_reimu "시치미 때도 소용없어. 너에게서 느껴지는 기운이 틀림없는 증거니까"
                        ch_ins "잠.. 잠깐만"
                        hide scg_reimu_angry1
                        show scg_reimu_1  with dissolve
                        ch_reimu "문답무용!!"

                        scene bg_reimukuro with dissolve
                        ch_ins "하아아... 저 깡패년... "
                        ch_ins "..."

                        "죽고 난 다음 가고 싶은 곳은?"
                        menu:
                            "나는 이세계에 가서 깽판을 칠 것이다.":
                                "..."
                                jump akua_ending
                            "그냥 편히 쉬고 싶다":
                                "..."
                                jump yuyuko_ending
                    "지금 당장 도망간다":
                        hide  scg_reimu_1 
                        show scg_reimu_2 with dissolve
                        ch_reimu "? 뭐야 왜 사람을 보자마자 도망가는거야?"
                        ch_ins "그.. 그게 빨리 학교가야한 다는 사실이 떠올라서"
                        hide  scg_reimu_2 
                        show scg_reimu_angry1 with dissolve
                        ch_reimu "그러고보니 너에게서 묘한 기운이 느껴지는데 니가 이번 이변의 원인이지?"
                        ch_ins "무슨 소리야? 이변이라니"
                        hide scg_reimu_angry1
                        show scg_reimu_1  with dissolve
                        ch_reimu "둘러대지 마시지 니가 이번 이변의 원인이니까 도망가려 했겠지"
                        ch_ins "잠.. 잠깐만"
                        ch_reimu "문답무용!!"
                        scene bg_reimukuro with dissolve
                        stop music fadeout 1.0
                        ch_ins "하아아... 저 깡패년... "
                        ch_ins "..."

                        "깡패 무녀와의 만남 배드엔딩을 맞이하였습니다."

                        scene bg_tohoend with dissolve
                        play music "bgm/tohoend.mp3" 
                        "주인공을 퇴치하자 겨드랑이 무녀의 세상인 환상향의 공간전이의 이변은 해결되었습니다."
                        "주인공은 알게모르게 신이 만들어낸 세상에서 다른 차원, 다른 시공의 인물들을 불러들였던 것이었습니다."
                        "사실 모태솔로인 주인공이 연예에 성공하면 사라지는 이변인데 깡패무녀 덕에 빨리 해결 되었습니다."
                        "연예 한 번 못해보고 억울하게 죽은 주인공은 안타깝지만 환상향의 친구들은 평화롭게 잘 지내는 것 같아 다행입니다."
                        "... 하아.. XX"
                        return
            "오늘 따라 걷기가 싫으니 버스를 타고 간다.":
                "오늘은 버스를 타고 등교하기로 결정했다."
                "의자에 앉자 마자 앞의 아저씨가 뒤돌아보며 나에게 말을 걸었다."
                show scg_sibalisu with dissolve
                ch_nanimono "의자 차면 죽여버린다"
                $sibal_point = 1
                ch_nanimono "시발년아"
                ch_ins "???"
                ch_ins "'뭐지 이 초면에 욕하는 아저씨는...''"
                menu:
                    "아무리 나이 많은 어른이지만 욕을 먹은 이상 참을 수 없다.\n한 마디 해준다.":
                        show scg_insStand at right with dissolve 
                        ch_ins "아저씨는 뭔데 지랄이야?"
                        stop music fadeout 1.0
                        play music "bgm/Lowof.mp3" fadein 1.0
                        ch_nanimono "아니 시발 뭐라했어?"
                        ch_ins "지랄이라고 했다. 왜?"
                        ch_nanimono "이런 싸가지 없는 새끼를 봤나?"
                        ch_ins "아저씨 부터 지랄 했잖아 이 미친새끼야"
                        ch_nanimono "이런 버르장머리 없는 새끼 보아하니 남창고등학교 다니는 것 같은데 잘 만났다."
                        ch_ins "왜 학교에 신고라도 하게? 이 꼰대틀딱아."
                        
                        "그렇게 언쟁이 계속 되고 주변 사람들이 쳐다보기 시작했다."
                        play sound "bgm/sakujovoice.mp3"
                        ch_nanimono2 "삭제"
                        "그 삭제라는 단어를 들은 순간 나는 왠지 모를 불안함을 느꼈다."
                        hide scg_sibalisu
                        hide scg_insStand
                        with dissolve
                        show zoominsAware at left 
                        
                        ch_ins "뭐야.. 이 느낌은?"
                        play sound "bgm/40.mp3"
                        ch_ins "설.. 설마?"
                        "갑자기 심장에서 아픔이 느껴졌고 난 그대로 쓰러졌다."
                        "'키..라가 이 버..스에 타 있 었 을 줄이야...'"
                        "'아..아.. 젠장 화 좀 참고 살 걸 그랬어..'"
                        show mikami movie
                        
                        "화를 참지 못하고 어른에게 욕을 하고 나쁜 짓을 하면 이렇게 정의의 심판을 받을 수도 있습니다."
                        "우리 모두 착하게 삽시다."
                        "축하합니다. 삭제 당하는 엔딩을 맞이하였습니다."
                        return
                    "그냥 참고 넘어간다.":
                        "'성격 참 더럽네.. 다시는 마주치고 싶지 않다.'"
                        "이 때의 나는 몰랐다.. 저 인간이랑 또 만나게 될 것이라는 것을..."
    if(end_point==2):
        scene bg_ele with fade
        "나는 어서 가방을 챙기고 밖에 나가서 엘리베이터로 내려가기 시작한 찰나 바로 아랫층에서 엘리베이터가 멈추었다"
        show scg_yeoul_idle at right with dissolve
        ch_yeoul "안뇨옹"
        "이 녀석은 바로 아래층에 사는 여자로서 엘리베이터 문이 닫히기 전에 나를 봐도 웃으며 문을 닫는 여자다."
        menu :
            "문을 닫기를 빠르게 여러번 누른다.":
                "여울이의 발이 문 닫히는 것을 저지하여 문이 다시 열리게 된다."
                show scg_yeoul_angry at right with dissolve
                ch_yeoul "우쒸 야 죽을래?"
                show scg_insStand at left with dissolve 
                ch_ins "하아.. 엘리베이터 문 닫는 속도가 니가 들어오는 속도보다 빨랐으면 좋았을 텐데..."
                ch_yeoul "또 문닫으려고 하면 진짜 맞는다."
                ch_ins "너나 좀 버리고 가지마라 진짜..."
                hide scg_yeoul_angry with dissolve
            "문 열기를 눌러준다.":
                show scg_insStand at left with dissolve 
                ch_ins "어.."
                ch_yeoul "어제 뭘 했길래 그렇게 힘이 없냐?" 
   
        "그리고 나선 침묵이 흘렀다. 엘리베이터는 사람에게 침묵이라는 마법을 선사하나 보다."
        scene bg_classikumichi with fade
        show scg_insStand 
        show scg_yeoul_idle at right
        with dissolve 
        ch_ins "맞다 넌 몇반이냐?"
        ch_yeoul "2반"
        ch_ins "아 x됐다. 나도 2반인데"
        show scg_yeoul_angry at right with dissolve
        ch_yeoul "진짜 맞을래?"
        ch_ins "야 어떻게 매번 같은 반에 같은 학원이냐? 혹시 나 따라다니냐?"
        ch_yeoul "헐 내가 미쳤다고 널 따라다니냐?"
        ch_ins "그냥 오늘 일찍 끝내줬으면 좋겠다.."
        ch_yeoul "어차피 끝나고 피시방밖에 더 안 가잖아. 게임 좀 그만해라"
        ch_ins "그게 나보다 티어도 높으신 분이 할 말이세요?"
        ch_yeoul "그건 니 손이 문제라서 그런거지"
        menu:
            "날 욕하는 건 참아도 게임허졉이란 말은 못참는다. 이 자리에서 죽여버린다":
                "주인공이 여울이를 향해 악의를 품고 다가가자"
                "갑자기 축구공이 날아왔다."
                jump goza_ending
            "아놔.. 한 두번 이긴거 가지고 잘난척하지말고 오늘 끝나고 1:1 한판할래?":
                ch_yeoul "콜 지면 매점빵"
                ch_ins "콜"

        "그렇게 대화를 하다보니 어느샌가 학교에 도착했다."
    scene bg_asaclassRoom with fade
    stop music fadeout 1.0
    play music "bgm/StarCraft_Soundtrack_Terran.mp3"
    "새학기의 시작... 새롭게 만나는 인간관계에서 부터 내 인생은 변한다."
    "여기선 사람들을 파악하고 전략적으로 신중하게 행동해야겠어."
    "나는 우선 반의 분위기를 살펴보았다."
    show scg_yagami at left with dissolve
    ch_ins "'음...'"
    ch_ins "'이 친구한테 말을 걸어볼까?'"

    play sound "bgm/sinsegenokami.mp3"
    hide scg_yagami
    show scg_yagami2 at right with dissolve
    ch_nanimono "잘 들어.. 난 키라 그리고,, 신 세 계 의 신 이 다"
    ch_nanimono "내가 정의다!"
    ch_ins "뭐야.. 이 중2병 걸린 놈은.."
    ch_ins "'아...저 녀석과는 안 친해져야겠다.'"
    hide scg_yagami2
    play sound "bgm/matuda.mp3"
    ch_ins "'저런 애랑은 가까이 다가가지 말아야지..'"
    ch_ins "???"
    ch_ins "정신병잔가?"
    show scg_sulnonri at center with dissolve
    ch_nanimono "그래 저 놈이 정신병자인건 논리적으로 반박할 수 없어."
    ch_ins "얜 또 뭐야?"
    ch_nanimono "나는 신경쓰지마"
    ch_ins "'본능적으로 느껴졌다. 이 녀석도... 병신이라는 것이'"
    ch_ins "으.. 응"
    hide scg_sulnonri
    "난 말을 걸어온 아이에게서 떨어진 쪽 자리에 앉았다."
    "그렇게 반 분위기를 계속 살피던 중 어떤 여자아이가 나에게 다가왔다."
    show scg_nugu_idle with dissolve
    ch_nugu "안녕 난 철수라고 한다네. 옆에 앉아도 괜찮을까"
    ch_ins "'이름도 남자같은 모르는 여자애가 먼저 이상한  말투로 말을 걸어오다니 수상하다. 신종 사이비종교 권유 혹은 다단계일지도 모른다.'"
    menu:
        "미안한데 난 이미 믿는 종교가 있고 돈은 한 푼도 없어":
            ch_nugu "그대는 날 뭐라고 생각하는 겐가?"
            ch_ins "머리가 이상한 여자애"
            ch_nugu "내 성별은 그대와 같은 남자일세"
        "ㅇ.. 어.. 앉아.. 근데 저기 여자들 있는 곳으로 가는게 좋지 않겠어?":
            ch_nugu "그대는 날 뭐라고 생각하는 겐가?"
            ch_ins "머리가 이상한 여자애"
            ch_nugu "내 성별은 그대와 같은 남자일세"
    ch_ins "'믿을 수 없어. 이 얼굴에 남자라고?'"
    ch_ins "뭐 내 이름은 인공이야"
    ch_nugu "오 좋은 이름이구려"
    ch_ins "아니야 그것보다.."
    ch_nugu "왜 그러는가?"
    ch_ins "진짜 남자야?"
    hide scg_nugu_idle
    show scg_nugu_angry with dissolve
    ch_nugu "남자라니까"
    ch_ins "뭐 믿을게"

    hide scg_nugu_angry
    
    "그렇게 잡담을 하고 있으니 어느새 선생님이 들어왔다."
    show scg_sibaltouzyo with dissolve
    ch_nanimono "선생이 들어왔는데도 떠들고 있어? 조용히해 이 새끼들아"
    if(sibal_point==1):
        "아침에 봤던 그 미친놈이 잖아?"
    else:
        "뭔 선생이 저렇게 입이 험해?"
    ch_nanimono "내 이름은 '시발국회의원더럽게일안하네' 다. 이름가지고 뭐라하면 죽는다."
    ch_sense "난 일을 빨리 처리하는 걸 좋아해 지금 당장 반장을 뽑도록 하겠다."
    ch_sense "반장 하고 싶은 사람 손들어."
    ch_sense "아니다 됐다 그냥 출석번호 몇개 부를테니까 그 중에 뽑아"
    "'뭐야 이 선생은'"
    ch_sense "503번"
    ch_nanimono2 "그런 번호 없는데요 선생님."
    ch_sense "시발 농담한거 가지고 더럽게 지랄하네."
    ch_sense "그럼 이번주 로또 당첨번호 3번 8번 16번 32번 34번 43번 그리고 10번"
    ch_nanimono2 "선생님 출산율 감소로 한 반에 30명 까지 없습니다."
    ch_sense "토 달지마 그럼 3번 8번 16번 10번 나와"

    ch_nugu "이런.. 내가 3번일세.."
    ch_ins "하아.. 나도 10번이야."

    ch_sense "조용히하고 연설해. 너 10번이야? 너부터 해."
    hide scg_sibaltouzyo 
    stop music fadeout 1.0
    play music "bgm/MeitanteiConan.mp3"
    show scg_kuroiwarai with dissolve
    ch_ins "내 이름은 주인공"
    ch_ins "난 반장이 될 인재가 아니고 할 마음도 없으니 날 뽑지 말아줬으면 한다."
    ch_sense "다시 해."
    ch_ins "..."
    ch_ins "존경하고 사랑하는 학우여러분 감사합니다. 주인공입니다. 제 공략은 정책담당관에게 물어보세요."
    ch_nanimono2 "??? 정책담당관이 누군데??"
    ch_ins "그 부분에 대해서는 이미 답해 드렸습니다."
    ch_nanimono2 "아니 언제 말했다는 거야?"
    ch_ins "이미 여러 차례 답변 드리지 않았습니까?"
    ch_ins "이상으로 연설 마치겠습니다."
    ch_sense "훌륭했다. 다음 니 옆에 있던애"
    hide scg_kuroiwarai
    show scg_nugu_idle with dissolve
    stop music fadeout 1.0
    ch_nugu "크흠.. 크흠.."
    ch_nugu "반갑습니다. 학우여러분. 제 이름은 참철수라고 합니다."
    ch_nugu "변화와 개혁을 바라는 절절한 마음입니다."
    ch_nugu "학생을 위한 학생에 의한"  
    ch_nugu "변화시킬 태풍!"
    play sound "bgm/nuguni.mp3"
    hide scg_nugu_idle
    show scg_nugu_metal
    ch_nugu "혁신가 누굽니까아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아"
    ch_nugu "아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아"
    ch_nugu "아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아"
    ch_nugu "아아아아아아아아아---------"
    
    ch_nanimono "와... 성대 성량봐.."
    ch_nanimono2 "잰 여자야? 남자야?"
    ch_nanimono "몰라 맛만 좋으면 되지."
    ch_nanimono2 "미친.."
    ch_nanimono "난 재 뽑을래"
    ch_sense "그래 멋진 연설이었다. 다음 너 나와라"
    ch_sense "되도록 연설하는데 잡담은 하지 마라. 미천한 것들아"
    hide scg_nugu_metal
    show scg_guzun1 with dissolve
    play music "bgm/SS501.mp3"
    ch_guzun "안녕하세요 구준표입니다."
    ch_nanimono "꺄아아아앙! 끼아아악!"
    ch_guzun "전 어릴적부터 대기업 회장 아버지가 일하는 모습을 지켜보며 살아왔습니다."
    ch_guzun "그래서 우리 반의 부와 풍요를 가져다 줄 수 있는 건 저밖에 없습니다."
    ch_nanimono "꺄아아악!!!!"
    ch_sense "좀 닥쳐라."
    ch_guzun "당당한 부자 반장"
    ch_guzun "저 구준표를 뽑아주십시오."
    ch_nanimono "워매 더 잘생긴 애 나왔어. 차원이 달라!"
    ch_nanimono2 "정말 차원이 다른걸.."
    ch_guzun "지키겠습니다. 자유로운 반 분위기"
    ch_guzun "제가 반장이 되지 못한다면 한강 물에 뛰어들겠습니다."
    ch_nanimono2 "제대로 된 공략은 없나요?"
    ch_guzun "제가 반장이 되지 못한다면 낙동강 물에 빠져죽겠습니다."
    ch_nanimono2 "뭐야 어디에 뛰어들겠다는거야?"
    ch_guzun "제가 반장이 되지 못한다면 금강 물에 뛰어들겠습니다."
    ch_guzun "공략 반드시 지키겠습니다. "
    ch_nanimono2 "아니.. 지킬 공략이 있는거야? 아니면 진짜 빠지겠다는건가?"
    hide scg_guzun1
    ch_sense "잘 했다. 그래 다음."
    stop music fadeout 1.0
    show scg_kim with dissolve
    play music "bgm/TrickleMorgan.mp3"
    ch_kim "김정동이라고 한다."
    ch_nanimono "뭐야"
    ch_kim "내가 반장이 되면 모두가 평등하게 배불리 간식을 먹으면서 수업을 듣게 해줄 것이다."
    ch_nanimono2 "헐"
    ch_kim "모두 다 같이 잘 살아보자."
    ch_nanimono "재 김정은 코스프레하다가 지가 김정은인지 아는 애잖아 냅둬"
    ch_nanimono2 "저거 간첩신고 안 되냐?"
    ch_sense "이제 그만 됐다. 자 그럼 투표를 시작하지."
    hide scg_kim with dissolve
    "투표가 시작 되었다."
    "누구를 뽑으시겠습니까?"
    menu:
        "주인공":
            "투표결과는 주인공이 반장이 되었고 철수는 낙선하였다."
        "참철수":
            "투표결과는 주인공이 반장이 되었고 철수는 낙선하였다."
        "구준표":
            stop music fadeout 1.0
            scene bg_classkuroka with dissolve
            "구준표가 반장이 되었고 난 부반장이 되었다."
            "우린 F4가 되어 학교에서 유명해졌다."
            "난 인기가 있다고 생각했지만..."
            "여자들이 좋아하는건 준표였다."

            play music "bgm/zetubou.mp3"
            
            "준표와 함께 다니며 많은 여자가 접근해 왔지만 모두 준표가 목적이었다."
            "결국 난 광대에 불과했던 것이다."
            "그녀들에게 난 그냥 잘생긴 애의 친구였고"
            "난 이용가치가 있는 인간이었던 거다."
            "나를 필요로 하지 않는다."
            "결국 난 연애를 하지 못하고 고등학교 졸업을 했다."
            "준표 친구로..."
            "잘생긴 애 친구로..."
            
            "**..."
            "아 진짜 연애해보고 싶다.."
            "아아... 아!"
            "아아앙!!!"
            "끼아아아악!!"
            return
        "김정동":
            scene bg_yaibarann with dissolve
            stop music fadeout 1.0
            show scg_yaieki with dissolve
            
            play sound "bgm/yaiseki.mp3"
            play music "bgm/DeusNonVult.mp3"
            "국가보안법 제 3조 반국가단체를 구성하거나 이에 가입한 자는 다음의 항목에 따라 처벌한다.\n1. 수괴의 임무에 종사한 자는 사형 또는 무기징역에 처한다.\n2. 간부 기타 지도적 임무에 종사한 자는 사형·무기 또는 5년 이상의 징역."
            "국가보안법 제 4조(목적) 간첩 - 반국가단체의 구성원 또는 그 지령을 받은 자가 그 목적수행을 위한 행위를 한 때에는 다음의 구별에 따라 처벌한다.\n6. 선동하거나 사회질서의 혼란을 조성할 우려가 있는 사항에 관하여 허위사실을 날조하거나 유포한 때에는 2년 이상의 유기징역에 처한다."
            "이 죄는 보안관찰해당범죄이기도 하다."
            "간첩 신고는 국군 기무사령부 - 1337\n합동참모본부 - 1338"
            "국가정보원 전화번호 - 111 / 대한민국 경찰청 113"
            "간첩신고 상금 최고 5억원 , 간첩선 신고 최고 7억 5천만원 신고번호 - 111"

            "당신들은 국가보안법 위반으로 잡혀들어갔습니다."
            "국가 보안법 위반 혐의 엔딩을 맞이하였습니다."
            return
    "이 반장선거 이후 수 많은 것이 변하게 된다."
    "김정동은 잡혀들어가게 되고 낙선한 준표는 공략대로 낙동강 물에 뛰어들어 이후 소식은 묘연하게 된다."
    "철수는 재충전의 시간을 가지겠다며 출석하지 않게 된다.\n절대 귀찮아서 다 없애는게 아니다."
    
    
    show scg_spring_idlekuru with dissolve
    ch_nanimono "저어.. 누구시죠?"
    stop music fadeout 1.0
    hide scg_spring_idlekuru
    show scg_spring_idlekuru2
    show scg_sibaltouzyo2 with dissolve 
    play music "bgm/Minecraft.mp3"
    ch_sense "그럼 댁은 누구세요?"
    ch_spring "전 이 반의 담임인 춘전이라고 하는데요."
    ch_sense "내가 담임이야 ** 꺼져."
    ch_spring "네??"
    "???"
    ch_mercy "그 사람 잡아주세요!!"
    "...?"
    ch_sense "쳇 들켰군"
    hide scg_sibaltouzyo2
    show scg_sibaltouzyo3
    ch_sense "저리 비켜!"
    "그렇게 '**국회의원더럽게일안하네' 는 사라졌다."
    ch_nanimono2 "대체 뭐였던거야..."
    hide scg_spring_idlekuru2
    show scg_spring_egaokuru 
    hide scg_sibaltouzyo3
    ch_spring "... 어 애들아 내가 앞으로 이 반을 담당하게 될 선생님이야.."
    ch_spring "지금까지 대체 뭘 하고 있었던 거니? 애들아.."
    ch_nanimono2 "반장을 뽑았습니다. 선생님"
    ch_nanimono "그냥 방금 전에 뽑은 사람을 반장으로 하는 게 좋다고 생각합니다. 선생님"
    ch_ins "어... "
    ch_spring "반장은 그럼 누구니?"
    ch_nanimono2 "저 친구입니다. 선생님"
    ch_ins "저는.. 반장 같은거..."
    ch_spring "잘부탁해. 이름은 뭐니?"
    "선생님의 웃음과 얼굴을보니.."
    ch_ins "주인공이라 합니다. 선생님의 수족이 되겠습니다."
    "말이 이상하게 나왔다."
    ch_spring "그래 잘 부탁해. 있다 끝나고 교무실에 와줄래?"
    ch_nanimono "선생님 남자 친구 있어요?"
    show scg_spring_hohoemikuru with dissolve
    ch_spring "아직 없단다."
    ch_nanimono "쌤 자기소개 해주세요!!"
    ch_spring "음.. 선생님은 여행 그리고 사격이 취미야. 여러 곳을 돌아봤고 사격으로 많은 이들을 이겨봤단다."
    ch_spring "사격 하는 사람들 사이에선 다들 나를 '봄날의 평야 (스프링필드)'라고 부를 정도로 유명한 실력자가 될 정도?"
    ch_spring "애들아 우리 모두 서로 즐겁게 지내봐요."  
    "네앱!!!"
    stop music fadeout 1.0
    scene bg_kyoumu with fade
    "학교 수업이 끝나고 나는 교무실의 선생님을 찾아갔다."
    play music "bgm/owari.mp3"
    ch_ins "안녕하세요!"
    show scg_spring_idlekuru with dissolve
    ch_spring "어 왔니? 안 오길래 왜 안 오나 했는데 설마 학교마치고 오라는 줄 알았니?"
    ch_ins "넵"
    ch_spring "아침 조회 끝나고 오라는 걸 잘못 전달했구나..."
    "선생님의 책상에는 '최신 군용 총기 사전', '제1차 세계대전'과 같은 책들이 놓여져있었다."
    ch_ins "'이 선생님은 밀덕인가..'"
    ch_spring "오늘 아침에 머핀을 구워봤는데 같이 먹을래?"
    ch_ins "넵! 머핀 엄청 좋아해요."
    "쩝쩝"
    ch_ins "저 근데.."
    ch_spring "입가에 빵가루가 묻었네.. 후후, 가만히 있어봐 떼어줄게."
    "..."
    ch_ins "저어 그런데 부르신 이유가..?"
    ch_spring "애들한테 나눠줄 프린트도 전해줄겸 앞으로 부탁 많이 할 반장하고 친해지기 위해서지"
    ch_ins "맡겨주세요. 바로 제가 프린트 나눠주기의 프로입니다."
    ch_spring "음.. 인공이는 꿈이 뭐니?"
    menu:
        "선생님의 남자친구요.":
            $otaku_point = 1
            ch_spring "농담도 참 잘하는 구나. ㅎㅎ"
            ch_ins "저도 사격 정말 좋아하고 잘해요. 선생님!"
        "국가를 지키는 군의 지휘관이 되고 싶습니다.":
            $otaku_point = 0
            ch_ins "군인인 아버지를 보며 저도 언젠가 녹색견장을 차고 싶었습니다.."
            ch_spring "아버지가 군인이시니?"
            ch_ins "네. 그리고 저도 사격이 취미예요. 선생님"

    ch_ins "나중에 사격 내기 한 번 해보지 않을래요 선생님?"
    ch_spring "후후 선생님은 상당한 실력자란다."
    ch_ins "쉽지만은 않을 거예요 선생님 저도 상당한 실력자거든요."
    
    "나는 학기 내내 선생님께 잘 보이려고 노력했다."
    "여러가지 일이 있었지만 어찌 저찌 학기가 끝났다."
    "그리고 여름이 왔다."
    scene springfieldomoide with dissolve
    stop music fadeout 1.0
    "전의 약속대로 나는 선생님과 함께 우리 아버지의 별장에 있는 섬에 사격을 하러 왔다."
    "그렇다. 난 갑부다."
    ch_ins "선생님, 어때요? 사격하기 좋은 곳이죠?"
    show scg_spring_sagekitouzyo with dissolve
    ch_spring "그러게.. 날씨도 정말 좋구나."
    play music "bgm/BG_lobby.mp3"
    ch_ins "더 많이 맞추는 쪽이 원하는 것 하나 들어주기 어때요?"
    ch_spring "후후 난 지지 않는단다."
    hide scg_spring_sagekitouzyo 
    show rasistouzyou with dissolve
    ch_rasis "하와와.. 안녕하세요! 레이시스라고 해요!"
    ch_rasis "크흠 크흠"
    ch_rasis "헬븐리 헤븐 사격장에 어서 오세요! 여러분의 쾌적한 사격을 지원해 드리겠습니다."
    ch_ins "'와 사격통제해주는 사람 진짜 이쁘네.'"
    menu:
        "나중에 몰래 작업을 건다.":
            $yann_point = 1
            "'역시 내 취향이야 나중에 연락처 물어야지'"
        "신경쓰지 않는다.":
            $yann_point = 0
            "'반드시 만발을 쏴주겠어.'"
    ch_rasis "아.. 아 하나 둘 셋 하나 둘 셋 후후.."
    "레이시스양이 마이크를 테스트하고 있다. 뭔가 귀엽다."
    ch_rasis "사로 통제하겠습니다. 노리쇠 후퇴고정"
    "갑자기 목소리가 낮게 변했다. 급격한 변화에 멍때리고 있자.."
    ch_rasis "복명복창 합니다."
    "...???"
    ch_rasis "복명 복창 합니다! 노리쇠 후퇴 고정!"
    "일단 레이시스의 말대로 복명복창하기 시작했다."
    ch_ins "노리쇠 후퇴고정!!"
    ch_rasis "탄피받이 결합"
    "탄피 받이 결합!"
    ch_rasis "탄확인"
    "우상탄 10발 이상무!"
    ch_rasis "복명복창 크게 합니다."
    "우상탄 10발 이상무!!!"
    ch_rasis "탄알집 결합"
    "탄알집 결합!!!"
    ch_rasis "노리쇠 전진"
    "(촤락!)"
    ch_rasis "조정간 단발"

    
    ch_rasis "준비된 사수로부터 사. 격. 개시"
    "타앙! 타앙!!"
    "우리는 최대한 집중해서 사격했다."
    ch_rasis "사격 중지. 탄피이상유무 확인"
    ch_ins "1사로 이상무"
    ch_spring "2사로 이상무"
    ch_rasis "1사로 19발"
    ch_rasis "2사로 19발"

    stop music fadeout 1.0
    "사격의 결과는 무승부였다."
    ch_ins "아까웠네요. 선생님"
    ch_spring "좋은 승부였어 인공아"

    if(yann_point == 1):
        scene bg_yuuhi with dissolve
        show scg_spring_yanndere with dissolve
        play music "bgm/immanence-calshutain.mp3"
        ch_spring "후후 찾고 있었어요..."
        ch_ins "서..선생님? 대체 왜 이래요?"
        ch_spring "그렇게 잔뜩 절 좋다고 해놓고는... 다른 여자한테 작업인가요?"
        ch_spring "전 그렇게 가르친 기억이 없답니다."
        ch_ins "뭔가 오해를.."
        ch_spring "레이시스양 이었던 가요?"
        ch_spring "걱정하지 않아도 되요.. 바람 필 일이 일어나지 않도록 잘 처리해뒀으니까요"
        ch_ins "저어.. 선생님??"
        "나는 무의식적으로 뒷걸음 치며 피하고 있었다."
        ch_spring "왜 저를 피하는 거죠?"
        ch_spring "당신이 절 꼬득여 놓고선 절 피하는 건가요?"
        ch_spring "정말 너무 하시네요."
        ch_spring "다리에 빵가루가 묻었네요. 후후, 가만히 있어주세요, 떼어드릴게요."
        "순간 난 움직이지 못했고 정신차린 순간"
        "칼이 내 다리에 박혀져있었다."
        ch_ins "끄아아악"
        ch_spring "어머 빵가루만 뗴어버린다는게 그만 실수 했네요. 안심하세요. 제가 손 수 치료해드릴게요"
        "출혈로 인해 의식이 흐려져 간다."
        scene bg_yanndere with dissolve
        show scg_spring_egaokuru with dissolve
        ch_spring "후훗, 좋은 아침이네요."
        ch_ins "?? 여긴 어디죠? 머리도 아프고.. 다리에 감각이..."
        ch_spring "어젯밤 이 섬에 괴한이 나타났다고 하는 것 같더라고요."
        ch_ins "... 기..기억이.."
        ch_spring "무리해서 떠올리지 마세요. 지금은 안정을 취할 때 예요.."
        ch_spring "많이 아팠죠? 참느라 수고했어요.. 인공아 물 한 잔 마실래?"
        ch_ins "아..네.."
        ch_spring "기다려봐 사과 깍아줄게.."
        "난 물을 마시며 선생님의 사과 깍는 모습을 바라보았다."
        ch_ins ".. 그 칼 어디서 본 기억이.."
        "갑자기 어제 있었던 일들이 떠오르기 시작했다.."
        "나는 새파랗게 질린 얼굴이 되어 열심히 이 상황에서 벗어날 궁리를 했다."
        ch_spring "기억이란 건 이렇게나 지우기 힘든 걸까요?"
        ch_ins "저어.. 선생님?"
        ch_spring "다 잊게 해줄게요. 아픈 것도 힘든 것도.."
        hide scg_spring_egaokuru with dissolve
        show bg_yanndereka 
        ch_spring "인공이는 다 잊어버리고.. 그저 항상 제 곁에 있으면 되요."
        ch_spring "그러면 모두가 행복해.."
        "얀데레화 엔딩을 맞이하였습니다."
        return
    scene bg_springfieldomoide2 with dissolve
    play music "bgm/arayo.mp3"
    show scg_spring_idlekuru with dissolve
    ch_spring "정말 예쁜 섬이네요.."
    ch_ins "선생님 줄게 있어요."
    menu:
        "사격경기용 철갑탄을 준다.\n(M1903에 사용 되는 매치 그레이드 탄약)":
            if (otaku_point == 1):
                stop music fadeout 1.0
                "갑자기 정신이 흐려 지며 난 쓰러졌다.."
                scene bg_anataend with dissolve
                play music "bgm/anatahasokoni.mp3"
                "지금까지 꿈을 꾸고 있었다는 걸 난 깨달았다.."
                "평소처럼 휴대폰으로 소녀전선을 실행하였다."
                "나의 부관 스프링필드(춘전)은... 잘 있었다.."
                "꿈속의 추억들이 ...... 나는 눈물이 났다."
                "그 어느 인형들보다 난.. 춘전이가 좋았다."
                "춘전이의 손 한번 잡고 싶어도 거긴 갈 수 없는 세상이라는 것이 너무 슬펐다."
                "아침에 눈을 뜨면 항상 내 옆에 그대가 미소를 짓고 있죠."
                "모닝터치를 피하지 않고 받아주는 게 늘 고마울 뿐"
                "상쾌한 하루의 시작, 웃음꽃이 핀다."
                "당신의 옷을 사주기 위해 내 옷을 포기했을 뿐인 생활을 1년"
                "남들은 가치관이 병들었다 날 타일러"
                "다 집어치워"
                "내겐 그녀만 있으면 돼"
                "실컷 떠들어봐 돼지 오덕후 아님 변태"
                "절대 후회 안해 널 선택한 걸 평생"
                "... 내가 틀렸다고?"
                "웃기지마!!!"
                "..."
                "춘전짱 나는 진지하다능! M14보다 어느 4성 라이플보다 니가 좋다능"
                "... 씹덕후 엔딩을 맞이하였습니다."
                return

            else:
                ch_spring "어떻게... 내가 사격경기용 철갑탄을 가지고 싶어했다는 걸 알았니?"
                ch_ins "난 선생님에 대한 거라면 뭐든지 알고 있어."
                ch_ins "이제 선생님 말고 누나라 부르면 안 될까?"
                ch_spring "안 됏 난 선생이고 넌 제자야.."
                ch_ins "지금 당장 안 된다고 해도.. 내가 나중에 꿈을 이뤄 지휘관이 되면 그 땐 그래도 되지?"
                ch_spring "... 니 마음대로 해.."
                "..."
                
                "난 결국 지휘관이라는 꿈을 이루었다."
                "알고보니 춘전이누나는 간첩으로 추정되는 인물을 감시하기 위해 만들어지고 파견된 국방과학연구소의 인형이었다."
                "난 춘전이 누나의 상관이 되었고 사람이 아닌 인형에게 청혼을 하였다."

                $ renpy.movie_cutscene("springend.mpg")
                return

        "낭만적으로 예쁜 꽃을 준다.":
            stop music fadeout 1.0
            scene bg_idw with dissolve
            play sound "bgm/IDW.mp3"
            play music "bgm/YouJustActivatedMyTrapCard.mp3"
            "아이디 더브류다냐!"

            "히키톳테 쿠레루카냥"
            "시키캉 네코는 좋아하냥?"
            "01:10"
            "네코미미 잇빠이다냐아아아!!!"
            "잇쇼니 아소부냐아!!"
            show bg_trap with dissolve
            "당신은 함정에 걸려들었습니다."

            "함정 엔딩을 맞이하였습니다."
            "당신이 만약 소녀전선을 한다면 이제 01:10 라는 시간을 볼 때마다 당신은 idw 만 나올 것입니다."
            "아이디 더브류다냐아아!!!!!!!!!!!!!!!!"
            "Ha ! Ha ! Ha ! You Just Activated My Trap Card ! "
            return 
    play music "horann.mp3"  fadein 1.0
    ch_ins "기하학"

    return

    label goza_ending:
        scene bg_conanshot with fade
        play music "bgm/meitanntei.mp3"
        "초등학생의 킥에 날아온 축구공의 파괴력은 엄청났다."
        ch_ins "크허억억"
        show scg_goza with dissolve
        "주인공은 축구공에 맞고 날아갔다."

        ch_ins "큽..."
        "축구공이 영 안 좋은 곳에 맞아 결국 고자가 되어버렸다"
        "당신은 아이를 가질 수 없습니다."

        "축하합니다. 고자엔딩을 맞이하였습니다."

        return
    label yuyuko_ending:
        scene bg_meikai with fade
        play music "bgm/yuahage.mp3"
        show scg_yuyuko_yosome at center with dissolve
        ch_nanimono "어머 꾀나 독특한 분이 오셨네요."
        ch_ins "여기는...?"
        ch_nanimono "이곳은 명계 죽은자들이 윤회의 섭리에 따라 모여드는 곳\n전 이 곳 명계의 유령을 관리하고 있는 유유코라 합니다."
        ch_ins "아.. 네"
        ch_yuyuko "실은 당신은 죽은게 아니예요."
        ch_ins "???"
        hide scg_yuyuko_yosome with dissolve
        show scg_yuyuko_warai with dissolve
        ch_yuyuko "하쿠레이의 무녀에게 당해 죽었다고 착각하고 본인 의지로 이곳으로 전이해왔다고 하는게 정답일까요"
        ch_ins "죽지 않았는데 제 의지로 이 곳으로 왔다고요?"
        ch_yuyuko "그렇게 되네요."
        ch_ins "아까 그 무녀가 이변의 원인의 원인이니 뭐니 하던데 대체 뭔가요?"
        ch_yuyuko "그건 당신을 중심으로 만들어진 세상에 각각의 세계의 사람들이 끌여들여지고 있기 때문아닐까요?"
        ch_ins "???"
        ch_yuyuko "하쿠레이의 무녀가 이 곳으로 올지도 모르겠네요."
        ch_ins "퀡..."
        menu:
            "실례가 안 된다면 저 좀 숨겨주실 수 있나요?":
                ch_nanimono2 "유유코 루트는 dlc추가 컨텐츠입니다."
                ch_nanimono2 "결제 수단은 없습니다."
                ch_nanimono2 "유유코님은 공략할 수 없다. 물럿거라!! 이 악귀야!"
            "마주치고 싶지 않네요.. 저어.. 어떻게 하면 다시 제가 있던 곳으로 갈 수 있을까요?":
                ch_yuyuko "글쎄요.. 저도 잘 모르는 걸요."
                hide scg_yuyuko_warai with dissolve
                show scg_reimu_1  with dissolve
                "...!?"
                ch_ins "버..벌써?"
                ch_reimu "어떻게 도망갔는지는 모르겠지만 이번에야 말로 끝이야"
                ch_ins "..."
                "나는 생각하는 것을 포기했다."
        return
    label akua_ending:
        scene bg_akuaend with fade
        play music "bgm/akuavoice.mp3"
        ch_nanimono "어서오세요.\n사후 세계에"
        ch_nanimono "당신은 불행하게도\n방금 죽었습니다."
        ch_nanimono "짧은 인생이었지만\n당신은 죽은 겁니다."
        stop music fadeout 1.0
        play music "bgm/nichizyou_konosuba.mp3"
        "... 약속된 전개로 이세계로 전생시켜줄 것 같은 신으로 보이는 여성이 있었다."
        "하지만 전혀 믿음이 가지 않는다..."
        ch_nanimono "내 이름은 아쿠아"
        ch_akua "젊은 나이에 죽은 인간을 이끄는 여신이야"
        ch_akua "당신에겐 두 가지 선택지가 있습니다."
        ch_akua "처음부터 새로운 인생을 시작할지"
        ch_akua "천국 같은 곳에 가서 할아버지 같은 생활을 할지"
        ch_akua "실은.. 천국이라는 곳은 말이야..\n너희가 상상하는 그런..."
        menu:
            "그냥 천국에 가겠습니다.":
                ch_akua "에!? 천국은 TV도 없을 뿐더러 만화나 게임도 없는데?"
                ch_akua "애초에 육체가 없으니까"
                ch_akua "야한 짓... 도 할 수 없고"
                ch_akua "영원히 햇볕이나 쬐며 살 수 밖에 없는 곳이라고?"
                ch_ins "상관없습니다. 보내주세요."
                ch_akua "하아!?"
                "축하합니다. 천국으로 가는 엔딩을 맞이하였습니다."
            "절 이세계로 보내주세요. 하하":
                ch_akua "? 이야기도 다 하지도 않았는데... 어떻게..."
                ch_akua "뭐 좋아... 오타쿠는 다르네"
                ch_ins "뻔한 전개대로 굉장한 능력이라던가 장비라던지 주는 거죠?"
                ch_akua "이야기가 빨라서 좋네."
                ch_ins "만약 그쪽 세계에 가면 언어는 어떻게 되는거죠?"
                ch_akua "우리 신들의 친절한 서포트로 네 뇌에 부하를 걸어 순식간에 습득할 수 있어"
                ch_akua "부작용으로 운이 나쁘면 바보가 될 수도 있지만"
                ch_akua "그러니 이제 굉장한 능력이니 장비를 고르는 것 뿐이네"
                ch_ins "...?"
                "지금 중대한 말이 들렸는데 바보가 뭐라고..."
                ch_akua "자 선택하도록!"
                ch_akua "당신에게 단 한 가지, 그 무엇에도 지지 않을 힘을 하사하겠습니다!"

                menu:
                    "벡터를 조종하는 능력":
                        stop music fadeout 1.0
                        play music "bgm/ahozura.mp3" fadein 5.0
                        ch_ins "저는 벡터를 조종하는 능력을 가지고 싶습니다!"
                        ch_akua "좋아 그럼 이 능력으로 선택한 거지?\n한 번 선택하면 못 바꾸니까 바꿀 거면 지금 말해라구"
                        ch_ins "이게 좋아요"
                        "..."
                        "그렇게 벡터를 조종하는 능력을 멋지게 사용하고 싶었지만 이 능력은 뇌에 부담이 많이 걸렸다."
                        play sound "bgm/kikansiagare.mp3" fadein 1.0
                        "언어지식과 함께 들어온 뇌의 한계를 뛰어넘는 능력에 뇌는 과부하가 걸리고 말았다."
                        
                        "당신은 이 날 뇌에 데미지를 입었습니다.\n이제부터 연산을 외부에 맡겨야 합니다."
                        "하지만 보내진 곳은 중세시대로 뛰어난 기술을 가진 헤븐캔슬러나 전기능력자 네트워크는 존재하지 않습니다."
                        "축하합니다. 바보엔딩을 맞이하였습니다."
                    "약속된 승리의 검 엑스칼리버":
                        scene bg_explosion with fade
                        stop music fadeout 1.0
                        play music "bgm/KonosubaExplosion.mp3" fadein 1.0
                        "당신은 전설의 성검을 가지고 이세계에 갔지만...\n(와가 나와 메구밍...)"
                        "그곳은 머리가 이상한 폭렬마가 매일 마법을 연습하던 곳이었습니다."

                        ch_ins "..잠.."
                        ch_ins "끄아아아아악"
                        stop music fadeout 1.0
                        show eileen movie
                        "폭렬 폭렬 랄랄라~"
                        "박그네츠 박그네츠 랄랄라~"
                        "바쿠레츠 바쿠레츠 랄랄라~\n영상을 감상하고 싶다면 넘기지마욧"
                        "박그네츠 박그네츠 랄라"
                        "받아라 익쓰 플로젼!"
                        "축하합니다.\n우연히 떨어진 이세계 폭렬마법에 의한 사망 엔딩을 맞이하였습니다."
                    "여신을 끌고 간다.":
                        "구현중"

        return 