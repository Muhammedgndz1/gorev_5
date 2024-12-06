TurtleFollow

TurtleFollow, ROS 2 kullanarak Turtlesim simülasyon ortamında özel servisler oluşturma ve kullanma örneğini göstermek için tasarlanmış bir pakettir. Bu proje, iki ana servis içerir:

Kaplumbağa Oluşturma Servisi: Turtlesim ortamında dinamik olarak kaplumbağalar oluşturur.

Kaplumbağa Takip Servisi: Bir veya birden fazla kaplumbağanın hedef bir kaplumbağayı takip etmesini sağlar.

Gereksinimler

ROS 2 Humble veya daha yeni bir sürüm

Python 3.8+

Turtlesim paketi (sudo apt install ros-humble-turtlesim)

a şeçeneği:
turtle_teleop_key paketini yükleyin:
sudo apt install ros-humble-turtle-teleop

TurtleSim'i başlatın:
ros2 run turtlesim turtlesim_node

Turtle'ı klavye ile kontrol etmek için teleop düğümünü çalıştırın:
ros2 run turtle_teleop_key teleop_turtle_key

Bu komut ile ekranda şu mesajı görmelisiniz:
Use arrow keys to control the turtle.

Burada, ok tuşlarıyla Turtle'ı hareket ettirebilirsiniz. Bu şekilde, Turtle'ınızı istediğiniz gibi yönlendirebilirsiniz.

Farklı Turtle'ları Kontrol Etme
Eğer birden fazla turtle varsa, her birini ayrı ayrı kontrol edebilirsiniz. 

Aşağıdaki komutla, turtle1 isimli turtle'ı klavye ile kontrol edebilirsiniz:
ros2 run turtle_teleop_key teleop_turtle_key --ros-args -r __node:=teleop_turtle_key -r /turtle1/teleop_key:=/turtle1

Bu komutla, yalnızca turtle1'i kontrol edebilirsiniz. Aynı komutu diğer turtle'lar için de çalıştırabilirsiniz.


Diğer seçenekler(b ve c) için Kurulum:

Depoyu klonlayın:
git clone https://github.com/Muhammedgndz1/gorev_5.git

cd turtlefollow_ws

Workspace'i derleyin:

colcon build
source install/setup.bash

Kullanım

Kaplumbağa Oluşturma Servisi

Turtlesim düğümünü başlatın:
ros2 run turtlesim turtlesim_node

Kaplumbağa oluşturma servisini çalıştırın:
ros2 run turtlefollow_ws turtle_creation_service

Servisi çağırıp kaplumbağalar oluşturun:
ros2 service call /turtles_create turtlefollow/srv/CreateTurtles "{count: 3}"

Kaplumbağa Takip Servisi

Kaplumbağa takip servisini çalıştırın:
ros2 run turtlefollow turtle_follow_service

Servisi çağırıp kaplumbağaları hedef bir kaplumbağayı takip ettirin:
ros2 service call /turtles_follow turtlefollow/srv/FollowTurtle "{target_name: 'turtle1'}"

Dosya Yapısı

├── turtlefollow
│   ├── __init__.py
│   ├── turtle_creation_service.py
│   ├── turtle_follow_service.py
├── srv
│   ├── CreateTurtles.srv
│   └── FollowTurtle.srv
├── package.xml
├── CMakeLists.txt
└── setup.py

turtle_creation_service.py: Kaplumbağa oluşturma mantığını içerir.

turtle_follow_service.py: Kaplumbağaları hedef bir kaplumbağayı takip etmeye yönelik mantığı uygular.

CreateTurtles.srv: Kaplumbağa oluşturma için özel bir servis.

FollowTurtle.srv: Kaplumbağa takip için özel bir servis.

Katkıda Bulunma

Bu depoyu forklayarak çekme istekleri gönderebilirsiniz. Öneriler ve iyileştirmeler her zaman memnuniyetle karşılanır!

Destek

Sorularınız veya sorunlarınız için lütfen GitHub deposunda bir sorun (“issue”) oluşturun.

Bilgilendirme

Bu proje, ROS 2'de özel servislerin kullanımını göstermek için eğitim amaçlıdır.
